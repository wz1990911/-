# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
from quan.items import QuanItem,Quancontent

class QswSpider(CrawlSpider):
    name = 'qsw'
    allowed_domains = ['quanshuwang.com']
    start_urls = ['http://www.quanshuwang.com/']
#http://www.quanshuwang.com/book/47/47670
    # http: // www.quanshuwang.com / book_154780.html
    #http://www.quanshuwang.com/book/47/47670/16135082.html
    rules = (
        Rule(LinkExtractor(allow=r'.*?/list/\d+.*?\d+.*?html'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'.*?/book_\d+.html'), callback='jianjie', follow=True),
        # Rule(LinkExtractor(allow=r'.*?/book/\d+/\d+',restrict_xpaths='//a[@class="reader"]'), callback='mulu', follow=True),
        Rule(LinkExtractor(allow=r'.*?/book/\d+/\d+/\d+.html'),callback='mulu',follow=True)
    )

    def parse_item(self, response):
       print('爬虫开始')

    def jianjie(self, response):
        # print(response.url,'=======')
        item = QuanItem()
        id_url = re.compile('.*?//.*?/.*?(\d+).html')
        # id
        item['id'] = re.findall(id_url, response.url)[0]
        # 分类
        item['fenlei'] = response.css('a.c009900 ::text').extract_first('')
        # 名字
        item['name'] = response.css('div.b-info h1::text').extract()
        # 简介
        item['jianjie'] = ''.join(response.css('div.infoDetail > div ::text').extract()).replace('\n', '').replace('\xa0','')
        yield item
    def mulu(self, response):
        item = Quancontent()
        item['title'] = response.css('div.main-index a.article_title ::text').extract()
        item['zhangjie'] = response.css('strong.l.jieqi_title ::text').extract_first()
        item['neirong'] = ''.join(response.css('div.mainContenr ::text').extract()).replace(' ', '').replace('\r', '').replace('\n', '').replace('\xa0','')
        yield item