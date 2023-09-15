import scrapy


class AgentSpider(scrapy.Spider):
    name = "agent"
    allowed_domains = ["housing.com"]
    start_urls = ["https://housing.com/"]

    def parse(self, response):
        pass
