BOT_NAME = "scraper"

SPIDER_MODULES = ["scraper.spiders"]
NEWSPIDER_MODULE = "scraper.spiders"

ROBOTSTXT_OBEY = False

SELENIUM_DRIVER_NAME = "chrome"
SELENIUM_DRIVER_EXECUTABLE_PATH = (
    "C:\\Users\\AntonKaminsky\\Documents\\projects\\gthl-scraper\\bin\\chromedriver.exe"
)
SELENIUM_DRIVER_ARGUMENTS = ['--headless']

DOWNLOADER_MIDDLEWARES = {
    'scrapy_selenium.SeleniumMiddleware': 800
}

ITEM_PIPELINES = {
    'scraper.pipelines.FirestoreWriterPipeline': 800,
}
