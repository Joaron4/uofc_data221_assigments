# Question 7 (1 Point)
"""
n this question, you will work on extracting structured content from a webpage using Beautiful-
Soup.
Scrape the Wikipedia page:
https://en.wikipedia.org/wiki/Data_science
Write a program using requests and BeautifulSoup that:
• Extracts and prints the page title from the <title> tag.
• Extracts the first paragraph from the main article content inside the div with id mw-
content-text.
• The paragraph must contain at least 50 characters (after stripping whitespace)

"""

import requests
from bs4 import BeautifulSoup as BS
URL = "https://en.wikipedia.org/wiki/Data_science"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
wikipedia_response = requests.get(URL, headers=headers).text
parsed_html_document = BS(wikipedia_response,"html5lib")
page_title = parsed_html_document.find("title").text
print("Page Title:", page_title)

content_div = parsed_html_document.find("div", id="mw-content-text")
if content_div:
    paragraphs = content_div.find_all("p")
    for p in paragraphs:
        text = p.text.strip()
        if len(text) >= 50:
            print(text)
            break

