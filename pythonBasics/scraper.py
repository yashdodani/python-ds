import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.geeksforgeeks.org/") # url to scrap

soup = BeautifulSoup(req.content, "html.parser") # to insert what to request and how to
# beautifulSoup is used to scrap content from a website

res = soup.title 

# print(soup.prettify())
print(res.get_text()) # to get everything in the form of text 
