# -*- coding: utf-8 -*-
import scrapy


class XiaoshuoSpider(scrapy.Spider):
    name = 'xiaoshuo'
    allowed_domains = ['17k.com']
    start_urls = ['http://www.17k.com/quanben/']

    def parse(self, response):
        url_list = response.xpath('//dl[@class="BZZD_TOP"]//dd/ul/li')
        for i in url_list:
            url = i.xpath('.//a/@href').extract_first()
            yield scrapy.Request(
                url=url,
                callback= self.mingcheng
            )



    def mingcheng(self,response):

        print(response.url)
        #书名
        title = response.xpath('//div[@class="BookInfo"]/div[2]/h1/a/text()').extract_first()
        #分类
        a = []
        biaoqian = response.xpath('//div[@class="label"]/a')
        for i in biaoqian:
            fenlei1 = i.xpath('./@title').extract_first()
            a.append(fenlei1)
        fenlei = ','.join(a)


        #简介
        jianjie =''.join(response.xpath('//dl[@class="Tab"]/dd/div[1]/a/text()').extract()).replace('\u3000','')
        #封面图片
        img = response.xpath('//div[@id="bookCover"]/a/img/@src').extract_first()

        url_list = response.xpath('//dl[@class="Bar"]/dt/a/@href').extract_first()

        yield scrapy.Request(
            url=url_list,
            callback=self.mulu
        )

    def mulu(self,response):
        url = response.xpath('//dl[@class="Volume"]/dd/a/@href').extract_first()
        # yield scrapy.Request(
        #     url=url,
        #     callback=self.mulu
        # )
        #



