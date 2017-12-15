# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ToycrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class BilibiliItem(scrapy.Item):
    # name
    name = scrapy.Field()
    # num_uploads
    num_uploads = scrapy.Field()
    # num_fans
    num_fans = scrapy.Field()
    # info
    info = scrapy.Field()
