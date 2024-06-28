"""
fetch_youtube_titles.py
This script reads a list of YouTube links from a file, validates the links, fetches the video titles
using Selenium with the Firefox WebDriver, and writes the titles and links to a Markdown file in a
formatted manner. It also ensures the titles are tidied by removing any characters that might break
the Markdown formatting, such as '|', '[', and ']'. The script logs its progress and any errors
encountered for better traceability.
"""

import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def read_youtube_links(file_path):
    logging.info(f"Reading YouTube links from {file_path}")
    with open(file_path, "r") as file:
        links = file.readlines()
    # Remove empty lines and strip whitespace
    links = [link.strip() for link in links if link.strip()]
    logging.info(f"Found {len(links)} YouTube links in {file_path}")
    return links


def is_valid_youtube_link(link):
    is_valid = link.startswith("https://youtu.be/") or link.startswith(
        "https://www.youtube.com/"
    )
    if not is_valid:
        logging.warning(f"Invalid YouTube link: {link}")
    return is_valid


def get_video_title(link, driver):
    logging.info(f"Fetching title for {link}")
    driver.get(link)
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
        logging.error(f"Error fetching title for {link}: {e}")
        return None


def tidy_title(title):
    # Remove characters that can break markdown
    tidy = re.sub(r"[\|\[\]]", " ", title)
    return tidy


def main():
    file_path = "youtube_links.txt"
    output_file = "links.md"
    youtube_links = read_youtube_links(file_path)

    options = webdriver.FirefoxOptions()
    options.add_argument(
        "--headless"
    )  # Run headless Firefox for less resource consumption
    driver = webdriver.Firefox(options=options)

    with open(output_file, "w") as f:
        for link in youtube_links:
            if is_valid_youtube_link(link):
                title = get_video_title(link, driver)
                if title:
                    tidy_title_text = tidy_title(title)
                    logging.info(f"Successfully retrieved title: {tidy_title_text}")
                    f.write(f"* [{tidy_title_text}]({link})\n")
                else:
                    logging.error(f"Failed to retrieve title for {link}")

    driver.quit()
    logging.info("Finished processing all links")


if __name__ == "__main__":
    main()
