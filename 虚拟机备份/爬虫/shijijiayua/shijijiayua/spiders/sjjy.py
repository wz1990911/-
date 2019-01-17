# -*- coding: utf-8 -*-
import scrapy
import re,json
from shijijiayua.items import ShijijiayuaItem
from scrapy_redis.spiders import RedisSpider

class SjjySpider(RedisSpider):
    name = 'sjjy'
    allowed_domains = ['jiayuan.com']
    #确定目标url,并设置为起始url
    # start_urls = [
    #     #上海徐家汇店
    #     'http://date.jiayuan.com/eventslist_new.php?page=1&city_id=31&shop_id=15',
    #     #武汉典
    #     'http://date.jiayuan.com/eventslist_new.php?page=1&city_id=4201&shop_id=33',
    # ]
    redis_keys = 'sjjy:start_urls'
    def start_requests(self):

        cookies_str = '_gscu_1380850711=43812116hs5dyy11; user_access=1; PHPSESSID=283f655135c88f1627abc9058aa33aa5; plat=date_pc; uv_flag=114.242.248.51; SESSION_HASH=d5eb69633548b50a4fa164b18c3eded552030bd1; jy_refer=www.baidu.com; _gscbrs_1380850711=1; DATE_FROM=daohang; DATE_SHOW_LOC=4201; DATE_SHOW_SHOP=33'

        cookie_dict = {note.split('=')[0]:note.split('=')[1] for note in cookies_str.split('; ')}

        print(cookie_dict)

        for url in self.start_urls:
            #总结：在scrapy框架中,如果发起请求西药携带cookies
            #我们需要将cookies参数赋值给Request对象中的cookies(是一个字典类型)参数
            #如果我们将cookies信息放在请求头中,cookies是不会生效的（起作用）
            yield scrapy.Request(url,cookies=cookie_dict,callback=self.parse)

    def parse(self, response):
        """
        第一页为静态页面,请求成功后回调parse方法
        #提取页面中的活动详情url地址,构造Request请求
        #构造下一页请求
        :param response:
        :return:
        """

        #活动详情url地址
        with open('page.html','w') as file:
            file.write(response.text)
        detail_urls = response.xpath('//h2[@class="hot_title"]/a/@href').extract()
        detail_urls2 = response.xpath('//ul[@class="review_detail fn-clear t-activiUl"]/li/a[1]/@href').extract()
        print(len(detail_urls),len(detail_urls2))

        for url in detail_urls:
            full_url = response.urljoin(url)
            yield scrapy.Request(full_url,callback=self.parse_detail_data)

        #构造下一页请求
        #提取当前页的url地址中分页pagenum
        pattern = re.compile('.*?page=(\d+).*?')
        cur_page = re.findall(pattern,response.url)[0]
        next_page = int(cur_page)+1
        #替换
        pattern = re.compile('page=\d+')
        next_page_url = re.sub(
            pattern,
            'page='+str(next_page),
            response.url
        )
        print(cur_page,next_page_url)

        yield scrapy.Request(next_page_url,callback=self.parse_other_page_data)

    def parse_other_page_data(self,response):
        print('=====其他分页的数据',response.text,response.status)

        data_list = json.loads(response.text)
        if isinstance(data_list,dict) and data_list['status'] == '2':
            #没有数据了
            pass
        elif isinstance(data_list,list) and len(data_list) > 0:
            for subDict in data_list:
                id = subDict['id']
                full_detail_url = 'http://date.iayuan.comj/activityreviewdetail.php?id='+id
                yield scrapy.Request(full_detail_url,callback=self.parse_detail_data)

            #构造下一页的url地址
            # 提取当前页的url地址中分页pagenum
            pattern = re.compile('.*?page=(\d+).*?')
            cur_page = re.findall(pattern, response.url)[0]
            next_page = int(cur_page) + 1
            # 替换
            pattern = re.compile('page=\d+')
            next_page_url = re.sub(
                pattern,
                'page=' + str(next_page),
                response.url
            )
            print(cur_page, next_page_url)
            yield scrapy.Request(next_page_url, callback=self.parse_other_page_data)

    def parse_detail_data(self,response):
        """
        这里返回的是json字符串
        :param response:
        :return:
        """

        with open('detail.html','w') as file:
            file.write(response.text)
        #实例化item
        item = ShijijiayuaItem()
        # 活动标题
        item['title'] = ''.join(response.xpath('//h1[@class="detail_title"]/text()').extract())
        # 活动时间
        item['time'] = ','.join(response.xpath('//div[@class="detail_right fn-left"]/ul[@class="detail_info"]/li[1]//text()').extract())
        # 活动地址
        item['adress'] = response.xpath('//ul[@class="detail_info"]/li[2]/text()').extract_first('')
        # 参加人数
        item['joinnum'] = response.xpath('//ul[@class="detail_info"]/li[3]/span[1]/text()').extract_first('')
        # 预约人数
        item['yuyue'] = response.xpath('//ul[@class="detail_info"]/li[3]/span[2]/text()').extract_first('')
        # 介绍
        item['intreduces'] = response.xpath('//div[@class="detail_act fn-clear"][1]//p[@class="info_word"]/span[1]/text()').extract_first('')
        # 提示
        item['point'] = response.xpath('//div[@class="detail_act fn-clear"][2]//p[@class="info_word"]/text()').extract_first('')
        # 体验店介绍
        item['introductionStore'] = ''.join(response.xpath('//div[@class="detail_act fn-clear"][3]//p[@class="info_word"]/text()').extract())
        # 图片连接
        item['coverImage'] = response.xpath('//div[@class="detail_left fn-left"]/img/@data-original').extract_first('')

        print(item)

        yield  item





