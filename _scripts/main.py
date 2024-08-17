import logging
from datetime import datetime

from selenium import webdriver
from utilities import clear_file
from news_research import perform_news_research
from news_links_markdown import process_markdown_links
from news_post import create_weekly_news_post_template
from constants import (
    NEWS_SOURCES_FILENAME,
    RAW_LINKS_FILENAME,
    PROCESSED_LINKS_FILENAME,
    NEWS_LINKS_MD_FILENAME,
)


logging.basicConfig(level=logging.INFO)


def run():
    current_date = datetime.now()
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")

    # Ensure files are clear
    clear_file(RAW_LINKS_FILENAME)
    clear_file(PROCESSED_LINKS_FILENAME)
    clear_file(NEWS_LINKS_MD_FILENAME)

    # STEP 1
    logging.info("Starting news research.")
    with webdriver.Firefox() as driver:
        perform_news_research(driver, NEWS_SOURCES_FILENAME)
    logging.info("News research completed.")

    # STEP 2
    logging.info("Processing markdown links.")
    with webdriver.Firefox(options=options) as headless_driver:
        process_markdown_links(
            headless_driver, PROCESSED_LINKS_FILENAME, NEWS_LINKS_MD_FILENAME
        )
    logging.info("Markdown link processing completed.")

    # STEP 3
    logging.info("Creating weekly news post template.")
    create_weekly_news_post_template(current_date)
    logging.info("Weekly news post template created.")


if __name__ == "__main__":
    run()
