# -*- coding: utf-8 -*-
import scrapy
from xiachufang.items import XiachufangItem
import time
import re
class XchufSpider(scrapy.Spider):
    name = 'xchuf'
    allowed_domains = ['xiachufang.com']
    # start_urls = ['https://www.xiachufang.com/category/40076/?page=0']
    start_urls=['https://www.xiachufang.com/category/']

    def start_requests(self):
        '''
        重写这个方法可以根据自己的需求发起请求
        :return:
        '''
        for url in self.start_urls:
            yield scrapy.Request(url,callback=self.parse_category,dont_filter=True)

    def parse_category(self,response):
        '''
        获取所有分类菜单链接
        :param response:
        :return:
        '''
        print(response.status)
        # with open('category.html','w') as file:
        #     file.write(response.text)

        category_list = response.css('div.cates-list-mini.clearfix ul li a::attr(href)').extract()
        # print(category_list)
        if len(category_list) > 0:
            #判断如果取到就发起请求
            for category_url in category_list:
                category_url = response.urljoin(category_url)

                yield scrapy.Request(category_url,callback=self.parse_candan_list)



    def parse_candan_list(self, response):
        # url = re.compile('page=(\tr(page)
        # yield scrapy.Request(url, callback=self.parse_candan_list)

        # print(response.status)
        # with open('page.html','w') as file:
        #     file.write(response.text)
        # 图片
        caipu_list = response.css('div.pure-u-3-4.category-recipe-list ul li')
        # print(len(coverImage))
        for caipu in caipu_list:
            itme = XiachufangItem()
            #图片
            itme['coverImage'] = caipu.css('div.cover.pure-u img::attr(data-src)').extract_first('')

            # 名字
            itme['title'] = caipu.css('div.info.pure-u > p.name a::text').extract_first('').replace(' ','').replace('\n','')
            # print(itme)
            # 描述
            itme['content'] = ''.join(caipu.css('p.ing.ellipsis ::text').extract()).replace(' ','').replace('、','').replace('\n','')

            # 评分
            itme['score'] = caipu.css('p.stats span::text').extract_first('')

            # 数量
            try:
                itme['doitnum'] = caipu.css('span.bold.score ::text').extract()[1]

            except:
                itme['doitnum'] = 0


            #  发布人
            itme['author'] = caipu.css('a.gray-font ::text').extract_first('')
            data_url = response.urljoin(caipu.css('p.name a::attr(href)').extract_first(''))
            itme['author'] = data_url


            yield scrapy.Request(
                data_url,
                meta={'item':itme},
                callback= self.peilaio_data
            )
        url = response.css('div.pager a.next ::attr(href) ')
        try:
            if url:
                url = response.urljoin(url)
                yield scrapy.Request(url, callback=self.parse_candan_list)
        except:
            print('没有了')

    def peilaio_data(self,response):
        item = response.meta['item']
        item['yongliao'] = ''.join(response.css('div.ings td ::text ').extract()).replace(' ','').replace('\n','')

        # 做法
        item['zuofa'] = ''.join(response.css('div.steps p ::text').extract())

        # 小贴士
        item['tieshi'] =  ''.join(response.css('div.tip ::text').extract()).replace(' ','').replace('\n','')

        yield item


