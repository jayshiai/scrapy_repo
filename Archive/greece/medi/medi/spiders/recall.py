import scrapy
from scrapy_selenium import SeleniumRequest
from medi.items import MediItem
from selenium.webdriver.common.by import By


class RecallSpider(scrapy.Spider):
    name = "recall"
    allowed_domains = ["recalls-rappels.canada.ca"]
   
    def start_requests(self):
        yield SeleniumRequest(
            url ="https://recalls-rappels.canada.ca/en/search/site?search_api_fulltext=ultrasound",
            wait_time = 10,
            callback = self.parse,
            
        )
    async def parse(self, response):
        element = response.request.meta['driver'].find_element(By.XPATH, '//div[@class="view-content"]')
        element.screenshot("recall.png")
        data= response.xpath("//div[@class='search-result views-row']")
        for item in data:
            report = MediItem()
            report['title'] = item.xpath("./div/span/span/a/text()").get()
            report['description'] = item.xpath("./div/span/span/div").get().replace('<div class="search-excerpt-wrapper">','').replace('</div>','').replace('\n','').replace("</strong>",'').replace('<strong>','').strip()
            yield report