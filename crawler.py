import requests
from bs4 import BeautifulSoup

url = "https://www.gentool.net/data/zh/"
r = requests.get(url)
soup = BeautifulSoup(r.content, features="html.parser")
links = soup.find_all("a")

for link in links:
    print (link.get("href"), link.text)
