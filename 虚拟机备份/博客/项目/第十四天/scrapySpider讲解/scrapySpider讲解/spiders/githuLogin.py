# -*- coding: utf-8 -*-
import scrapy


class GithuloginSpider(scrapy.Spider):
    name = 'githuLogin'
    allowed_domains = ['github,com']
    start_urls = ['http://github,com/']

    def parse(self, response):
        pass
