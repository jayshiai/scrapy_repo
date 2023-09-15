import scrapy
from scrapy_selenium import SeleniumRequest
from medi.items import MediItem
from selenium.webdriver.common.by import By

class BfarmSpider(scrapy.Spider):
    name = "bfarm"
    allowed_domains = ["www.bfarm.de"]
    

    def start_requests(self):
        yield SeleniumRequest(
            url ="https://www.bfarm.de/SiteGlobals/Forms/Suche/EN/Expertensuche_Formular.html?templateQueryString=ultrasound",
            wait_time = 10,
            callback = self.parse,
            
        )
    async def parse(self, response):
        element = response.request.meta['driver'].find_element(By.XPATH, '//*[@class="l-teaser-list"]')
        element.screenshot("bfarm.png")
        data= response.xpath('//*[@class="l-teaser-list"]/div')

        for item in data:
            report = MediItem()
            report['title'] = item.xpath("./div/h3/a/span/text()").get().replace("\n","").strip()
            report['description'] = item.xpath("./div/p/span/text()").get().replace("\n","").strip()
            yield report