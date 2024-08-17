import logging
import re
from typing import Optional

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from constants import NEWS_LINK_MD_FORMAT


def fetch_links(file_path: str) -> list[str]:
    logging.info(f"Reading links from {file_path}")
    with open(file_path, "r") as file:
        links = file.readlines()
    # Remove empty lines and strip whitespace
    links = [link.strip() for link in links if link.strip()]
    logging.info(f"Found {len(links)} links in {file_path}")
    return links


def is_valid_youtube_link(link: str) -> bool:
    return link.startswith("https://youtu.be/") or link.startswith(
        "https://www.youtube.com/"
    )


def tidy_title(title: str) -> str:
    # Remove characters that can break markdown
    tidy = re.sub(r"[\|\[\]]", " ", title)
    return tidy


def remove_source(link: str) -> str:
    return re.sub(r"\[.*?\]$", "", link)


def extract_source(link: str) -> str:
    match = re.search(r"\[(.*?)\]$", link)
    return match.group(1) if match else "Unknown Source"


def get_youtube_video_title(driver: WebDriver, url: str) -> Optional[str]:
    logging.info(f"Fetching title for {url}")
    driver.get(url)
    try:
        # Wait for the title element to be present
        title_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[@id='above-the-fold']/div[@id='title']//yt-formatted-string[@class='style-scope ytd-watch-metadata']",
                )
            )
        )
        return title_element.text
    except Exception as e:
        logging.error(f"Error fetching title for {url}: {e}")
        return None


def process_markdown_links(
    driver: WebDriver, processed_links_filename: str, news_links_md_filename: str
) -> None:

    processed_links = fetch_links(processed_links_filename)
    youtube_links = []
    other_links = []

    for link in processed_links:
        if is_valid_youtube_link(link):
            youtube_links.append(link)
        else:
            other_links.append(link)

    with open(news_links_md_filename, "w") as f:
        for link in youtube_links:
            yt_link = remove_source(link)
            source = extract_source(link)
            title = get_youtube_video_title(driver, yt_link)
            if title:
                tidy_title_text = tidy_title(title)
                logging.info(f"Successfully retrieved title: {tidy_title_text}")
                f.write(NEWS_LINK_MD_FORMAT.format(source, tidy_title_text, yt_link))
            else:
                logging.error(f"Failed to retrieve title for {yt_link}")

        logging.info("Please add other link titles manually.")

        for link in other_links:
            try:
                other_link = remove_source(link)
                source = extract_source(link)
                title = input(f"Enter the title for the link {other_link}: ").strip()
                if title:
                    tidy_title_text = tidy_title(title)
                    logging.info(f"Successfully retrieved title: {tidy_title_text}")
                    f.write(
                        NEWS_LINK_MD_FORMAT.format(source, tidy_title_text, other_link)
                    )
                else:
                    logging.warning(f"No title provided for link: {link}")
            except Exception as e:
                logging.error(f"Error processing link {link}: {e}")

    logging.info("Finished processing all links")
