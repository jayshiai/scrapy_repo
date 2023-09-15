import requests
from bs4 import BeautifulSoup
url = "https://www.passiton.com/inspirational-quotes"

page = requests.get(url)

soup = BeautifulSoup(page.content, "html5lib")

div = soup.find("div", attrs={"id":"all_quotes"})

data = div.findAll("div")

for i in data:
    url = i.a["href"]
    url = "https://www.passiton.com/"+url
    r= requests.get(url)
    soup = BeautifulSoup(r.content, "html5lib")

    data = soup.find("h5", attrs={"class" : "alt-font text-extra-dark-gray quotation"})
    quote = data.text
    print(quote)