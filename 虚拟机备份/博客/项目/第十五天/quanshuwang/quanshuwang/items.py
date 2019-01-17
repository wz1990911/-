# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QuanshuwangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # id
    id = scrapy.Field()
    #分类
    fenlei = scrapy.Field()
    #名字
    name = scrapy.Field()
    #简介
    jianjie = scrapy.Field()