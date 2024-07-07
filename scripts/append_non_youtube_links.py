"""
This script reads a list of non-YouTube links from a file, prompts the user to input the title for each link,
tidies the titles by removing any characters that might break the Markdown formatting, and appends the links
with titles to the same Markdown file (`links.md`). The script includes logging for progress tracking and error handling.
"""

import logging
import re

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def read_other_links(file_path):
    logging.info(f"Reading other links from {file_path}")
    with open(file_path, "r") as file:
        links = file.readlines()
    # Remove empty lines and strip whitespace
    links = [
        link.strip() for link in links if link.strip()
    ]  # Clean up lines by removing empty ones and stripping whitespace
    return links


def tidy_title(title):
    # Remove characters that can break markdown
    tidy = re.sub(r"[\|\[\]]", "", title)
    return tidy


def main():
    file_path = "other_links.txt"
    output_file = "links.md"
    other_links = read_other_links(file_path)

    with open(output_file, "a") as f:
        for link in other_links:
            try:
                title = input(f"Enter the title for the link {link}: ").strip()
                if title:
                    tidy_title_text = tidy_title(title)
                    logging.info(f"Successfully retrieved title: {tidy_title_text}")
                    f.write(f"* [{tidy_title_text}]({link})\n")
                else:
                    logging.warning(f"No title provided for link: {link}")
            except Exception as e:
                logging.error(f"Error processing link {link}: {e}")

    logging.info("Finished processing all links")


if __name__ == "__main__":
    main()
