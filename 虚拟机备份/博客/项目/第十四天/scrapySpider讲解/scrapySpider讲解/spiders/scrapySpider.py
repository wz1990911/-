# -*- coding: utf-8 -*-
import scrapy


class ScrapyspiderSpider(scrapy.Spider):
    name = 'scrapySpider'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']
    #同样是设置参数,会覆盖掉
    #setting.py文件中的参数,(优先级比settings.py药膏
    # custom_settings={
    #     'User-Agent':''
    # }

    def parse(self, response):
        pass
