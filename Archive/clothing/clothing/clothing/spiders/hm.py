import scrapy
import json
from clothing.items import ClothingItem
class HmSpider(scrapy.Spider):
    name = "hm"
    allowed_domains = ["www2.hm.com"]
    start_urls = ["https://www2.hm.com"]

    def parse(self, response):

        with open("data.json") as f:
            data = json.load(f)['products']
        print(data)
        for item in data:
           product = ClothingItem()

           product['name'] = item['title']
           product['price'] = item['price']
           product['img_url'] = item['image'][0]['src']
           product['product_url'] = "www2.hm.com" + item['link']
           product['website'] = "H&M"

           yield response.follow(item['link'], callback=self.parse_description, meta = dict(
               product = product
           ))

    def parse_description(self,response):
        product = response.meta['product']

        data = json.loads(response.xpath('//script[@id="product-schema"]/text()').get())['description']
        product['description'] = data

        yield data