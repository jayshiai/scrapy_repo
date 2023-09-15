import scrapy
from hoogscraper.items import HoogscraperItem

class HoogSpider(scrapy.Spider):
    name = "hoog"
    
    start_urls = ["https://www.hoog.design"]

    def parse(self, response):
        
        i = 1
        while(i<=24):
            url = "https://www.hoog.design/en/com/architects/page/"+str(i)
            i+=1
            yield scrapy.Request(url,callback=self.parse_links)
            
            
    def parse_links(self,response):
        data = response.xpath('//*[@class="btn btn-link mb-4"]/@href')
        for item in data:
                link = item.get()
                yield response.follow(link,callback=self.parse_data)

    def parse_data(self,response):
        details = HoogscraperItem()
        contact = response.xpath('//*[@class="company-contact-buttons"]/a')
        details['name'] = response.xpath('//*[@id="single-company"]/div/div/div[1]/h1/text()').get()
        try:
            details['website'] =  contact[0].xpath('./@href').get().split("?utm_source")[0].strip()
        except:
            details['website'] = ""
        try:
            details['phone'] = contact[1].xpath('./@href').get().split(":")[1].strip()
        except:
            details['phone'] = ""

        yield response.follow(details['website'], callback=self.parse_page, meta= dict(
            details = details
        ))
    
    def parse_page(self,response):
        details = response.meta['details']

        
        mails = response.css('[href^="mailto:"]').xpath('./@href').get()
        

        if mails!=None:
            details['email'] = mails.strip().split(":")[1]
        else:
            try:
                contact = response.xpath('//a[contains(@href, "contact")]/@href').get()
                yield response.follow(contact, callback=self.parse_contact,meta=dict(
                    details = details
                ))
            except:
                yield details
            
        
    def parse_contact(self,response):
        details = response.meta['details']

        
        mails = response.css('[href^="mailto:"]').xpath('./@href').get()
        
        if mails!=None:
            details['email'] = mails.strip().split(":")[1]

        yield  details