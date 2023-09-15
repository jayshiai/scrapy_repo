import scrapy


class HouzzSpider(scrapy.Spider):
    name = "houzz"
    allowed_domains = ["www.houzz.com"]
    start_urls = ["https://www.houzz.com/"]

    def parse(self, response):
        pass
