from playwright.sync_api import sync_playwright
from scraper.config import BASE_URL


def scrape_repos(codigo):

    url = f"{BASE_URL}?c={codigo}"

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto(url)

        page.wait_for_timeout(5000)

        repos = page.query_selector_all(
            "div.styles_main-content__S0u-T"
        )

        data = []

        for repo in repos:

            link_element = repo.query_selector("a")

            if not link_element:
                continue

            github_url = link_element.get_attribute("href")
            repo_name = link_element.inner_text()

            description = ""

            description_elements = repo.query_selector_all("p")

            if len(description_elements) > 0:
                description = description_elements[0].inner_text()

            data.append({
                "repo_name": repo_name,
                "github_url": github_url,
                "description": description
            })

        browser.close()

        return data