# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# import pymongo
# class ZhanzhangPipeline(object):
#     def __init__(self,host,prot,db):
#         self.client = pymongo.MongoClient(host,prot)
#         self.db = self.client[db]
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         host = crawler.settings['MONGO_HOST']
#         prot = crawler.settings['MONGO_PORT']
#         db = crawler.settings['MONGO_DB']
#         return cls(host,prot,db)
#
#     def process_item(self, item, spider):
#         try:
#             title_name = self.db[item.table_name()]
#             title_name.insert(dict(item))
#             print('插入成功')
#
#         except:
#             print('插入失败')
#         return item
import pymysql


class ZhanzhangPipeline(object):
    def __init__(self,host,user,pwd,db,set):
        self.client = pymysql.Connect(host,user,pwd,db,charset=set)
        self.cursor = self.client.cursor()

    @classmethod
    def from_crawler(cls, crawler):
        host = crawler.settings['MYSQL_HOT']
        user = crawler.settings['MYSQL_USER']
        pwd = crawler.settings['MYSQL_PWD']
        db = crawler.settings['MYSQL_DB']
        set = crawler.settings['MYSQL_SET']
        return cls(host,user,pwd,db,set)

    def process_item(self, item, spider):
        sql,data = item.insert_data_db(dict(item))
        try:
            self.cursor.execute(sql,data)
            self.client.commit()
            print('数据插入成功')
        except:
            print('数据插入失败')
            self.client.rollback()
        return item
    def cole_spider(self,spider):
        self.cursor.close()
        self.client.close()