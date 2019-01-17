# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiachufangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #图片链接
    coverImage = scrapy.Field()
    #名称
    title = scrapy.Field()
    #描述
    content = scrapy.Field()
    #评分
    score = scrapy.Field()
    #多少人做过
    doitnum = scrapy.Field()
    #发布人
    author = scrapy.Field()
    #用料
    used = scrapy.Field()
    #做法
    methodway = scrapy.Field()

    def insert_data_to_db(self,dataDict):
        sql = """
        INSERT INTO caipu (%s)
        VALUES (%s)
        """ % (','.join(dataDict.keys()),','.join(['%s']*len(dataDict)))

        data = list(dataDict.values())

        return sql,data

