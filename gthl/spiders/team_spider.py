import scrapy
import urllib
import requests

# seasons = response.css("#ddlSeason>option::attr(value)").getall()
# self.settings.getbool("ALL_YEARS")

iframe_url = "https://ssp.agilex.ca/gthlssp/standings.aspx"


class TeamTableSpider(scrapy.Spider):
    name = "teams"

    def start_requests(self):
        headers = {
            "Referer": "https://www.gthlcanada.com/leaguestandings/",
            "Cookie": "AGILEX=Division=MBN&Category=A1&Season=19-20&Region=East",
        }

        return [
            scrapy.Request(url=iframe_url, headers=headers, callback=self.parse_iframe)
        ]

    def parse_iframe(self, response: scrapy.http.Response):
        # viewstate = response.css("#__VIEWSTATE::attr(value)").get()
        # viewstate2 = response.css("#__VIEWSTATE").get()
        # eventval = response.css("#__EVENTVALIDATION::attr(value)").get()
        
        params = {
            "ddlCat": "A1",
            "ddlDiv": "MBN",
            "ddlRegion": "East",
            "ddlSeason": "19-20",
        }
        return scrapy.FormRequest.from_response(
            response, formdata=params, callback=self.parse_rows
        )

    def parse_rows(self, response):
        """This boi will parse the team tables and make Items for each team with
        the data we care about for now only for this year """
        print("st_RepeaterBody" in response.body)

