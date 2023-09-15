# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CarsItem(scrapy.Item):
    # define the fields for your item here like:
    make = scrapy.Field()
    model = scrapy.Field()
    price = scrapy.Field()
    age = scrapy.Field()
    milage = scrapy.Field()
    colour = scrapy.Field()
    fuel = scrapy.Field()
    transmission = scrapy.Field()
    body = scrapy.Field()
    location = scrapy.Field()
