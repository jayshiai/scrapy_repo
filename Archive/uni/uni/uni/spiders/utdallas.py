import scrapy
from uni.items import UniItem

class UtdallasSpider(scrapy.Spider):
    name = "utdallas"
    allowed_domains = ["websvcs.utdallas.edu"]
    start_urls = ["https://websvcs.utdallas.edu/directory/includes/directories.class.php?dirType=displayname&dirSearch=&dirAffil=faculty&dirDept=All&dirMajor=All&dirSchool=All"]

    def parse(self, response):
        data = response.xpath('//div[@class="resultPage"]/div')

        for item in data:
            name = item.xpath("./h2/text()").get()
            phone = email = item.xpath('./div/div/p[1]/a/text()').get()
            email = item.xpath("./div/div/p[2]/a/text()").get()

            ps = item.xpath("./div/div/p")

            for p in ps:
                text = p.xpath('./b/text()').get()
                if 'Department' in text:
                    department = p.xpath('./text()').get().strip()
            prof = UniItem(
                name = name,
                email = email,
                phone = phone,
                department = department
            )

            yield prof
