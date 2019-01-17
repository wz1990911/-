# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from twisted.enterprise import adbapi
import pymongo

# class QidianPipeline(object):
#     def __init__(self,dbpool):
#         self.dbpool = dbpool
#
#     @classmethod
#     def from_crawler(cls,crawler):
#         host = crawler.settings['MONGO_HOST']
#         port = crawler.settings['MONGO_PORT']
#         db = crawler.settings['MONGO_DB']
#
#         parmas = {'host':host,'port':port,'db':db}
#
#         dbpool = adbapi.ConnectionPool(
#             'pymongo',
#             **parmas
#         )
#
#         return cls(dbpool)
#     def process_item(self, item, spider):
#         handler = self.dbpool.runInteraction(
#             self.insert_data,
#             item,spider
#         )
#         handler.addErrback(
#             self.handler_err,
#             item
#         )
#
#         return item
#     def insert_data(self,cursor,item,spider):
#         data_name = item.get_cllection_name()
#         try:
#             col_name = cursor.db[data_name]
#             col_name.insert(dict(item))
#             print('数据插入成功')
#         except Exception as err:
#             print('********',err)
#     def handler_err(self,failure,item):
#         print(failure,'数据插入失败')


