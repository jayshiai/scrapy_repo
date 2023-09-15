import scrapy
from trip.items import TripItem
from scrapy_playwright.page import PageMethod

class TripspiderSpider(scrapy.Spider):
    name = "tripspider"
    allowed_domains = ["www.tripadvisor.com"]
    start_urls = [
        "https://www.tripadvisor.com/Attractions-g191-Activities-oa0-United_States.html"
    ]

    def __init__(self):
        self.counter = 1

    def parse(self, response):
        link_boxs = response.xpath('//div[@class="Vonpt _T _Z"]')
        if len(link_boxs) == 0:
            yield scrapy.Request(response.url, callback=self.parse)

        for link_box in link_boxs:
            divs = link_box.xpath("./div")
            link = divs[0].xpath("./a/@href").get()
            if len(divs) == 3:
                svgClass = divs[2].xpath("./a/div/div/div/svg/path/@class").get()
                if svgClass == "EsrqS":
                    award = "Gold"
                elif svgClass == "bpQdo":
                    award == "Green"
                else:
                    award == "NO"
            else:
                award = "NO"
            host = 'https://www.tripadvisor.com'
            yield scrapy.Request(host+link, callback=self.parse_page, meta=dict(
                playwright = True,
                playwright_include_page = True,
                award = award,
                errback=self.errback,
                playwright_page_methods =[PageMethod('wait_for_selector', 'a.UikNM')],
            ))
        
        if self.counter <= 120:
            next = (
                "https://www.tripadvisor.com/Attractions-g191-Activities-oa"
                + str(self.counter - 1)
                + "-United_States.html"
            )
            yield response.follow(next, callback=self.parse)
        
    async def parse_page(self, response):
        award = response.meta["award"]
        item = TripItem()

        item["id"] = self.counter
        self.counter += 1

        item["name"] = response.xpath('//div[@class="iSVKr"]/h1/text()').get()
        item["award"] = award
        item["section"] = (
            response.xpath('//*[@id="lithium-root"]/main/div[1]/div[1]/div/div/div')[-2]
            .xpath("./a/span/span/text()")
            .get()
        )
        item["link"] = response.url
        item["category"] = response.xpath(
            '//*[@id="lithium-root"]/main/div[1]/div[2]/div[2]/div[2]/div/div[1]/section[1]/div/div/div/div/div[1]/div[3]/div/div/div[1]/text()'
        ).get()
        links =  response.xpath('//div[@class="WoBiw Q3 K"]/a')
        item['website'] = links[0].xpath("./a/@href").get()
        item['phone'] = links[1].xpath("./a/@href").get()
        item['email'] = links[2].xpath("./a/@href").get()
        yield item

    async def errback(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()