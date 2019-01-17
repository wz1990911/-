# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#分类
class QuagnbenItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    fenlei = scrapy.Field()

#图片 书名 简介
class Biaoti(scrapy.Item):
    image = scrapy.Field()
    title = scrapy.Field()
    jianjie = scrapy.Field()

class TshuJianjie(scrapy.Item):
    #作者
    name = scrapy.Field()
    #分类标题
    flbt = scrapy.Field()
    #状态
    zhuangtai = scrapy.Field()

class ZhangjieMing(scrapy.Item):
    #章节名字
    zhhangjie = scrapy.Field()


class Content(scrapy.Item):
    content = scrapy.Field()
