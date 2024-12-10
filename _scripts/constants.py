NEWS_SOURCES_FILENAME = "news_sources.yaml"
RAW_LINKS_FILENAME = "raw_links.txt"
PROCESSED_LINKS_FILENAME = "processed_links.txt"
NEWS_LINKS_MD_FILENAME = "news_links.md"
NEWS_LINK_MD_FORMAT = "* [`{}` {}]({})\n"
USER_INPUT_YES = "y"
USER_INPUT_NO = "n"
VERIFIED_SOURCES_KEY = "verified_sources"
SOURCE_TITLE_KEY = "title"
SOURCE_URL_KEY = "url"
SOURCE_INFO_KEY = "info"
SOURCE_RANK_KEY = "rank"
PROCESSED_LINK_FORMAT = "{}[{}][{}]\n"
NEWS_POST_FILENAME_FORMAT = "{}-weekly-news.markdown"
NEWS_POST_COMMIT_MSG = "feat: weekly news post added {}"
NEWS_POST_TEMPLATE = """
---
layout: post
title:  "✊ Progressive News | {}"
date:   {} 11:00:00 +0800
categories: weekly news
---

### International

* [Article](https://website.com/)

### China

* [Article](https://website.com/)

### South Asia

* [Article](https://website.com/)

### Southeast Asia

* [Article](https://website.com/)

### East Asia

* [Article](https://website.com/)

### Central Asia

* [Article](https://website.com/)

### West Asia (Middle East)

* [Article](https://website.com/)

### Russia

* [Article](https://website.com/)

### Europe

* [Article](https://website.com/)

### Africa

* [Article](https://website.com/)

### North America

* [Article](https://website.com/)

### Latin America and The Caribbean

* [Article](https://website.com/)

### Oceania

* [Article](https://website.com/)

### Miscellaneous

* [Article](https://website.com/)
"""
