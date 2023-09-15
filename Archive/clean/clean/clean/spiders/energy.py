import scrapy
import json
from clean.items import CleanItem

class EnergySpider(scrapy.Spider):
    name = "energy"
    allowed_domains = ["www.cleanenergycouncil.org.au"]
    start_urls = ["https://www.cleanenergycouncil.org.au/"]

    def parse(self, response):
        with open('data.json', 'r') as f:
            data = json.load(f)
        for item in data:
            shop = CleanItem()
            name = item['firstName'].strip() + " " +item['lastName']
            shop['name'] = name.strip()
            shop['location'] = item['location']
            shop['telephone'] = item['phone'].strip()
            shop['business'] = item['business']
            yield shop
