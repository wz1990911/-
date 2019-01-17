# -*- coding: utf-8 -*-
import scrapy
import re,json
from  shijiayuan.items import ShijiayuanItem
from scrapy_redis.spiders import RedisSpider
class SjjySpider(RedisSpider):
    name = 'sjjy'
    allowed_domains = ['jiayuan.com']
    #确定目标ulr，并设置为起始url

    # start_urls = [
    #     # 上海徐家汇
    #     'http://date.jiayuan.com/eventslist_new.php?page=1&city_id=31&shop_id=15'
    #
    # ]
    redis_key = 'sjjy:start_urls'

    def start_requests(self):
        cookies_str = 'SESSION_HASH=df31ce1635575e85ba84d125b20909e30d32d24e; user_access=1; PHPSESSID=21453d8412da34328720ac2a130a90af; plat=date_pc; DATE_SHOW_LOC=4201; DATE_SHOW_SHOP=33; uv_flag=218.26.54.250'


        for url in self.start_urls:
            yield scrapy.Request

    def parse(self, response):
        '''
        第一页为静态页面，请求成功后回调parse方法
        提取页面中的活动详情url地址，构造Request请求
        构建下一页请求
        :param response:
        :return:
        '''
        #活动详情url
        # with open('page.html','w') as file:
        #     file.write(response.text)

        detail_urls = response.xpath('//h2[@class="hot_title"]/a/@href').extract()
        # url  =response.xpath('//ul[@class="review_detail fn-clear t-activiUl"]/li/a/@href').extract()
        for url in  detail_urls:
            full_url = response.urljoin(url)
            yield scrapy.Request(full_url,callback=self.parse_detail_data)

        #构造下一页请求
        #提取当前页面的url地址中分页pagenum
        pattern = re.compile('.*?page=(\d+).*?')
        cur_page= re.findall(pattern,response.url)[0]
        next_page = int(cur_page)+1

        #替换
        pattern = re.compile('page=\d+')
        next_page_url = re.sub(pattern,'page='+str(next_page),response.url)
        # print(next_page_url)
        yield scrapy.Request(next_page_url,callback=self.parse_other_page_data)

    def parse_other_page_data(self,response):
        '''
        #这里返回的是json字符串
        :param response:
        :return:
        '''
        data_list = json.loads(response.text)
        if isinstance(data_list,dict) and data_list['status'] == 2:
            #没有数据了
            pass
        elif isinstance(data_list,list) and len(data_list) > 0 :
            for subDict in data_list:
                id = subDict['id']
                full_detail_url = 'http://date.jiayuan.com/activityreviewdetail.php?id='+str(id)
                # print('=============',full_detail_url)
                yield scrapy.Request(full_detail_url,callback=self.parse_detail_data)
                # 构造下一页请求
                # 提取当前页面的url地址中分页pagenum
            pattern = re.compile('.*?page=(\d+).*?')
            cur_page = re.findall(pattern, response.url)[0]
            next_page = int(cur_page) + 1

            # 替换
            pattern = re.compile('page=\d+')
            next_page_url = re.sub(pattern, 'page=' + str(next_page), response.url)
            # print('============',next_page_url)
            yield scrapy.Request(next_page_url, callback=self.parse_other_page_data)

    def parse_detail_data(self,response):
        item = ShijiayuanItem()
        # 活动标题
        item['title'] = response.xpath('//h1[@class="detail_title"]/text()').extract_first('')

        # 活动时间
        item['time']= ''.join(response.xpath('//ul[@class="detail_info"]/li[1]/text()').extract()) + ''.join(response.xpath('//ul[@class="detail_info"]/li[1]/em/text()').extract())
        # print(time)
        # 活动地址
        item['adress'] = response.xpath('//ul[@class="detail_info"]/li[2]/text()').extract_first('')
        # 参加人数

        item['join'] = response.xpath('//ul[@class="detail_info"]/li[3]/span[1]/text()').extract_first('')

        # 预约人数
        item['yuyue'] = response.xpath('//ul[@class="detail_info"]/li[3]/span[2]/text()').extract_first('')
        # 活动介绍
        item['intreduces'] = ''.join(response.xpath('//p[@class="info_word"]/text()').extract())
        # 温馨提示
        item['point'] = response.xpath('//div[@id="date_float"]/div[3]/div[2]/p/text()').extract_first('')
        # 体验店介绍

        item['introductionStire'] = response.xpath('//div[@id="date_float"]/div[4]/div[2]/p/text()').extract_first('')
        # 图片链接
        item['coverImage'] = response.xpath('//div[@class="detail_left fn-left"]/img/@data-original').extract_first('')
        yield item