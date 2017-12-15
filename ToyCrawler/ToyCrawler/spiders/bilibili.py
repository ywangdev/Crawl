# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from ToyCrawler.items import BilibiliItem


class BilibiliSpider(scrapy.Spider):
    """crawl bilibili.com account
    format:
      owner's space: 'https://space.bilibili.com/' + num_id + '#/'
      owner's fans: 'https://space.bilibili.com/' + num_id + '#/fans/fans'
    """
    name = 'bilibili'
    allowed_domains = ['bilibili.com']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def __init__(self, id=None, *args, **kwargs):
        super(BilibiliSpider, self).__init__(*args, **kwargs)
        self.user_id = id

    def start_requests(self):
        url = 'https://search.bilibili.com/upuser?keyword=%s' % self.user_id
        yield Request(url, headers=self.headers)

    def parse(self, response):
        item = BilibiliItem()
        limit = 3
        users = response.xpath('//div[@class="ajax-render"]/li')
        for user in users:
            limit -= 1
            if limit < 0:
                break

            item['name'] = user.xpath(
                './/div[@class="headline"]/a/@title').extract()[0]
            item['num_uploads'] = user.xpath(
                './/div[@class="up-info"]/span[1]/text()').re(ur'稿件：(.*)')[0]
            item['num_fans'] = user.xpath(
                './/div[@class="up-info"]/span[2]/text()').re(ur'粉丝：(.*)')[0]
            item['link'] = user.xpath(
                './/div[@class="up-face"]/a/@href').extract()[0]
            item['info'] = user.xpath(
                './/div[@class="desc"]/text()').extract()[0]
            yield item

        """
        next_url = response.xpath('//span[@class="next"]/a/@href').extract()
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url[0]
            yield Request(next_url, headers=self.headers)
        """
