# -*- coding: utf-8 -*-
import scrapy
from quanben.items import QuanbenItem, Biaoti, TshuJianjie, ZhangjieMing, Content
import time

class XiaoshuoSpider(scrapy.Spider):
    name = 'xiaoshuo'
    allowed_domains = ['qb5200.tw']
    start_urls = ['https://www.qb5200.tw/']

    def parse(self, response):
        item = QuanbenItem()
        # 分类
        fenlei_list = response.xpath('//div[@class="nav"]/ul/li/a')
        for i in fenlei_list:
            item['fenlei'] = i.xpath('./text()').extract_first()
            print(item['fenlei'])
            yield item
            url_list = i.xpath('./@href').extract_first()
            url = response.urljoin(url_list)
            yield scrapy.Request(
                url=url,
                callback=self.Book_data
            )

    def Book_data(self, response):

        item = Biaoti()
        book_list = response.xpath('//div[@class="l bd"]/ul/li')
        if len(book_list) > 0:
            for i in book_list:
                # 分类标题
                item['flbt'] = i.xpath('./span[1]/text()').extract_first()
                # 书名
                item['title'] = i.xpath('./span[2]/a/text()').extract_first()
                yield item
                url = response.urljoin(i.xpath('./span[2]/a/@href').extract_first())

                yield scrapy.Request(
                    url=url,
                    callback=self.Jian_data
                )
            pass
        if len(response.xpath('//div[@class="wrap rank"]/div/ul/li')) > 0:
            print(response.url,'===================================')
            shu_list = response.xpath('//div[@class="wrap rank"]/div/ul/li')
            for i in shu_list:
                #分类标题
                item['flbt'] = i.xpath('./span/text()').extract_first()
                #书名
                item['title'] = i.xpath('./a/text()').extract_first()
                yield item
                url = response.urljoin(i.xpath('./a/@href').extract_first())
                yield scrapy.Request(
                    url=url,
                    callback=self.Jian_data
                )





    def Jian_data(self, response):
        item = TshuJianjie()
        mulu = ZhangjieMing()
        # print('==============================')
        # 作者
        item['name'] = response.xpath('//div[@class="small"]/span[1]/text()').extract_first()
        # 简介
        item['jianjie'] = response.xpath('//div[@class="intro"]/text()').extract_first('').replace(' ', '').replace(
            '\n', '').replace('\u3000\u3000','')

        # 状态
        item['zhuangtai'] = response.xpath('//div[@class="small"]/span[3]/text()').extract_first()
        # 字数
        item['zishu'] = response.xpath('//div[@class="small"]/span[4]/text()').extract_first()
        # 图片
        item['image'] = response.urljoin(response.xpath('//div[@class="cover"]/img/@src').extract_first())
        # print('==============================')
        yield item
        time.sleep(4)
        # 目录名字
        mulu_list = response.xpath('//div[@class="listmain"]/dl/dd')
        for i in mulu_list:
            mulu['zhangjie'] = i.xpath('./a/text()').extract_first()
            yield mulu
            url = response.urljoin(i.xpath('./a/@href').extract_first())
            yield scrapy.Request(
                url=url,
                callback=self.Neirong
            )

    def Neirong(self, response):
        item = Content()
        item['content'] = ''.join(response.xpath('//div[@id="content"]/text()').extract()).replace(' ', '').replace(
            '\r', '').replace('\u3000\u3000', '').replace('\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0','')
        yield item
