BOT_NAME = "scraper"

SPIDER_MODULES = ["scraper.spiders"]
NEWSPIDER_MODULE = "scraper.spiders"

ROBOTSTXT_OBEY = False

SELENIUM_DRIVER_NAME = "chrome"
SELENIUM_DRIVER_EXECUTABLE_PATH = 'chromedriver'
SELENIUM_DRIVER_ARGUMENTS = ['--headless', '--no-sandbox']

DOWNLOADER_MIDDLEWARES = {
    'scrapy_selenium.SeleniumMiddleware': 800
}

ITEM_PIPELINES = {
    'scraper.pipelines.FirestoreWriterPipeline': 800,
}

