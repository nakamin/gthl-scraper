import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.support.ui import Select


class TableSpider(scrapy.Spider):
    name = "table"

    def start_requests(self):
        yield SeleniumRequest(
            url="https://www.gthlcanada.com/leaguestandings/",
            wait_time=10,
            callback=self.get_table,
        )

    def get_table(self, response):
        driver = response.request.meta["driver"]
        iframe = driver.find_element_by_id("iframed-stats")
        driver.switch_to.frame(iframe)
        division = Select(driver.find_element_by_id("ddlDiv"))
        division.select_by_value("MBN")
        driver.implicitly_wait(5)
        division = Select(driver.find_element_by_id("ddlCat"))
        division.select_by_value("A1")
        driver.implicitly_wait(10)
