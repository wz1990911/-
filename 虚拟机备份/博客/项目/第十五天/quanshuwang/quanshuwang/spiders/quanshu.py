# -*- coding: utf-8 -*-
import scrapy
import re
from quanshuwang.items import QuanshuwangItem
class QuanshuSpider(scrapy.Spider):
    name = 'quanshu'
    allowed_domains = ['quanshuwang.com']
    start_urls = ['http://www.quanshuwang.com/']

    def parse(self, response):
        # 分类
        jianjie_url = response.css('ul.channel-nav-list li a::attr(href)').extract()
        if len(jianjie_url) > 0:
            for list_url in jianjie_url:
                yield scrapy.Request(
                    list_url,
                    callback=self.xiangxi
                )
    def xiangxi(self,response):
        # 简介url
        xiangxi_url = response.css('ul.seeWell.cf li > a ::attr(href)').extract()
        # print(xiangxi_url)
        if len(xiangxi_url) > 0:
            for list_url in xiangxi_url:
                yield scrapy.Request(
                    list_url,
                    callback=self.jieshao
                )
    def jieshao(self,response):
        item = QuanshuwangItem()
        id_url = re.compile('.*?//.*?/.*?(\d+).html')
        # id
        item['id'] = re.findall(id_url,response.url)[0]
        #分类
        item['fenlei'] = response.css('a.c009900 ::text').extract_first('')
        #名字
        item['name'] = response.css('div.b-info h1::text').extract()
        #简介
        item['jianjie'] = ''.join(response.css('div.infoDetail > div ::text').extract()).replace('\n','')
        url = response.css('div.b-oper > a ::attr(href)').extract_first()
        # print(url)
        # yield item
        yield scrapy.Request(
            url,
            callback=self.content
        )
    def content(self,response):
        content_url = response.css('div.clearfix.dirconone li a::attr(href)').extract()
        if len(content_url)>0:
            for i in content_url:
                yield scrapy.Request(
                    url=i,
                    callback=self.neirong
                )


    def neirong(self,response):
        name = response.css('div.main-index a.article_title ::text').extract()
        zhangjie = response.css('strong.l.jieqi_title ::text').extract_first()
        neirong = ''.join(response.css('div.mainContenr ::text').extract()).replace(' ','').replace('\r','').replace('\n','')
        print(neirong)


