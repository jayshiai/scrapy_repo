# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ClothingItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price = scrapy.Field()
    img_url = scrapy.Field()
    product_url = scrapy.Field()
    website = scrapy.Field()
    description = scrapy.Field()
