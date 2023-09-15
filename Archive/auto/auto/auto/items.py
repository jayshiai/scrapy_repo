# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AutoItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price = scrapy.Field()
    launch = scrapy.Field()
    engine = scrapy.Field()
    fuel = scrapy.Field()
    transmission = scrapy.Field()
    mileage = scrapy.Field()