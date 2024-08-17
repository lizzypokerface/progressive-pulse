import logging
from news_research import perform_news_research
from selenium import webdriver
from constants import NEWS_SOURCES_FILENAME

logging.basicConfig(level=logging.INFO)

def run():
    driver = webdriver.Firefox()
    perform_news_research(driver, NEWS_SOURCES_FILENAME)

if __name__ == "__main__":
    run()
