import scrapy, scrapy_splash
import requests


class TableSpider(scrapy.Spider):
    name = "table"

    def start_requests(self):
        yield scrapy_splash.SplashRequest(
            "https://gthlcanada.com/leaguestandings/", callback=self.get_table
        )

    def get_table(self, response):
        yield scrapy_splash.SplashFormRequest.from_response(
            response,
            url="https://ssp.agilex.ca/gthlssp/standings.aspx",
            formdata={
                "ddlCat": "A1",
                "ddlDiv": "MBN",
                "ddlRegion": "East",
                "ddlSeason": "19-20",
            },
            callback=self.parse,
        )

    def parse(self, response):
        print("st_RepeaterBody" in response.body)
