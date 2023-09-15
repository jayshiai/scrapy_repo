import scrapy
import re
import json
from carbon.items import CarbonItem
class CleanSpider(scrapy.Spider):
    name = "clean"
    allowed_domains = ["flo.uri.sh"]
    start_urls = ["https://flo.uri.sh/visualisation/12603037/embed?auto=1"]

    def parse(self, response):
        data = json.loads(re.findall(r'_Flourish_data\s*=\s*({.+?}),\n', response.text)[0])['data']
        for item in data:
            clean = CarbonItem()
            clean['type'] = item['filter']
            clean['date'] = item['label']
            clean['price'] = item['value']

            yield clean
