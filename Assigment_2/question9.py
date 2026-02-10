# Question 9 (1 Point)
""""
In this question, you will extract tabular data from a webpage and store it in a structured format.
Scrape the Wikipedia page:
https://en.wikipedia.org/wiki/Machine_learning
• Locate the first table inside the main content area (div with id mw-content-text) that
contains at least 3 data rows.
• Extract the table header from <th> tags if present; otherwise create headers named col1,
col2, col3, etc.
• Some rows may have fewer columns than others; pad missing values with empty strings.
• Save the extracted table to wiki_table.csv.
"""

import requests
from bs4 import BeautifulSoup as BS
import pandas as pd

URL = "https://en.wikipedia.org/wiki/Machine_learning"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
wikipedia_response = requests.get(URL, headers=headers).text
parsed_html_document = BS(wikipedia_response,"html5lib")
first_table = parsed_html_document.find("div", id="mw-content-text").find("table")
rows = first_table.find_all("tr")

if len(rows) < 4:
    parsed_tables_contents = parsed_html_document.find("div", id="mw-content-text").find_all("table")
    for i in parsed_tables_contents:     
        rows = i.find_all("tr")
        if len(rows) >= 4:
            first_table = i
            break
        
headers = [i.text for i in first_table.find_all("th")]
if headers == []:
    num_cols = max([len(r.find_all(["td", "th"])) for r in first_table.find_all("tr")])
    headers = [f"col{i+1}" for i in range(num_cols)]
body_rows = first_table.find_all("tr")


table_data = []
n_cols = len(headers)

for tr in body_rows:
    cells = tr.find_all(["td", "th"])
    values = [c.text for c in cells]

    values = (values + [""] * n_cols)[:n_cols]
    table_data.append(values)

wikipedia_dataframe = pd.DataFrame(table_data, columns=headers)
wikipedia_dataframe.to_csv("data/output/wiki_table.csv", index=False)
print(wikipedia_dataframe)

