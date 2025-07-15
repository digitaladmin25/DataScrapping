import requests
from bs4 import BeautifulSoup
import csv

# Make a request
page = requests.get(
    "https://bt.design/dot-with-arm-chair.html")
soup = BeautifulSoup(page.content, 'html.parser')

# Extract title of page
page_title = soup.title

# Extract body of page
page_body = soup.body

# Extract head of page
page_head = soup.head

# print the result
print(page_body)