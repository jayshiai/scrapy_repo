import scrapy
from ucc.items import UccItem
import json
import string

class CaliforniaSpider(scrapy.Spider):
    name = "california"
    allowed_domains = ["bizfileonline.sos.ca.gov"]
    start_urls = ["https://bizfileonline.sos.ca.gov/"]

    def parse(self, response):
        url = "https://bizfileonline.sos.ca.gov/api/Records/uccsearch"
        headers={'Content-type':'application/json'}      
        prefix = "aa"
        for letter1 in string.ascii_lowercase:
            for letter2 in string.ascii_lowercase:
                print(prefix + letter1 + letter2)
        
                query= prefix + letter1 + letter2
                data = "{'SEARCH_VALUE': '"+query+"','STATUS': 'ALL','RECORD_TYPE_ID': '0','FILING_DATE': {'start': null, 'end': null},'LAPSE_DATE': {'start': null, 'end': null}}"
                yield scrapy.Request(url=url,method='POST', body=data,headers=headers,callback=self.parse_data)
    
    def parse_data(self,response):
        data = json.loads(response.text)
        data = data["rows"]
        for key, item in data.items():
            ucc = UccItem()

            ucc['name'] = item['TITLE'][0]
            ucc['type'] = item['RECORD_TYPE']
            ucc['file_number'] = item['RECORD_NUM']
            ucc['secured_party_info'] = item['SEC_PARTY'][0]
            ucc['status'] = item['STATUS']
            ucc['filling_date'] = item['FILING_DATE']
            ucc['lapse_date'] = item['LAPSE_DATE']

            yield ucc