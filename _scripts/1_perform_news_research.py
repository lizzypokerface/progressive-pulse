import yaml
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Configuring the logging
logging.basicConfig(level=logging.INFO)

# Load the YAML file
with open("news_sources.yaml") as file:
    news_sources = yaml.safe_load(file)

# Loop through each news source
for source in news_sources["verified_sources"]:
    logging.info(f"Title: {source['title']} \nURL: {source['url']}")

    # Open browser
    driver = webdriver.Firefox()
    driver.get(source["url"])

    # Ask user to continue to the next news source or exit
    user_input = input("Continue to next news source? [y/n] ")
    if user_input.lower() == "n":
        driver.quit()
        break

    # Close the current browser
    driver.quit()

logging.info("News research complete.")
