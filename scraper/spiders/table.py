import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.support.ui import Select
from scraper.items import Team


class TableSpider(scrapy.Spider):
    name = "table"

    def start_requests(self):
        yield SeleniumRequest(
            url="https://www.gthlcanada.com/leaguestandings/",
            wait_time=10,
            callback=self.parse_teams,
        )

    def parse_teams(self, response):
        driver = response.request.meta["driver"]
        iframe = driver.find_element_by_id("iframed-stats")
        driver.switch_to.frame(iframe)
        division = Select(driver.find_element_by_id("ddlDiv"))
        division.select_by_value("MBN")
        driver.implicitly_wait(10)
        division = Select(driver.find_element_by_id("ddlCat"))
        division.select_by_value("A1")
        driver.implicitly_wait(10)

        r = scrapy.Selector(text=driver.page_source)

        for row in r.css("tbody > tr").getall():
            yield Team(
                name=row.css(".tblTeam::attr(data)").get(),
                gms_played=row.css(".tblGP::text()"),
                w_l_t=row.css(".tblWLT::text()").get(),
                points=row.css(".tblPTS::text()").get(),
                winpct=row.css(".tblPPG::text()").get(),
                gls_foravg=row.css(".tblGFA::text()").get(),
                gls_agstavg=row.css(".tblGAA::text()").get(),
                home_record=row.css(".tblHome::text()").get(),
                away_record=row.css(".tblAway::text()").get(),
                past_10=row.css(".tblP10::text()").get(),
                streak=row.css(".tblStreak::text()").get(),
            )

