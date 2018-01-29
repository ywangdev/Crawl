# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from ToyCrawler.items import InstagramItem


class InstagramSpider(scrapy.Spider):
    """crawl instagram.com account
    format:
      owner's space: 'https://www.instagram.com/' + num_id + '/'
    """
    name = 'instagram'
    allowed_domains = ['www.instagram.com']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    custom_settings = {
        # specifies exported fields and order
        'FEED_EXPORT_FIELDS': ["name", "num_uploads", "num_fans", "num_followees", "link", "info"],
    }

    def __init__(self, id=None, *args, **kwargs):
        super(InstagramSpider, self).__init__(*args, **kwargs)
        self.user_id = id

    def start_requests(self):
        url = 'https://www.instagram.com/%s/' % self.user_id
        yield Request(url, headers=self.headers)

    def parse(self, response):
        from scrapy.shell import inspect_response
        inspect_response(response, self)

        item = InstagramItem()
        profile = response.xpath('//header[@class="_mainc"]')
        # profile = response.xpath('//div[@class="_ienqf"]')
        print "debug by yiyiwang:", profile
        item['name'] = profile.xpath(
            './/div[@class="_tb97a"]/h1[@class="_kc4z2"]/text()').extract()[0]
        item['num_uploads'] = profile.xpath(
            './/div[@class="_h9luf"]/li[1]/span/span/text()').extract()[0]
        item['num_fans'] = profile.xpath(
            './/div[@class="_h9luf"]/li[2]/span/span/text()').extract()[0]
        item['num_followees'] = profile.xpath(
            './/div[@class="_h9luf"]/li[3]/span/span/text()').extract()[0]
        item['link'] = 'https://www.instagram.com/%s/' % self.user_id
        item['info'] = profile.xpath(
            './/div[@class="_tb97a"]/h1/span/span/text()').extract()[0]
