# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CarbonItem(scrapy.Item):
    # define the fields for your item here like:
    type = scrapy.Field()
    date = scrapy.Field()
    price = scrapy.Field()
