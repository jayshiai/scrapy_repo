import scrapy
from scrapy_selenium import SeleniumRequest

class CarsSpider(scrapy.Spider):
    name = "cars"
    allowed_domains = ["www.carjam.co.nz"]

    def parse(self, response):
        yield SeleniumRequest(url="https://www.carjam.co.nz/car/?plate=TI3854",callback=self.parse_page, wait_time=10000)

    def parse_page(self,response):
        print(response.text)
        input("Press ENTER to exit\n")
