import scrapy


class PsySpider(scrapy.Spider):
    name = "psy"
    allowed_domains = ["www.google.com"]
    start_urls = ["https://www.google.com/maps"]

    def parse(self, response):
        pass
