import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from scraper.items import Team


class TableSpider(scrapy.Spider):
    name = "table"

    def start_requests(self):
        yield SeleniumRequest(
            url="https://www.gthlcanada.com/leaguestandings/",
            wait_time=20,
            callback=self.parse_teams,
        )

    def parse_teams(self, response):
        driver = response.request.meta["driver"]
        iframe = driver.find_element_by_id("iframed-stats")
        driver.switch_to.frame(iframe)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "st_tblRepeater")))
        division = Select(driver.find_element_by_id("ddlDiv"))
        division.select_by_value("MBN")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "st_tblRepeater")))
        category = Select(driver.find_element_by_id("ddlCat"))
        category.select_by_value("A1")
        driver.implicitly_wait(10)

        r = scrapy.Selector(text=driver.page_source)

        for row in r.css("tbody > tr"):
            yield Team(
                name=row.css(".tblTeam::attr(data)").get(),
                gms_played=row.css(".tblGP::text").get(),
                w_l_t=row.css(".tblWLT::text").get(),
                points=row.css(".tblPTS::text").get(),
                winpct=row.css(".tblPPG::text").get(),
                gls_foravg=row.css(".tblGFA::text").get(),
                gls_agstavg=row.css(".tblGAA::text").get(),
                home_record=row.css(".tblHome::text").get(),
                away_record=row.css(".tblAway::text").get(),
                past_10=row.css(".tblP10::text").get(),
                streak=row.css(".tblStreak::text").get(),
            )
