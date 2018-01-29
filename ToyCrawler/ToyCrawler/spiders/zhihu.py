# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from ToyCrawler.items import IDItem


class ZhihuSpider(scrapy.Spider):
    """crawl zhihu.com account
    format:
      search a person: 'https://www.zhihu.com/search?q=' + id + '&type=people
      owner's space: 'https://www.zhihu.com/people/' + link_id
    """
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    custom_settings = {
        # specifies exported fields and order
        'FEED_EXPORT_FIELDS': ["name", "num_uploads", "num_answers", "num_followers", "num_followees", "image", "link", "info"],
    }

    def __init__(self, id=None, *args, **kwargs):
        super(ZhihuSpider, self).__init__(*args, **kwargs)
        self.user_id = id

    def start_requests(self):
        url = 'https://www.zhihu.com/search?q=%s&type=people' % self.user_id
        yield Request(url, headers=self.headers)

    def parse(self, response):
        item = IDItem()
        limit = 2
        for idx in range(1, limit + 1):
            user_xpath = '//*[@id="SearchMain"]/div/div/div/div[%d]/div/div' % (idx)
            item['name'] = response.xpath(user_xpath +
                '/div[2]/h2/div/span/div/div/a/span/text()').extract()[0]
            item['info'] = response.xpath(user_xpath +
                '/div[2]/div/div/div[1]/text()').extract()[0]

            line3 = user_xpath + '/div[2]/div/div/div[2]'
            item['num_answers'] = response.xpath(
                line3 + '/a[1]/text()').re(ur'(.*) 回答')[0]
            item['num_uploads'] = response.xpath(
                line3 + '/a[2]/text()').re(ur'(.*) 文章')[0]
            item['num_followers'] = response.xpath(
                line3 + '/a[3]/text()').re(ur'(.*) 关注者')[0]
            yield item
