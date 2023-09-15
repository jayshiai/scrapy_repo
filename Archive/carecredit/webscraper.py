import requests
from bs4 import BeautifulSoup
url = "https://www.passiton.com/inspirational-quotes"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html5lib")

print(soup)