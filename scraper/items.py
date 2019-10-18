# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Team(scrapy.Item):
    name = scrapy.Field()
    gms_played = scrapy.Field()
    w_l_t = scrapy.Field()
    points = scrapy.Field()
    winpct = scrapy.Field()
    gls_foravg = scrapy.Field()
    gls_agstavg = scrapy.Field()
    home_record = scrapy.Field()
    away_record = scrapy.Field()
    past_10 = scrapy.Field()
    streak = scrapy.Field()
