import scrapy
import json
from medi.items import MediItem
class MedicineSpider(scrapy.Spider):
    name = "medicine"
    allowed_domains = ["www.keldoc.com"]
    start_urls = ["https://www.keldoc.com/"]

    def parse(self, response):
        
        i = 1;
        while i<=100:
            url = "https://www.keldoc.com/api/patients/v2/searches/geo_location?specialty_id=medecin-generaliste&raw_location=paris-75014&page="+str(i)
            i+=1
            yield scrapy.Request(url, callback=self.parse_data)

    def parse_data(self,response):
        data = json.loads(response.text)['results']
        
        for key, section in data.items():
            if len(section["data"]) !=0:
                data = section["data"]
                break
        for item in data:
            id = item["id"]
            page = "https://www.keldoc.com/api/patients/v2/staffs/"+str(id)+"/details"
            yield scrapy.Request(page, callback=self.parse_phone, meta=dict(id=id))
    
    def parse_phone(self,response):
        id = response.meta["id"]
        data = json.loads(response.text)
        item = MediItem()
        item["id"] = id
        item["phone"] = data["phone_number"].replace(" ","")
        if len(item["phone"]) >=10:
            yield item
        else:
            pass
