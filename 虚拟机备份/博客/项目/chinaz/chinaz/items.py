# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#定义要爬取的字段
class ChinazItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #定义分类的名称
    categoryName = scrapy.Field()
    #分类的url地址
    fristPage = scrapy.Field()

    # 可以通过对象调用此方法,获取到集合名称
    def get_collection_name(self):

        return 'category'

    #往mysql数据库下存储数据调用这个方法,返回sql语句和
    #要插入的数据

    def insert_data_to_db(self,dataDict):
        sql = """
        INSERT INTO category(%s)
        VALUES (%s)
        """ % (
            ','.join(dataDict.keys()),
            ','.join(['%s']*len(dataDict))
        )

        data = list(dataDict.values())

        return sql,data

class Paihangbang(scrapy.Item):
    # 标题
    title = scrapy.Field()
    # 排名
    paim = scrapy.Field()

    # 反链数
    flshu = scrapy.Field()
    # 网站简介
    content = scrapy.Field()
    # 网站排名
    rank = scrapy.Field()
    # 得分
    score = scrapy.Field()
    # 图片地址
    Image = scrapy.Field()
    #本地图片的存储路径
    localImagePath = scrapy.Field()


    #可以通过对象调用此方法，获得集合名称
    def get_collection_name(self):
        return 'webinfo'

        # 往mysql数据库下处处数据掉用这个方法返回生气了语句
    def insert_data_to_db(self, dataDict):
        sql = """
          INSERT INTO webinfo(%s)
          VALUES (%s)
        """ % (
            ','.join(dataDict.keys()),
            ','.join(['%s'] * len(dataDict))
        )

        data = list(dataDict.values())

        return sql, data