import scrapy
import json
from czech.items import CzechItem
class CastrolSpider(scrapy.Spider):
    name = "castrol"
    allowed_domains = ["www.castrol.com"]
    start_urls = ["https://www.castrol.com/castrol-global-oil-selector-maps/api/oil-selector-data-api/api/v1/data/locations?page=1&perPage=242&openingHourFrom=06%3A00&openingHourTo=23%3A59&distanceInMiles=99&currentLatitude=47.162494&currentLongitude=19.503304&sortBy=distanceInMiles&sortDirection=asc&countryIds=100"]

    def parse(self, response):
        data = json.loads(response.text)

        data = data['items']

        for item in data:
            shop = CzechItem()

            shop['name'] = item['name'].strip()
            shop['street'] = item['address']['line1'].strip()
            shop['city'] = item['address']['townOrCity'].strip()
            shop['zip'] = item['address']['postCode'].strip()
            try:
                shop['phone'] = item["telephone"].strip()
            except:
                shop['phone'] = ""
            try:
                shop['email'] = item['email'].strip()
            except:
                shop['email'] = ""
            
            shop['type'] = item["locationTypes"][0]['name'].strip()

            try:
                shop['Mon'] = item["openingHours"][0]["open"] + " - " + item["openingHours"][0]["close"]
                shop['Tue'] = item["openingHours"][1]["open"] + " - " + item["openingHours"][1]["close"]
                shop['Wed'] = item["openingHours"][2]["open"] + " - " + item["openingHours"][2]["close"]
                shop['Thu'] = item["openingHours"][3]["open"] + " - " + item["openingHours"][3]["close"]
                shop['Fri'] = item["openingHours"][4]["open"] + " - " + item["openingHours"][4]["close"]
                shop['Sat'] = item["openingHours"][5]["open"] + " - " + item["openingHours"][5]["close"]
            except:
                shop['Mon'] = ""
                shop['Tue'] = ""
                shop['Wed'] = ""
                shop['Thu'] = ""
                shop['Fri'] = ""
                shop['Sat'] = ""

            yield shop
