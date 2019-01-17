# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class ZhilianzhaopinPipeline(object):

    def __init__(self, host, port, db):
        # 在初始化方法中创建数据库连接
        self.client = pymongo.MongoClient(host, port)
        # 获取数据库
        self.db = self.client[db]

    @classmethod
    def from_crawler(cls, crawler):
        host = crawler.settings['MONGO_HOST']
        port = crawler.settings['MONGO_PORT']
        db = crawler.settings['MONGO_DB']
        return cls(host, port, db)

    def process_item(self, item, spider):
        try:
            col_name = self.db[item.get_collection_name()]

            col_name.insert(dict(item))
            print('插入成功','=======')
        except Exception as err:
            print('插入失败')
            print(err)

        return item

    def close_spider(self, spider):

        self.client.close()
