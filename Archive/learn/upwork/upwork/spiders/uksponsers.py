import scrapy
import json
from upwork.items import UpworkItem
import re


class UksponsersSpider(scrapy.Spider):
    name = "uksponsers"

    start_urls = ["https://uktiersponsors.co.uk/"]

    # niche = ["Care Home", "Medical", "Recruitment"]

    def parse(self, response):
        yield scrapy.Request(
            url="https://uktiersponsors.co.uk/tierApi/api/tierData/Companies",
            method="POST",
            body=json.dumps(
                {
                    "PageNumber": 3,
                    "RowsPerPage": 20,
                    "Company": "",
                    "Town": "",
                    "Industry": "Care Home",
                }
            ),
            headers={"Content-Type": "application/json"},
            callback=self.after_res,
        )

    def after_res(self, response):
        for item in response.json()["companies"]:
            uksponser = UpworkItem()

            if item["website"] != "":
                yield scrapy.Request(
                    url=item["website"],
                    callback=self.parse_website,
                    meta={"uksponser": uksponser},
                )
            else:
                uksponser["email"] = ""

            uksponser["name"] = item["organisationName"]
            uksponser["website"] = item["website"]
            uksponser["social"] = item["socialWebsite"]
            uksponser["industry"] = item["industry"]
            uksponser["town"] = item["town"]
            uksponser["date"] = item["dateAdded"]
            yield uksponser

    def parse_website(self, response):
        uksponser = response.meta.get("uksponser")

        # retrieve the HTML code of the URL
        html_code = response.body.decode("utf-8")

        # use regular expression to find email addresses in the page
        emails = re.findall(
            r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", html_code
        )
        if emails:
            print("EMAIL:" + emails[0])
            uksponser["email"] = emails[0]
        else:
            uksponser["email"] = ""

        return uksponser
