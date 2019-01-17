# -*- coding: utf-8 -*-
import scrapy
from xiachufang.items import XiachufangItem
from scrapy_redis.spiders import RedisSpider

class XcfSpider(RedisSpider):
    name = 'xcf'
    allowed_domains = ['xiachufang.com']
    # start_urls = ['https://www.xiachufang.com/category/40076/?page=1']
    redis_key = 'xcf:start_urls'
    def parse(self, response):
        print(response.status)
        with open('page.html','w') as file:
            file.write(response.text)

        #获取菜谱的列表
        caipu_list = response.css('div.pure-u-3-4.category-recipe-list ul li')
        print(len(caipu_list))
        for caipu_li in caipu_list:
            item = XiachufangItem()
            # 图片链接
            item['coverImage'] = caipu_li.css('div.cover.pure-u img::attr(data-src)').extract_first('')
            # # 名称
            item['title'] = caipu_li.css('div.info.pure-u > p.name a::text').extract_first('').replace('\n','').replace(' ','')
            # # 描述
            item['content'] = ','.join(caipu_li.css('p.ing.ellipsis > a ::text').extract())
            #在获取(评分和多少人做过)之前需要判断一下
            spans = caipu_li.css('p.stats > span')
            if len(spans) > 1:
                # # 评分
                item['score'] = spans[0].css('::text').extract_first('')
                # # 多少人做过
                item['doitnum'] = spans[1].css('::text').extract_first('')
            else:
                # # 评分
                item['score'] = '0'
                # # 多少人做过
                item['doitnum'] = spans[0].css('::text').extract_first('')

            # # 发布人
            item['author'] = caipu_li.css('p.author a')[0].css('::text').extract_first('')


            #获取详情的地址
            detail_url = caipu_li.css('div.info.pure-u > p.name a ::attr(href)').extract_first()

            if detail_url:
                #得到完整的url地址
                detail_url = response.urljoin(detail_url)
                yield scrapy.Request(detail_url,callback=self.parse_detail_data,meta={'item':item})

        #获取下一页地址,如果存在继续发起请求，不存在则不在发起请求
        next_page_url = response.css('div.pager > a.next ::attr(href)').extract_first()
        if next_page_url:
            next_page_url=response.urljoin(next_page_url)
            yield scrapy.Request(next_page_url,callback=self.parse)

        #方式二获取所有的分页url地址,然后发起请求
        # next_pages = response.css('div.pager a ::attr(href)').extract()
        # if len(next_pages) > 0:
        #     for url in next_pages:
        #         next_page_url = response.urljoin(url)
        #         yield scrapy.Request(next_page_url,callback=self.parse)

    def parse_detail_data(self,response):
        #取出item
        item = response.meta['item']
        #获取用料的列表
        # 对吓：8只;对吓：8只;对吓：8只;对吓：8只;对吓：8只
        tr_list = response.css('div.ings tr')
        used_list = []
        for tr in tr_list:
            name = ''.join(tr.css('td.name ::text').extract()).replace('\n','').replace(' ','')
            value = ''.join(tr.css('td.unit ::text').extract()).replace('\n','').replace(' ','')
            if len(value) == 0:
                value = '若干'
            used_list.append(name+':'+value)
        item['used'] = ';'.join(used_list)
        #获取做法
        item['methodway'] = '->'.join(response.css('div.steps p.text ::text').extract())
        # print(item)
        yield item


