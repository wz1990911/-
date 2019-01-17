# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WoaiwojiaItem(scrapy.Item):
    #标题
    title = scrapy.Field()
    # 空间
    kongjian = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 发布时间和状况
    time_data = scrapy.Field()
    # 看房时间
    room_time = scrapy.Field()

    def insert_data_to_db(self, dataDict):
        sql = """
        INSERT INTO wawj_list(%s)
        VALUES (%s)
        """ % (
            ','.join(dataDict.keys()),
            ','.join(['%s'] * len(dataDict))
        )

        data = list(dataDict.values())

        return sql, data

class WoaiwojiaContentItem(scrapy.Item):
    # 标题
    title = scrapy.Field()
    #房源信息
    fyxinxi = scrapy.Field()
    # 房源特色
    fytese = scrapy.Field()
    #房源图片
    fyimage = scrapy.Field()
    #小区介绍
    xq_jieshao = scrapy.Field()

    def insert_data_to_db(self, dataDict):
        print('==============================')
        sql = """
        INSERT INTO wawj_content(%s)
        VALUES (%s)
        """ % (
            ','.join(dataDict.keys()),
            ','.join(['%s'] * len(dataDict))
        )

        data = list(dataDict.values())

        return sql, data
