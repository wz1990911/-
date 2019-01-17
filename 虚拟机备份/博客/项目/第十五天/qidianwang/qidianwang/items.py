# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QidianwangNovalItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #封面图派你
    coverImage = scrapy.Field()
    #小说名称
    novalTile = scrapy.Field()
    #作者
    cuthor = scrapy.Field()
    #分类
    category= scrapy.Field()
    #连载状态
    status= scrapy.Field()
    #简介
    content= scrapy.Field()
    def get_collection_name(self):
        return 'novals'
class QidianwangContentItem(scrapy.Item):
    # 名称
    title = scrapy.Field()
    #章节
    zhangjie = scrapy.Field()
    #字数
    zishu = scrapy.Field()
    #时间
    time = scrapy.Field()
    #内容
    neirong = scrapy.Field()
    def get_collection_name(self):
        return 'chpaters'