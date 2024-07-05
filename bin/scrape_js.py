#!/usr/bin/env python

from decouple import config
from playwright.sync_api import Playwright, sync_playwright
from pathlib import Path

url = config('URL', default='https://apps.health.ny.gov/statistics/environmental/public_health_tracking/tracker/#/CCList')


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)

    # Wait for the tables to be loaded. Adjust the selector as needed.
    page.wait_for_selector("div.tab-content")

    # Get all table elements
    tables = page.locator("div.tab-content table")

    # Extract the HTML content of each table and save to a file
    raw_dir = Path("../raw")
    raw_dir.mkdir(parents=True, exist_ok=True)
    with open(raw_dir / "tables.html", "w", encoding="utf-8") as file:
        for index in range(tables.count()):
            table_html = tables.nth(index).inner_html()
            file.write(f"<!-- Table {index + 1} -->\n")
            file.write(table_html)
            file.write("\n\n")

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
