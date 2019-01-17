# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShijijiayuaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #活动标题
    title = scrapy.Field()
    #活动时间
    time = scrapy.Field()
    #活动地址
    adress = scrapy.Field()
    #参加人数
    joinnum = scrapy.Field()
    #预约人数
    yuyue = scrapy.Field()
    #介绍
    intreduces = scrapy.Field()
    #提示
    point = scrapy.Field()
    #体验店介绍
    introductionStore = scrapy.Field()
    #图片连接
    coverImage = scrapy.Field()

    def insert_data_to_db(self, dataDict):
        sql = """
        INSERT INTO sjjy (%s)
        VALUES (%s)
        """ % (','.join(dataDict.keys()), ','.join(['%s'] * len(dataDict)))

        data = list(dataDict.values())

        return sql, data
