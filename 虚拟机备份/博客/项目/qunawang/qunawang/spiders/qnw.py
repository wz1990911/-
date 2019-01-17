# -*- coding: utf-8 -*-
import scrapy
from qunawang.items import QunawangItem
import re,json
from scrapy.selector import Selector
from pymongo import MongoClient

class QnwSpider(scrapy.Spider):
    name = 'qnw'
    allowed_domains = ['qunar.com']
    #让url循环请求
    start_urls = [
        'https://tuan.qunar.com/vc/index.php?category=all_r&limit=0%2C30',
        'https://tuan.qunar.com/vc/index.php?category=all_i&limit=0%2C30',
        'https://tuan.qunar.com/vc/index.php?category=all_o&limit=0%2C30',
    ]

    def parse(self, response):
        fenlei = ''
        # 判断分类
        if response.url.find('all_r') > 0:
            print('周边游')
            fenlei = '周边游'
        elif response.url.find('all_i') > 0:
            print('国内游')
            fenlei = '国内游'
        elif response.url.find('all_o') > 0:
            print('境外游')
            fenlei = '境外游'


        pattern = re.compile('<script>pageLoader\(({"id":"tuan-list".*?)\);</script>',re.S)
        json_str = re.findall(pattern, response.text)[0]
        html_str = json.loads(json_str)['html']
        select_obj = Selector(text=html_str)
        #获取详情页面的url
        details_li_url = select_obj.xpath('//div[@id="list"]/ul/li/a[1]/@href').extract()
        for i in details_li_url:
            xiangqing_url = 'https:'+ i

            yield scrapy.Request(
                url= xiangqing_url,
                meta={'fenlei':fenlei},
                callback = self.parse_data_url
            )
    def parse_data_url(self,response):
        fenlei = response.meta['fenlei']
        #匹配详情的url
        xiangqing_url = 'https:' + response.xpath('.').re("location.href = '(.*?)'")[0]
        yield scrapy.Request(
            url=xiangqing_url,
            meta={'fenlei':fenlei},
            callback=self.content_data
        )
    def content_data(self,response):
        item = QunawangItem()
        #标题
        item['wz_title']=''.join(response.css('div.summary h1::text').extract()).replace(' ','').replace('\n','')
        #图片链接
        item['wz_image'] = response.xpath('//div[@class="hotlist"]/ul/li/a/img/@src').extract()
        #介绍
        item['wz_jieshao'] = response.xpath('//span[@class="feature-value"]/text()').extract()
        #价格
        item['wz_price'] = response.xpath('//span[@class="number"]/var/text()').extract()
        #产品编号
        item['wz_bianhao'] = response.xpath('//div[@class="order"]/ul/li[1]/span/text()').extract_first()
        #行程套餐
        item['wz_taocan'] = response.xpath('//div[@class="order"]/ul/li[2]/span/em/text()').extract()

        pattern = re.compile(
            '.*?"choosen":"(\d+)"'
        )
        choosen = re.findall(pattern, response.text)[0]
        pattern = re.compile(
            '(https.*?com)/.*?id=(\d+).*?', re.S
        )
        add_url_result = re.findall(pattern, response.url)
        js_result_url = add_url_result[0][0] + '/user/detail/getStatistics.json?pId=' + add_url_result[0][1]

        choosen_url = add_url_result[0][0] + '/user/detail/getDetail.json?pId=' + add_url_result[0][1] + '&isVer=false&oid=&tuId=&tId' + str(choosen) + '&takeoffDate=2018-12-14'

        yield scrapy.Request(
            url=js_result_url,
            meta={'item': item, 'choosen_url': choosen_url},
            callback=self.js_data_cp
        )
    def js_data_cp(self,response):
        item = response.meta['item']
        choosen_url = response.meta['choosen_url']
        cp = json.loads(response.text)
        #历史成交
        item['wz_chengjiao'] = cp['data']['soldCountHistory']
        # 评论量
        item['wz_pinglun'] = cp['data']['totalRatings']

        yield scrapy.Request(
            url=choosen_url,
            meta={'item': item},
            callback=self.xingcheng_data
        )

    def xingcheng_data(self, response):
        item = response.meta['item']
        choosen_url = response.meta['choosen_url']

        pattern = re.compile(
            '[^\x00-\xff]', re.S
        )
        js_data = json.loads(response.text)
        # 行程包含
        item['wz_baohan'] = ''.join(re.findall(pattern, js_data['data']['feeInfo']['costIncludeDesc']))
        # 儿童政策
        item['wz_et_zhengce'] = ''.join(re.findall(pattern, js_data['data']['feeInfo']['childDetail']))
        # 老人政策
        item['wz_lr_zhengce'] = ''.join(re.findall(pattern, js_data['data']['feeInfo']['elderDetail']))
        # 行程不含
        item['wz_buhan'] = ''.join(re.findall(pattern, js_data['data']['feeInfo']['costExcludeDesc']))
        yield scrapy.Request(
            url=choosen_url,
            meta={'item': item},
            callback=self.chucun
        )
    def chucun(self,response):
        item = response.meta['item']
        try:
            client = MongoClient(host='localhost', port=27017)
            db = client.dangdang
            db.stu.insert_one(item)
            print(item['wz_title'] + '写入成功')
        except:
            print(item['wz_title'] + '写入失败')








