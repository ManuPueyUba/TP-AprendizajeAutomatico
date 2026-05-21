from scraper.storage import load_json, save_json
from scraper.materia_scraper import scrape_materias
from scraper.repo_scraper import scrape_repos

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

    materias = get_materias()

    all_repos = []

    for materia in materias:

        print(f"\nMateria: {materia['nombre']}")

        for codigo in materia["codigos"]:

            print(f"  Código: {codigo}")

            try:

                repos = scrape_repos(codigo)

                all_repos.append({
                    "materia": materia["nombre"],
                    "codigo": codigo,
                    "repos": repos
                })

                print(f"  Repos encontrados: {len(repos)}")

            except Exception as e:

                print(f"  Error: {e}")

    save_json(REPOS_PATH, all_repos)

    print("\nRepos guardados")


if __name__ == "__main__":
    main()