# -*- coding: utf-8 -*-
import scrapy
from  jobboleproject.items import JobboleprojectItem

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/1/']

    def parse(self, response):
        #获取响应的二进制数据(当文件出现乱码的时候可以娜奥二进制数据进行解码
        b_html = response.body
        #获取响应头
        response_headers= response.headers
        print(response_headers)
        #获取请求头
        request_headers = response.request.headers
        pass


