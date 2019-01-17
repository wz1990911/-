# -*- coding: utf-8 -*-
import scrapy
import re,json
from shijijiayuan.items import ShijijiayuanItem
class SjjySpider(scrapy.Spider):
    name = 'sjjy'
    allowed_domains = ['jiayuan.com']
    start_urls = ['http://date.jiayuan.com/eventslist_new.php?page=1&city_id=21&shop_id=18',
                  'http://date.jiayuan.com/eventslist_new.php?page=1&city_id=31&shop_id=60'
                  ]
    #http://date.jiayuan.com/eventslist.php
    #http://date.jiayuan.com/eventslist.php


    def parse(self, response):

        list = []
        xiangqing = response.xpath('//ul[@class="review_detail fn-clear t-activiUl"]/li/a/@href')
        if len(xiangqing) > 0:
            for xq_url in xiangqing:
                list_url = 'http://date.jiayuan.com/'+xq_url.xpath('./a/@href').extract_first('')
                print(list_url)
                yield scrapy.Request(
                    list_url,
                    callback=self.xiangqing_data
                )
        # else:
        #     html = response.text
        #     data = json.loads(html)
        #     for i in data:
        #         id = i['id']
        #         url = 'http://date.jiayuan.com/activityreviewdetail.php?id=' + id
        #         list.append(url)
        #     for i in list:
        #         yield scrapy.Request(i, callback=self.xiangqing_data)
        #     pattern = re.compile('page=(\d+)')
        #     result = re.findall(pattern, response.url)[0]
        #     num = int(result) + 1
        #     url = 'http://date.jiayuan.com/eventslist_new.php?page=' + str(num) + '&city_id=11&shop_id=18'
        #     yield scrapy.Request(url, callback=self.parse)


    def xiangqing_data(self,response):
        item = ShijijiayuanItem()
        #标题
        item['title'] = response.xpath('//h1[@class="detail_title"]/text()').extract_first('')
        #时间
        item['time'] = ''.join(response.xpath('//ul[@class="detail_info"]/li[1]/text()').extract())
        #地址
        item['dz'] = response.xpath('//ul[@class="detail_info"]/li[2]/text()').extract_first('')
        #参加
        item['canjia'] = ''.join(response.xpath('//ul[@class="detail_info"]/li[3]/span[1]/text()').extract())
        #预约
        item['yuyue'] = ''.join(response.xpath('//ul[@class="detail_info"]/li[3]/span[2]/text()').extract())
        #活动介绍
        item['jieshao'] = ''.join(response.xpath('//p[@class="info_word"]/text()').extract())
        #温馨提示
        item['wxts'] = response.xpath('//div[@id="date_float"]/div[3]/div[2]/p/text()').extract_first()
        #体验店介绍
        item['tyd'] = response.xpath('//div[@id="date_float"]/div[4]/div[2]/p/text()').extract_first()
        yield item


