# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShijiayuanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #活动标题
    title = scrapy.Field()
    # 活动时间
    time = scrapy.Field()
    #活动地址
    adress = scrapy.Field()
    #参加人数
    join = scrapy.Field()
    #预约人数
    yuyue = scrapy.Field()
    #活动介绍
    intreduces = scrapy.Field()
    #温馨提示
    point = scrapy.Field()
    #体验店介绍
    introductionStire = scrapy.Field()
    #图片链接
    coverImage = scrapy.Field()
