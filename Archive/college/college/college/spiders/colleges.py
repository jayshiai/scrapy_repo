import scrapy
from college.items import CollegeItem

class CollegesSpider(scrapy.Spider):
    name = "colleges"
    allowed_domains = ["www.collegesimply.com"]
    start_urls = ['https://www.collegesimply.com/colleges/rank/colleges/lowest-graduation-rate/?page=1']

    def parse(self, response):
        i=1;
        while(i<=177):
            url = "https://www.collegesimply.com/colleges/rank/colleges/lowest-graduation-rate/?page="+str(i)
            
            i+=1
            yield scrapy.Request(url,callback=self.parse_page)
    
    def parse_page(self,response):
       
        data = response.xpath('//tr[@itemprop="itemListElement"]')
        print(data)
        for item in data:
            college = CollegeItem()
            college['name'] = item.xpath('./td[2]/h6/a/text()').get().strip()
            link = item.xpath('./td[2]/h6/a/@href').get()
            address = item.xpath('./td[2]/p/text()').get()
            address = address.split(',')
            college['city'] = address[0].strip()
            college['state'] = address[1].strip()
            college['rate'] = item.xpath('./td[3]/text()').get().replace('\n','')

            yield response.follow(link,callback=self.parse_enroll,meta=dict(
                college=college
            ))
    
    def parse_enroll(self,response):
        college = response.meta['college']

        college['enroll']= int(response.xpath('//*[@class="card-body"]/div[@class="row"]/div[@class="col"]/div[@class="h2 mb-4"]/text()').get().replace('\n','').replace(",",''))

        yield college