import scrapy
from scrapy.http import FormRequest

class JobsSpider(scrapy.Spider):
    name = "jobs"
    allowed_domains = ["careerbuilder.vn"]
    

    def parse(self, response):
        i = 1;
        formData = {
            'dataOne': 'a:1:{s:4:"PAGE";s:1:"2";}',
            'dataTwo' : 'a:0:{}}'
        }
        
        yield FormRequest(url='https://careerbuilder.vn/search-jobs', formdata=formData, callback=self.parse_jobs)

    def parse_jobs(self,response):
        print(response) 