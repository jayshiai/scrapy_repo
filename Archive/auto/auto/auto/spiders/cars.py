import scrapy
from auto.items import AutoItem

class CarsSpider(scrapy.Spider):
    name = "cars"
    allowed_domains = ["www.autocarindia.com"]
    start_urls = ["https://www.autocarindia.com/upcoming-cars"]

    def parse(self, response):
        data = response.xpath('//div[@class="car-lis-sec bg-white box-shadow margin_bottom_25 mb-mb-15 mob-pad-col mb-pt-5"]')

        for item in data:
            car = AutoItem()
            car['name'] = item.xpath('./div[1]/div[2]/h3/a/text()').get().strip()
            car['price'] = item.xpath('./div[1]/div[2]/div[1]/p/span/text()').get().strip()
            car['launch'] = item.xpath('./div[1]/div[2]/div[2]/p/span/text()').get().strip()
            car['engine'] = item.xpath('./div[2]/div[1]/p[2]/text()').get().strip()
            car['fuel'] = item.xpath('./div[2]/div[2]/p[2]/text()').get().strip()
            car['transmission'] = item.xpath('./div[2]/div[3]/p[2]/text()').get().strip()
            car['mileage'] = item.xpath('./div[2]/div[3]/p[2]/text()').get().strip()

            yield car