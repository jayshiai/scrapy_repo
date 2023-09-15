import scrapy
import json

class FaqsSpider(scrapy.Spider):
    name = "faqs"
    allowed_domains = ["www.catho.com.br"]
    

    def parse(self, response):
        url = "https://www.catho.com.br/ajuda/graphql"
        payload = {"operationName":None,"variables":{"categoryNamespace":"Candidatos","categorySlug":"alteracao-de-curriculo","limit":10,"start":0},"query":"query ($categoryNamespace: String!, $categorySlug: String!, $limit: Int!, $start: Int!) {\n  category: helpCategories(limit: 1, where: {namespace: $categoryNamespace, slug: $categorySlug}) {\n    ...GetCategory\n    questions(limit: $limit, start: $start) {\n      ...GetQuestion\n      __typename\n    }\n    __typename\n  }\n  totalQuestions: questionsCountByCategorySlug(slug: $categorySlug)\n}\n\nfragment GetQuestion on HelpQuestions {\n  id\n  name\n  slug\n  resume\n  description\n  __typename\n}\n\nfragment GetCategory on HelpCategories {\n  id\n  namespace\n  slug\n  name\n  title\n  description\n  __typename\n}\n"}
        yield scrapy.Request(url=url,callback=self.parse_faqs,body=payload,method='POST', headers={'Content-Type':'application/json'})

    def parse_faqs(self,response):
        print(response.content)