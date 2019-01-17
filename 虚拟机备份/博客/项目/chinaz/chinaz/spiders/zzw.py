# -*- coding: utf-8 -*-
import scrapy
import time

# 存储数据的容器
from chinaz.items import ChinazItem,Paihangbang
from urllib.parse import urljoin


# 爬虫文件
class ZzwSpider(scrapy.Spider):
    # 爬虫文件的名称
    name = 'zzw'
    # chinaz.com :设置允许爬取的域(可以指定多个 )
    allowed_domains = ['chinaz.com']
    # 设置起始的url(可以指定多个)
    start_urls = ['http://top.chinaz.com/']

    def parse(self, response):
        '''
        在这里接受响应结果，解析数据，提取新的url
        :param response: 响应结果
        :return:
        '''
        # 获取响应状态码
        # status = response.status
        # 获取响应的html文本
        # html_text = response.text
        # print(status,html_text)
        # with open('page_html','w') as file:
        #     file.write(html_text)
        # 获取响应的二进制数据(当responpse.text出现乱码的时候，可以拿到二进制数据，进行解码)
        # b_html = response.body
        # print(b_html)
        # #获取响应头
        # response_header = response.headers
        # print('响应头',response_header)
        # #获取请求头
        # request_headers = response.request.headers
        # print('请求头',request_headers)
        # step1:获取标题和分类的url地址
        # response.xpath可以直接根据xpath语法提取目标url
        # category_list = response.xpath('//di[@class="MaWebClist"]/dd')+response.xpath('//di[@class="MaWebClist02"]/dd')
        # 获取到所有dd标签,每一个都是selector,并且放在列表里面
        category_list = response.xpath('//div[@class="MainWebClass clearfix"]/dl/dd/a')
        # print(category_list)
        # print(len(category_list))
        for category_a in category_list:
            category_item = ChinazItem()
            # extract():作用将提取到的Selector对象中,data数据提取出来
            # 是一个unicode编码类型
            # title = category_a.xpath('./text()').extract()
            # extract_first(''):取转换之后的列表中的第一个元素如果列表为空
            # 可以在括号中设置一个默认值,如果不设置默认返回值返回的是None
            title = category_a.xpath('./text()').extract_first('')

            href = category_a.xpath('./@href').extract_first('')
            category_item['categoryName'] = title
            # 方式一
            # category_item['fristPage'] = urljoin(response.url,href)
            # 将不完整url拼接完整
            category_item['fristPage'] = response.urljoin(href)
            # 将item数据交给管道(这里使用yield)
            yield category_item

            '''
            url, 发起请求的url地址
            callback = None, 请求成功后的毁掉
            method = 'GET' 请求方式
            headers = None 请求头
            cookies = None  cookies
            meta = None 要传递的参数
            encoding = 'utf-8' 编码类型
            priority = 0 优先级
            dont_filter = False 是否要过滤请求(False去重, 不会重复请求
            errback = None 请求错误的毁掉
            '''

            yield scrapy.Request(
                url=category_item['fristPage'], callback=self.parse_web_list_data

            )


    def parse_web_list_data(self, response):
        # 分类的列表页发起请求成功或的毁掉
        # 在这里提取列表中网站数据将或取的嫁给管道
        # 2提取下一页分页地址,继续发起请求

        title_list = response.xpath('//ul[@class="listCentent"]/li')
        # # print(title_list)
        for title in title_list:
            xl_item = Paihangbang()
            xl_item['title'] = title.xpath('./div[@class="CentTxt"]/h3/a/text()').extract_first('')

            xl_item['paim'] = title.xpath('./div[@class="CentTxt"]/div/p[1]/a/text()').extract_first('')
            # qzhong = category_list_data.xpath('./div[@class="CentTxt"]/div/p[2]/a/img/@src').extract_first('')
            # PR = category_list_data.xpath('./div[@class="CentTxt"]/div/p[3]/a/img/@src').extract_first('')
            xl_item['flshu'] = title.xpath('./div[@class="CentTxt"]/div/p[last()]/a/text()').extract_first(
                '')
            xl_item['content'] = title.xpath('./div[@class="CentTxt"]/p/text()').extract_first('')
            xl_item['rank'] = title.xpath('./div[@class="RtCRateWrap"]/div/strong/text()').extract_first(
                '')
            xl_item['score'] = title.xpath('./div[@class="RtCRateWrap"]/div/span/text()').re('\d+')[0]
            xl_item['Image'] = title.xpath('./div[@class="leftImg"]/a/img/@src').extract_first('')

            # 将获取的数据交给管道处理
            yield xl_item