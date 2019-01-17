# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
class QidianwangPipeline(object):
    def __init__(self,host,port,dbname):
        self.mongoClient = pymongo.MongoClient(host,port)
        #获取到数据库
        self.db = self.mongoClient[dbname]


    @classmethod
    def from_crawler(cls, crawler):

        host = crawler.settings['MONGO_HOST']
        port = crawler.settings['MONGO_PORT']
        dbname = crawler.settings['MONGO_DB']

        return cls(host,port,dbname)
    def process_item(self, item, spider):
        col_name = item.get_collection_name()
        try:
            self.db[col_name].insert(dict(item))
            print('插入成功')
        except:
            print('插入失败')

        return item
    def close_spider(self,spide):
        self.mongoClient.close()
