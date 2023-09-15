import scrapy
from cars.items import CarsItem

class CarspiderSpider(scrapy.Spider):
    name = "carspider"
    allowed_domains = ["www.carshop.co.uk"]
    start_urls = ["https://www.carshop.co.uk/vehicle/resultsAjax?byFinance=false&byPrice=true&excludeReserved=true&maxResults=500&offset=0&sortBy=PRICE_ASC"]
    def __init__(self):
        self.counter = 0
    def parse(self, response):
        for item in response.json()["vehicles"]:
            car = CarsItem()
            
            car["make"] = item["bodyStyle"]["make"]
            car["model"] = item["bodyStyle"]["model"]
            car["price"] = item["vehiclePrice"]["salePrice"]
            car["age"] = item["ageInYears"]
            car["milage"] = item["mileage"]
            car["colour"] = item["displayColour"]
            car["fuel"] = item["fuel"]
            car["transmission"] = item["transmission"]
            car["body"] = item["displayBodyStyle"]
            car["location"] = item["storeName"]

            yield car
        if(self.counter!=6500):
            self.counter +=500
            url = "https://www.carshop.co.uk/vehicle/resultsAjax?byFinance=false&byPrice=true&excludeReserved=true&maxResults=500&offset="+str(self.counter)+"&sortBy=PRICE_ASC"
            yield response.follow(url, self.parse)