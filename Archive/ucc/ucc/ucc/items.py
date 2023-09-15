# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UccItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    type = scrapy.Field()
    file_number = scrapy.Field()
    secured_party_info = scrapy.Field()
    status = scrapy.Field()
    filling_date = scrapy.Field()
    lapse_date = scrapy.Field()

class TeachItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    statut = scrapy.Field()
    bureau = scrapy.Field()
    equipe = scrapy.Field()
