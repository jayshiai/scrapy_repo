import scrapy
import json
from realtors.items import RealtorsItem

class RealestateSpider(scrapy.Spider):
    name = "realestate"
    allowed_domains = ["www.top100realestateagents.com"]
    start_urls = ["https://www.top100realestateagents.com/"]


    def parse(self, response):
        with open('data.json') as f:
            data = json.load(f)
        data = data['listings']
        
        for item in data:
            link = item['permalink']
            yield response.follow(link, callback=self.parse_data, meta={'item':item})
    
    def parse_data(self, response):
        item = response.meta["item"]
        mail = response.xpath("//div[@class='listing-email']/a/@href").get().split(":")[1]
        try:
            site = item["json_ld"]["mainEntityOfPage"]["@id"]
        except:
            site=""

        agent = RealtorsItem(
            name = item["title"],
            phone = item["telephone"],
            email = mail,
            website = site,
            company = item["company_name"],
            address= item["json_ld"]["itemReviewed"]["address"]["streetAddress"],
            city = item["json_ld"]["itemReviewed"]["address"]["addressLocality"],
            state = item["json_ld"]["itemReviewed"]["address"]["addressRegion"],
            pincode = item['location']['raw'][-5:]
        )

        yield agent

