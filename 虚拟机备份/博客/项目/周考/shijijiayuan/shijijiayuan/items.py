# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShijijiayuanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 时间
    time = scrapy.Field()
    # 地址
    dz = scrapy.Field()
    # 参加
    canjia = scrapy.Field()
    # 预约
    yuyue = scrapy.Field()
    # 活动介绍
    jieshao = scrapy.Field()
    # 温馨提示
    wxts = scrapy.Field()
    # 体验店介绍
    tyd = scrapy.Field()
