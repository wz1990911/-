# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QuanbenItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 大分类
    fenlei = scrapy.Field()


    # 往mysql数据库下存储数据调用这个方法,返回sql语句和
    # 要插入的数据

    def insert_data_to_db(self, dataDict):
        sql = """
           INSERT INTO xiaoshuo_fenlei(%s)
           VALUES (%s)
           """ % (
            ','.join(dataDict.keys()),
            ','.join(['%s'] * len(dataDict))
        )

        data = list(dataDict.values())

        return sql, data



class Biaoti(scrapy.Item):
    # 分类标题
    flbt = scrapy.Field()

    #书名
    title = scrapy.Field()

    # 往mysql数据库下存储数据调用这个方法,返回sql语句和
    # 要插入的数据

    def insert_data_to_db(self, dataDict):
        sql = """
              INSERT INTO xiaoshuo_biaoti(%s)
              VALUES (%s)
              """ % (
            ','.join(dataDict.keys()),
            ','.join(['%s'] * len(dataDict))
        )

        data = list(dataDict.values())

        return sql, data


class TshuJianjie(scrapy.Item):
    # 作者
    name = scrapy.Field()
    # 简介
    jianjie = scrapy.Field()
    #状态
    zhuangtai = scrapy.Field()
    #字数
    zishu = scrapy.Field()
    # 图片
    image = scrapy.Field()

    # 往mysql数据库下存储数据调用这个方法,返回sql语句和
    # 要插入的数据

    def insert_data_to_db(self, dataDict):
        sql = """
                 INSERT INTO xiaoshuo_tshujianjie(%s)
                 VALUES (%s)
                 """ % (
            ','.join(dataDict.keys()),
            ','.join(['%s'] * len(dataDict))
        )

        data = list(dataDict.values())

        return sql, data


class ZhangjieMing(scrapy.Item):
    #章节名字
    zhangjie = scrapy.Field()
    # 往mysql数据库下存储数据调用这个方法,返回sql语句和
    # 要插入的数据

    def insert_data_to_db(self, dataDict):
        sql = """
                 INSERT INTO xiaoshuo_zhangjieming(%s)
                 VALUES (%s)
                 """ % (
            ','.join(dataDict.keys()),
            ','.join(['%s'] * len(dataDict))
        )

        data = list(dataDict.values())

        return sql, data


class Content(scrapy.Item):
    #内容
    content = scrapy.Field()
    def insert_data_to_db(self, dataDict):
        sql = """
                 INSERT INTO xiaoshuo_content(%s)
                 VALUES (%s)
                 """ % (
            ','.join(dataDict.keys()),
            ','.join(['%s'] * len(dataDict))
        )

        data = list(dataDict.values())

        return sql, data
