from playwright.sync_api import sync_playwright
from scraper.config import BASE_URL


def scrape_materias():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto(BASE_URL)

        # Esperar a que aparezcan las materias
        page.wait_for_selector("div.css-8paexb")

        cards = page.query_selector_all("div.css-8paexb")

        materias = []

        for card in cards:

            title_element = card.query_selector("h2")

            if not title_element:
                continue

            title = title_element.inner_text()

            code_elements = card.query_selector_all("p.css-1noieid")

            codes = [c.inner_text() for c in code_elements]

            materias.append({
                "nombre": title,
                "codigos": codes
            })

        browser.close()

        return materias