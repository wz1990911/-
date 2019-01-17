# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class ZhanzhangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 定义分类的名称
    fenleiname = scrapy.Field()
    # 分类的url地址
    fenleiurl = scrapy.Field()
    def table_name(self):
        return 'leibie'

    def insert_data_db(self,shuju):
        sql ="""
        INSERT INTO leibie(%s)
        VALUES(%s)
        """%(
            ','.join(shuju.keys()),
            ','.join(['%s']*len(shuju))
        )
        data = list(shuju.values())

        return sql,data



class Zhanzhang_data(scrapy.Item):
    #标题
    title = scrapy.Field()
    #周排名
    ranking  = scrapy.Field()
    #反链数
    fanlain = scrapy.Field()
    #总排名
    orders = scrapy.Field()
    #简介
    content = scrapy.Field()
    #图片
    images = scrapy.Field()
    def table_name(self):
        return 'shuju'

    def insert_data_db(self, shuju):
        sql = """
        INSERT INTO shuju_1(%s)
        VALUES(%s)
        """ % (
            ','.join(shuju.keys()),
            ','.join(['%s'] * len(shuju))
        )
        data = list(shuju.values())

        return sql, data


