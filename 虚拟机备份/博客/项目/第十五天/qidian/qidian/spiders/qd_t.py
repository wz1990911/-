# -*- coding: utf-8 -*-
import scrapy,re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from qidian.items import QidianNovalItem,QidianZhangJieItem

class QdTSpider(CrawlSpider):
    name = 'qd_t'
    allowed_domains = ['qidian.com']
    start_urls = ['https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=1']

    rules = (
        Rule(
            LinkExtractor(allow=r'.*?page=\d+',restrict_xpaths='//ul[@class="lbf-pagination-item-list"]'),
            callback='parse_item', follow=True
        ),
        #详情的url地址：https://book.qidian.com/info/1010734492
        Rule(
            LinkExtractor(allow=r'.*?/info/\d+',restrict_xpaths='//div[@class="book-mid-info"]'),
            callback='',follow=True,
            process_links= 'ckeck_noval_link'
        ),
        #章节详情地址:
        #https://read.qidian.com/chapter/ORlSeSgZ6E_MQzCecGvf7A2/atYOCLHSg35Ms5iq0oQwLQ2
        #https://vipreader.qidian.com/chapter/1010734492/397543156
        Rule(
            LinkExtractor(allow='//read.qidian.com/chapter/.*?',restrict_xpaths='//div[@class="volume"]'),
            callback='parse_chpater_detail',
            follow=False
        )
    )

    def parse_start_url(self, response):
        """
        TODO 起始url请求完成后的回调方法
        """
        pass

    def parse_item(self, response):
        """找到小说的列表,提取每一本小说的内容"""
        #小说列表
        noval_item = QidianNovalItem()
        noval_list = response.xpath('//ul[@class="all-img-list cf"]/li')
        print(len(noval_list))
        if len(noval_list) > 0:
            for noval_li in noval_list:
                # 封面图片
                noval_item['coverImage'] = noval_li.xpath('./div[@class="book-img-box"]/a/img/@src').extract_first()
                # 小说名称
                noval_item['novalTitle'] = noval_li.xpath('./div[@class="book-mid-info"]/h4/a/@href').extract_first()
                # 作者
                noval_item['author'] = noval_li.xpath('./div[@class="book-mid-info"]/p[@class="author"]/a[1]/text()').extract_first()
                # 分类
                noval_item['category'] = noval_li.xpath('./div[@class="book-mid-info"]/p[@class="author"]/a[2]/text()').extract_first() +  '.' + noval_li.xpath('div[@class="book-mid-info"]/p[@class="author"]/a[3]/text()').extract_first()
                # 状态
                noval_item['status'] = noval_li.xpath('./div[@class="book-mid-info"]/p[@class="author"]/span/text()').extract_first()
                # 简介
                noval_item['content'] = noval_li.xpath('./div[@class="book-mid-info"]/p[@class="intro"]/text()').extract_first().replace(' ','').replace('\r','')

                print(noval_item)

                yield noval_item

    def ckeck_noval_link(self,links):
        #在这个方法里做url的拦截

        #TODO links得到是一个列表，里面存放的都是Link对象
        change_list = []
        for link in links:
            link.url = link.url + '#Catalog'
            change_list.append(link)
        return change_list





    def parse_noval_detaill(self,response):
        print('小说章节获取成功')
        pass

    def parse_chpater_detail(self,response):
        #获取请求的请求头
        print(response.request.headers)

        content_item = QidianZhangJieItem()
        # 小说名称
        content_item['noval_name'] = response.xpath('//div[@class="crumbs-nav"]/a[4]/text()').extract_first()
        # 小说标题
        content_item['noval_title'] = response.css('h3.j_chapterName::text').extract_first()
        # 章节字数
        content_item['zj_zi_shu'] = response.css('span.j_chapterWordCut::text').extract_first()
        # 发布时间
        content_item['fb_data'] = response.css('span.j_updateTime::text').extract_first()
        pattern = re.compile(
            '[^\x00-\xff]', re.S
        )
        # 小说内容
        content_item['content'] = ''.join(re.findall(pattern,str(response.css('div.read-content.j_readContent').extract_first()).replace('\u3000','')))


        yield content_item







