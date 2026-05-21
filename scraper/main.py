from scraper.github_api import fetch_and_save_fiuba_repos

REPOS_PATH = "scraper/output/repos.json"


def get_repos():


    print("Obteniendo repos desde GitHub API...")

    fetch_and_save_fiuba_repos()



def main():

    repos = get_repos()



if __name__ == "__main__":
    main()