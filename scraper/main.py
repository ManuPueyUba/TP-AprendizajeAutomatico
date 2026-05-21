from scraper.storage import load_json, save_json
from scraper.materia_scraper import scrape_materias
from scraper.repo_scraper import scrape_repos
from scraper.scrape_all_repos import scrape_all_repos

MATERIAS_PATH = "scraper/output/materias.json"
REPOS_PATH = "scraper/output/repos.json"


def get_materias():

    materias = load_json(MATERIAS_PATH)

    if materias:
        print("Usando materias cacheadas")
        return materias

    print("Scrapeando materias...")

    materias = scrape_materias()

    save_json(MATERIAS_PATH, materias)

    return materias


def main():


    all_repos = scrape_all_repos()

    save_json(REPOS_PATH, all_repos)

    print("\nRepos guardados")


if __name__ == "__main__":
    main()