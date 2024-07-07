"""
This script generates a markdown file for a weekly news post, using the current date or a date provided as a command line argument.

It follows these steps:

1. Configures logging to provide timestamped informational and error messages.
2. Defines a function to parse the input date string and handle errors if the format is incorrect.
3. Retrieves the date from the command line argument if provided, or uses the current date.
4. Formats the date into strings suitable for use in the filename and post content.
5. Uses a template string to create the content of the markdown file, with sections for different regions of the world.
6. Writes the generated content to a markdown file named according to the formatted date.
7. Logs the success or failure of the file creation process.

Usage:
- To use the current date: `python script_name.py`
- To specify a date: `python script_name.py dd/mm/yyyy`
"""

import os
import sys
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


# Function to parse input date
def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%d/%m/%Y")
    except ValueError:
        logging.error("Incorrect date format. Please use dd/mm/yyyy.")
        sys.exit(1)


# Get the date from the command line argument if provided
if len(sys.argv) > 1:
    input_date_str = sys.argv[1]
    current_date = parse_date(input_date_str)
else:
    current_date = datetime.now()

date_str = current_date.strftime("%Y-%m-%d")
date_display = current_date.strftime("%d %B %Y")

# Template for the post
template = f"""---
layout: post
title:  "✊ Progressive News | {date_display}"
date:   {date_str} 11:00:00 +0800
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
"""

# Define the filename
filename = f"{date_str}-weekly-news.markdown"

# Write the template to the file in the current directory
try:
    with open(filename, "w") as file:
        file.write(template)
    logging.info(f"File {filename} created successfully in the current directory.")
except Exception as e:
    logging.error(f"Failed to create file {filename}. Error: {e}")
