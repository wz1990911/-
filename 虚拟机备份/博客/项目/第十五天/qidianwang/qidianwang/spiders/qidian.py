# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from qidianwang.items import QidianwangNovalItem,QidianwangContentItem
from  scrapy_redis.spiders import RedisCrawlSpider
class QidianSpider(RedisCrawlSpider):
    name = 'qidian'
    allowed_domains = ['qidian.com']
    # start_urls = ['https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=1']
    redis_key = ''
    #https://www.qidian.com/all
    #//read.qidian.com/chapter/_AaqI-dPJJ4uTkiRw_sFYA2/-doT6biEpYlOBDFlr9quQA2
    rules = (
        Rule(LinkExtractor(
            allow=r'.*?page=\d+',restrict_xpaths='//ul[@class="lbf-pagination-item-list"]'),
            callback='parse_item',
            follow=True,
        ),
        #//book.qidian.com/info/1010734492详情url地址
        Rule(
            LinkExtractor(allow=r'.*?/info/\d+',restrict_xpaths='//div[@class="book-mid-info"]'),
            callback='parse_noval_detail',
            follow=True,
            process_links='check_noval_lin'
        ),
        #免费
        # //read.qidian.com/chapter/_AaqI-dPJJ4uTkiRw_sFYA2/-doT6biEpYlOBDFlr9quQA2#
        #收费
        # //vipreader.qidian.com/chapter/1004608738/346953260
        Rule(
            LinkExtractor(allow='//read.qidian.com/chapter/.*?',restrict_xpaths='//div[@class="volume"]'),
            callback='parse_chparter_detail',
            follow=True,
        )

    )
    def parse_start_url(self, response):
        '''
        起始url请求完成后回调方法
        :param response:
        :return:
        '''
        pass
    def parse_item(self, response):
        '''
        找到小说列表提取小说内容
        :param response:
        :return:
        '''
        noval_list = response.xpath('//ul[@class="all-img-list cf"]/li')
        print(len(noval_list))
        if len(noval_list) > 0:
            item = QidianwangNovalItem()
            for noval_li in noval_list:
                item['coverImage'] = 'https:'+noval_li.xpath('.//div[@class="book-img-box"]/a/img/@src').extract_first('')
                # 小说名称
                item['novalTile'] = noval_li.xpath('.//div[@class="book-mid-info"]/h4/a/text()').extract_first('')
                # 作者
                item['cuthor'] = noval_li.xpath('.//div[@class="book-mid-info"]/p[1]/a[1]/text()').extract_first('')
                # 分类
                item['category'] = noval_li.xpath('.//div[@class="book-mid-info"]/p[1]/a[2]/text()').extract_first('')+','+noval_li.xpath('.//div[@class="book-mid-info"]/p[1]/a[3]/text()').extract_first('')
                # 连载状态
                item['status'] = noval_li.xpath('.//div[@class="book-mid-info"]/p[1]/span/text()').extract_first('')
                # 简介
                item['content'] =''.join( noval_li.xpath('.//div[@class="book-mid-info"]/p[2]/text()').extract()).replace(' ','').replace('\r','')
                yield item
    def check_noval_lin(self,links):
        '''
        过滤和拦截
        :param links:
        :return:
        '''
        #links得到的是一个list,里面存放的是link对象
        change_links =[]
        for link in links:
            link.url = link.url+'#Catalog'
            change_links.append(link)
        return  change_links
    def parse_noval_detail(self,response):
        print('小说详情内容获取成功')
        #获取到请求头
        print(response.request.headers,'==========')
        pass
    def parse_chparter_detail(self,response):
        item = QidianwangContentItem()
        # 名称
        item['title'] = response.xpath('//a[@class="act"]/text()').extract_first('')
        # 章节
        item['zhangjie'] = response.xpath('//h3[@class="j_chapterName"]/text()').extract_first('')
        # 字数
        item['zishu'] = response.xpath('//span[@class="j_chapterWordCut"]/text()').extract_first('')
        # 时间
        item['time'] =response.xpath('//span[@class="j_updateTime"]/text()').extract_first('')
        # 内容
        item['neirong'] = ''.join(response.xpath('//div[@class="read-content j_readContent"]/p/text()').extract()).replace('\u3000','').replace('\n','')
        yield item