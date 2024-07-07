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

### Other

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
