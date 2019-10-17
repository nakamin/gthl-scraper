BOT_NAME = "scraper"

SPIDER_MODULES = ["scraper.spiders"]
NEWSPIDER_MODULE = "scraper.spiders"

ROBOTSTXT_OBEY = True

DOWNLOADER_MIDDLEWARES = {
    "scrapy_splash.SplashCookiesMiddleware": 723,
    "scrapy_splash.SplashMiddleware": 725,
    "scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware": 810,
}

SPIDER_MIDDLEWARES = {"scrapy_splash.SplashDeduplicateArgsMiddleware": 100}

DUPEFILTER_CLASS = "scrapy_splash.SplashAwareDupeFilter"

SPLASH_URL = "http://192.168.59.103:8050"
