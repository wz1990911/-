# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from woaiwojia.items import WoaiwojiaItem,WoaiwojiaContentItem
from scrapy_redis.spiders import RedisCrawlSpider

class WawjSpider(RedisCrawlSpider):
    name = 'wawj'
    #北京https://bj.5i5j.com/?wscckey=7c2d91635cd4fa01_1544246180

    allowed_domains = ['5i5j.com']
    # start_urls = ['https://ty.5i5j.com']
    redis_key = 'wawj:start_urls'
    # https://bj.5i5j.com/ershoufang/
    rules = (

        Rule(LinkExtractor(
            allow=r'https://.*?5i5j.*?',
            restrict_xpaths='//div[@class="top-city-menu clear"]/ul[1]/li'),
            callback='parse_item',
            follow=True),
        #列表页请求
        Rule(LinkExtractor(
            allow=r'https://.*?5i5j.*?',
            restrict_xpaths='//ul[@class="top-nav"]/li'),
            # callback='list_url',
            follow=True),
        #下一页请求
        Rule(LinkExtractor(
            allow=r'https://.*?5i5j.*?',
            restrict_xpaths='//div[@class="pageSty rf"]/a'),
            callback='list_url',
            follow=True),
        #房子详情
        Rule(LinkExtractor(
            allow=r'.*?/.*?/\d+',
            restrict_xpaths='//ul[@class="pList"]/li'),
            callback='fang_data_pz',
            follow=True),

    )

    def parse_item(self, response):
        pass
    def list_url(self,response):
        if response.status < 400:
            jiainjie = response.xpath('//ul[@class="pList"]/li/div[1]/a')
            if len(jiainjie) > 0:
                #房子信息
                data = response.xpath('//ul[@class="pList"]/li')
                item = WoaiwojiaItem()
                for list_data in data:
                    if len(list_data.xpath('.//div[@class="listTag"]/span/text()').extract()) > 0:
                        #标题
                        item['title'] = list_data.xpath('.//div[@class="listCon"]/h3/a/text()').extract_first('')
                        #空间
                        item['kongjian'] = list_data.xpath('.//div[@class="listX"]/p[1]/text()').extract_first('')
                        #地址
                        item['address'] = list_data.xpath('.//div[@class="listX"]/p[2]/a/text()').extract_first('')
                        #发布时间和状况
                        item['time_data'] = list_data.xpath('.//div[@class="listX"]/p[3]/text()').extract_first('')
                        #看房时间
                        item['room_time'] = ','.join(list_data.xpath('.//div[@class="listTag"]/span/text()').extract())
                        #将数据返回给管道
                        yield item
                # print('下一页','=========================================')
                # if len(response.xpath('//div[@class="pageSty rf"]/a[1]/@href').extract_first('')) > 0 :
                #     url = 'https://ty.5i5j.com' + response.xpath('//div[@class="pageSty rf"]/a[1]/@href').extract_first('')
                #     print(url)
                #     yield scrapy.Request(url,callback=self.list_url)

    def fang_data_pz(self,response):
        if response.status < 400:
            item = WoaiwojiaContentItem()
            # 标题
            item['title'] = response.xpath('//h1[@class="house-tit"]/text()').extract_first('')
            if len(response.xpath('//div[@class="infocon fl"]/ul/li/label/text()')) > 0:
                fy_data = response.xpath('//div[@class="infocon fl"]/ul/li')
                xinxi = []
                for i in fy_data:
                    name = ''.join(i.xpath('./label/text()').extract())
                    value = ''.join(i.xpath('./span/text()').extract())
                    xinxi.append(name+':'+value)
                # 房源信息
                item['fyxinxi'] = ''.join(xinxi)

            elif len(response.xpath('//ul[@class="fysty"]/li')) > 0:

                #房源信息
                item['fyxinxi'] = ''.join(response.xpath('//ul[@class="fysty"]/li/text()').extract())

            tese = response.xpath('//ul[@class="fytese"]/li')
            ts = []
            for i in tese:
                name = ''.join(i.xpath('./span/text()').extract())
                value = ''.join(i.xpath('./label/text()').extract())
                ts.append(name + ':' + value)
            # 房源特色
            item['fytese'] = ''.join(ts)
            # 房源图片
            images = response.xpath('//ul[@class="listimg"]/li')
            for i in images:
                item['fyimage'] = i.xpath('./a/@href').extract_first('')

            # 小区介绍
            xq = []
            jieshao = response.xpath('//div[@class="infomain fl"]/ul/li')

            for i in jieshao:
                if len(i.xpath('./span/text()').extract()) > 0:
                    name = ''.join(i.xpath('./span/text()').extract())
                    value = ''.join(i.xpath('./text()').extract())
                    xq.append(name + ':' + value)
                item['xq_jieshao'] = ' '.join(xq)
            if len(item) > 3:
                yield item









