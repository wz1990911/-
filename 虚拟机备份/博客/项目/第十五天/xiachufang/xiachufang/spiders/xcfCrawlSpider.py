# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

#创建通用爬虫的命令
#scrapy genspider -t crawl  爬虫名称 域

class XcfcrawlspiderSpider(CrawlSpider):
    #爬虫名称
    name = 'xcfCrawlSpider'
    #允许爬取的域
    allowed_domains = ['xiachufang.com']
    #起始url
    start_urls = ['https://www.xiachufang.com/category/']

    # rules:是一个元组（列表）,里面存放的是规则Rule规则对象
    # 可以有多个规则

    # Rule:
    # LinkExtractor:设置提取规则
    # callback:设置回调函数（获取响应,解析数据）
    # follow:设置是否需要跟进

    # 　process_links:指定一个方法,可以在方法中拦截
    # 规则提取到的url构建的link对象

    # process_request：指定一个方法,可以在这个方法中拦截
    # request对象

    # LinkExtractor中的相关参数
    """
    allow = (), :设置正则规则,符合正则表达式的所有url都会被提取,
                如果为空,则提取全部的url连接
    deny = (), :设置这则表达式规则,符合规则的url连接不会被提取
                优先集比allow要高
    allow_domains = (), 允许爬取的域

    deny_domains = (), 指定不允许爬取的域,如果url在deny_domains
                      设置的域下,那么这个url就不会被提取,这个优先级
                      高于allow_domains
    restrict_xpaths = ():使用xpath语法,定位到指定的标签(节点)下,
                        在该标签(节点)下获取我们的url连接
    restrict_css = ()
    """

    # http://www.xiachufang.com/category/40073/
    rules = (
        Rule(
            LinkExtractor(allow=r'.*?/category/\d+/'),
            callback='parse_item',
            follow=True,
            process_links='check_category_url'
        ),
        # 菜单详情地址,
        # http://www.xiachufang.com/recipe/1055105/
        # http://www.xiachufang.com/recipe/12137/
        # http://www.xiachufang.com/recipe/100147684/

        # Rule(
        #     LinkExtractor(
        #         allow=r'.*?/recipe/\d+/',
        #     ),
        #     callback='parse_caipu_detail',
        #     follow=False,
        # )

    )

    # def parse(self): 一定不能出现这个方法,因为crawlSpider使用了这个方法
    def parse_item(self, response):
        print('分类获取成功')
        print(response.status, response.url)

    def check_category_url(self, links):
        print('===================', links, '===================')

        change_links = []

        for link in links:
            # http://nxkasbcbnclasnlvabkas
            # 　url,text
            link.url = link.url + 'abcd'
            change_links.append(link)

        print('======', change_links, '======')
        return change_links

    def parse_caipu_detail(self, response):
        """
        在这里做详情请求成功后的回调结果,从响应结果中提取目标数据
        :param response:
        :return:
        """
        print('详情获取成功')
        print(response.status, response.url)


