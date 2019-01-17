# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class QidianSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class QidianDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

import random
from fake_useragent import UserAgent


class QidianUserAgentDownloadmiddlerware(object):
    def __init__(self):
        self.User_Agent = UserAgent()



    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        #取出useragent列表
        # user_agents = spider.settings['USER_AGENTS']



        #随机获取一个ua
        # random_ua = random.choice(user_agents)
        random_ua = self.User_Agent.random



        if random_ua:
            print('进过下载中间件,设置了User-Agent')
            #将获取到的ua添加到请求头中
            request.headers['User-Agent'] = random_ua
            #第二种方式
            request.headers.setdefault(b'User-Agent',random_ua)
        return None

import base64
class QidianProxyDownloadMiddlerware(object):

    def process_request(self, request, spider):
        #获取拥有的代理池，从中随机抽取一个
        proxies = spider.settings['PROXIES']

        #随机获取
        proxy = random.choice(proxies)

        if proxy:
            if proxy['user_pwd']:
                print('使用了私密代理')
                #说明有账号密码(西药经过base64编码)
            #将账号密码经过 b64encode里面的数据需要传递一个bytes类型的数据
                pwd = base64.b64encode(proxy['user_pwd'].encode('utf-8')).decode('utf-8')
                request.heades['Proxy-Authorization'] = 'Basic' + ' ' + pwd

                request.meta['proxy'] = proxy['ip_port']
            else:
                #说明没有账户密码
                print('使用普通代理')
                request.meta['proxy'] = proxy['ip_port']


#使用selenium拦截url，加载动态页面
from selenium import webdriver
from scrapy.http import HtmlResponse
from selenium.common.exceptions import TimeoutException
class SeleniumDownloadMiddlerware(object):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='/home/ldz/桌面/驱动/chromedriver')
        #设置请求超时时间
        self.driver.set_page_load_timeout(10)
    def process_request(self,request,spider):
        url = request.url
        try:
            self.driver.get(url)
            if self.driver.page_source:
                #返回response
                response = HtmlResponse(
                    url,
                    status=200,
                    headers=None,
                    body=self.driver.page_source.encode('utf-8'),
                    request=request
                )

                return response
        except TimeoutException as err:
            print('请求超时',err)
            response = HtmlResponse(url,status='400',headers=None,body=b'',request=request)
            return response