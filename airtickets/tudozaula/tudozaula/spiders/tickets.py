import scrapy


class TicketsSpider(scrapy.Spider):
    name = "tickets"
    allowed_domains = ["interline.tudoazul.com"]
    start_urls = ["https://interline.tudoazul.com/"]

    def parse(self, response):
        pass
