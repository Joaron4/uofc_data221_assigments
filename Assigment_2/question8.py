# Question 8 (1 Point)
"""
This task focuses on extracting structured heading information from a webpage.
Using the same Wikipedia page:
https://en.wikipedia.org/wiki/Data_science
• Extract all <h2> section headings from the main content area (div with id mw-content-
text).
• Do not include headings containing the words: References, External links, See also, or
Notes.
• Remove any [edit] text from headings.
• Save the headings to headings.txt, one per line, in order
"""

import requests
from bs4 import BeautifulSoup as BS
URL = "https://en.wikipedia.org/wiki/Data_science"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
wikipedia_response = requests.get(URL, headers=headers).text
parsed_html_document = BS(wikipedia_response,"html5lib")
string_document = ""
count = 1
content_div = parsed_html_document.find("div", id="mw-content-text")
for i in content_div.find_all("h2"):
    if i.text not in ["References", "External links", "See also", "Notes","Contents"]:
        string_document +=  str(count) + ". " + i.text.replace("[edit]", "").strip() + "\n"
        count += 1
final_document = string_document.strip()
fhand = open('data/output/headings.txt', 'w')
fhand.write(final_document)
fhand.close()