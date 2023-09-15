import scrapy
from scrapy_selenium import SeleniumRequest
from medi.items import MediItem
from selenium.webdriver.common.by import By

class GovSpider(scrapy.Spider):
    name = "gov"
    allowed_domains = ["www.gov.uk"]
    def start_requests(self):
        yield SeleniumRequest(
            url ="https://www.gov.uk/drug-device-alerts?keywords=ultrasound&alert_type%5B%5D=field-safety-notices&alert_type%5B%5D=device-safety-information",
            wait_time = 3,
            callback = self.parse,
            
        )
 
    def parse(self, response):
        element = response.request.meta['driver'].find_element(By.XPATH, '//*[@id="js-results"]/div/ul')
        element.screenshot("screenshot.png")
        
        data= response.xpath('//*[@id="js-results"]/div/ul/li')
        for item in data:
            report = MediItem()
            report['title'] = item.xpath("./div/a/text()").get()
            report['description'] = item.xpath("./p/text()").get()
            yield report
