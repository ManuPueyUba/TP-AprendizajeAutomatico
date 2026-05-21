import requests

from scraper.storage import append_jsonl
from scraper.config import GITHUB_URL, OUTPUT_PATH


def fetch_and_save_fiuba_repos():

    page = 1
    total_count = None
    total_saved = 0

    while total_count is None or total_saved < total_count:

        response = requests.get(
            GITHUB_URL,
            params={
                "q": "topic:fiuba fork:true",
                "sort": "updated",
                "order": "desc",
                "page": page,
                "per_page": 100,
            },
            headers={
                "Accept": "application/vnd.github.v3+json",
            }
        )

        data = response.json()

        if not data.get("items"):
            break

        total_count = data["total_count"]

        for repo in data["items"]:

            parsed_repo = {
                "name": repo["name"],
                "full_name": repo["full_name"],
                "description": repo["description"],
                "url": repo["html_url"],
                "topics": repo["topics"],
                "language": repo["language"],
                "stars": repo["stargazers_count"],
                "updated_at": repo["updated_at"],
            }

            append_jsonl(
                OUTPUT_PATH,
                parsed_repo
            )

            total_saved += 1

        print(f"Página {page}")
        print(f"Repos guardados: {total_saved}")

        page += 1