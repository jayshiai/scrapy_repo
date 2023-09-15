# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FootywireItem(scrapy.Item):
    # define the fields for your item here like:
    year = scrapy.Field()
    round = scrapy.Field()
    match = scrapy.Field()
    date = scrapy.Field()
    time = scrapy.Field()
    venue = scrapy.Field()
    team = scrapy.Field()
    player = scrapy.Field()
    born = scrapy.Field()
    weight = scrapy.Field()
    height = scrapy.Field()
    position  = scrapy.Field()
    k = scrapy.Field()
    tog = scrapy.Field()

