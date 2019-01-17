# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiachufangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 图片
    coverImage = scrapy.Field()
    # 名字
    title = scrapy.Field()
    # 描述
    content = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 数量
    doitnum = scrapy.Field()
    #发布人
    author = scrapy.Field()
    #详情url
    data_url = scrapy.Field()
    #用料
    yongliao = scrapy.Field()
    #做法
    zuofa = scrapy.Field()
    #小贴士
    tieshi = scrapy.Field()
    #本地图篇存储路径
    localImagePath = scrapy.Field()
