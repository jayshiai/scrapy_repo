# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CzechItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    street = scrapy.Field()
    city = scrapy.Field()
    zip = scrapy.Field()
    phone = scrapy.Field()
    email = scrapy.Field()
    type = scrapy.Field()
    Mon = scrapy.Field()
    Tue = scrapy.Field()
    Wed = scrapy.Field()
    Thu = scrapy.Field()
    Fri = scrapy.Field()
    Sat = scrapy.Field()
