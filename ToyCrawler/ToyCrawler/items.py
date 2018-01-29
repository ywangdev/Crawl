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

class IDItem(scrapy.Item):
    # name
    name = scrapy.Field()
    # num uploads/posts
    num_uploads = scrapy.Field()
    # num answers (e.g. zhihu)
    num_answers = scrapy.Field()
    # num followers
    num_followers = scrapy.Field()
    # num followees
    num_followees = scrapy.Field()
    # image
    image = scrapy.Field()
    # link to personal page
    link = scrapy.Field()
    # info; description
    info = scrapy.Field()

class InstagramItem(scrapy.Item):
    # name
    name = scrapy.Field()
    # num uploads/posts
    num_uploads = scrapy.Field()
    # num fans/followers
    num_fans = scrapy.Field()
    # num followees
    num_followees = scrapy.Field()
    # link
    link = scrapy.Field()
    # info
    info = scrapy.Field()
