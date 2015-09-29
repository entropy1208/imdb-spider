# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()

class imdbItem(scrapy.Item):
    title = scrapy.Field()
    year = scrapy.Field()
    rating = scrapy.Field()
    runtime = scrapy.Field()
    genres = scrapy.Field()
    metascore = scrapy.Field()
    director = scrapy.Field()
    stars = scrapy.Field()
    desc = scrapy.Field()
     
