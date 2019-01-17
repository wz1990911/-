# -*- coding: utf-8 -*-
import scrapy
from quagnben.items import QuagnbenItem


class XiaoshuoSpider(scrapy.Spider):
    name = 'xiaoshuo'
    allowed_domains = ['qb5200.tw']
    start_urls = ['https://www.qb5200.tw/']

    def parse(self, response):
        item = QuagnbenItem()
        #fenlei
        print('=========')
        fenlei_list = response.xpath('//div[@class="nav"]/ul/li/a').extract()
        print('=========')
        for i in fenlei_list:
            fenlei = i.xpath('.//text()').extract()
            print(i)










