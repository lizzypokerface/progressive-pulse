import logging
from selenium.webdriver.remote.webdriver import WebDriver
from utilities import (
    load_yaml_file,
    clear_txt_file,
    get_datetime_one_week_ago,
)
from constants import (
    RAW_LINKS_FILENAME,
    PROCESSED_LINKS_FILENAME,
    USER_INPUT_YES,
    USER_INPUT_NO,
    VERIFIED_SOURCES_KEY,
    SOURCE_TITLE_KEY,
    SOURCE_URL_KEY,
    PROCESSED_LINK_FORMAT
)

def process_links(
    raw_links_file: str, processed_links_file: str, source_title: str
) -> None:
    # Read links from raw_links.txt and write to processed_links.txt
    with open(raw_links_file, "r") as raw_file, open(
        processed_links_file, "a"
    ) as processed_file:
        for line in raw_file:
            url = line.strip()
            processed_file.write(PROCESSED_LINK_FORMAT.format(url, source_title))


def perform_news_research(driver: WebDriver, new_sources_filename: str):

    news_sources = load_yaml_file(new_sources_filename)

    for source in news_sources[VERIFIED_SOURCES_KEY]:
        logging.info(
            f"Title: {source[SOURCE_TITLE_KEY]} \nURL: {source[SOURCE_URL_KEY]}"
        )

        # Log the date from one week ago to inform
        # the user when to start retrieving articles.
        logging.info(
            f"Date one week ago: {get_datetime_one_week_ago().strftime('%d %b %y')}"
        )

        driver.get(source["url"])

        logging.info("Please add links to raw_links.txt manually.")

        user_input = input("Save and continue? [y/n] ")

        if user_input.lower() == USER_INPUT_YES:
            process_links(
                RAW_LINKS_FILENAME, PROCESSED_LINKS_FILENAME, source[SOURCE_TITLE_KEY]
            )
            clear_txt_file(RAW_LINKS_FILENAME)
        elif user_input.lower() == USER_INPUT_NO:
            logging.info("Exited without saving.")
            break
        else:
            logging.info(
                f"Invalid input: '{user_input}'. Please enter {USER_INPUT_YES} or {USER_INPUT_NO}."
            )
            continue

    driver.quit()
