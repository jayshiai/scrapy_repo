import scrapy
from ucc.items import TeachItem
import json

class TeacherSpider(scrapy.Spider):
    name = "teacher"
    allowed_domains = ["www.imo.universite-paris-saclay.fr"]
    start_urls = ["https://www.imo.universite-paris-saclay.fr/en/people/json/?_=1691870610673"]

    def parse(self, response):
        data = json.loads(response.text)['data']
        for item in data:
            tech = TeachItem()
            tech['name'] = item['nom']
            tech['statut'] = item['fonction']
            tech['bureau'] = item['bureau']
            tech['equipe'] = item['equipe']

            yield tech