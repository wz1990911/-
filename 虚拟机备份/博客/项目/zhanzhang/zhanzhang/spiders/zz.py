# -*- coding: utf-8 -*-
import scrapy
from zhanzhang.items import ZhanzhangItem,Zhanzhang_data

class ZzSpider(scrapy.Spider):
    name = 'zz'
    allowed_domains = ['chinaz.com']
    start_urls = ['http://top.chinaz.com/']

    def parse(self, response):


        list_url = response.xpath('//div[@class="MainWebClass clearfix"]/dl/dd/a')
        for xian_data_url in list_url:
            items = ZhanzhangItem()
            href = xian_data_url.xpath('./@href').extract_first('')
            items['fenleiname']= xian_data_url.xpath('./text()').extract_first('')


            items['fenleiurl']= response.urljoin(href)

            yield items

            yield scrapy.Request(
                url = items['fenleiurl'],
                callback= self.list_data
            )
    def list_data(self,response):
        print('==============',response.url)
        xiangxi_data = response.xpath('//ul[@class="listCentent"]/li')
        for data in xiangxi_data:
            items = Zhanzhang_data()
            #标题
            items['title'] = data.xpath('.//div[@class="CentTxt"]/h3/a/@title').extract_first('')
            # 周排名
            items['ranking'] = data.xpath('.//div[@class="RtCPart clearfix"]/p[1]/a/text()').extract_first('')
            # 反链数
            items['fanlain'] = data.xpath('.//div[@class="RtCPart clearfix"]/p[last()]/a/text()').extract_first('')
            # 总排名
            items['orders'] = data.xpath('.//div[@class="RtCRateCent"]/strong/text()').extract_first('')
            # 简介
            items['content'] = data.xpath('./div[@class="CentTxt"]/p/text()').extract_first('')
            # 图片
            items['images'] = data.xpath('./div[@class="leftImg"]/a/img/@src').extract_first('')
            yield items
