# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from woaiwojia.items import WoaiwojiaItem,WoaiwojiaContentItem
class WoaiwojiaPipeline(object):
    def __init__(self, host, user, pwd, db, charset):
        # 创建一个数据库链接
        self.client = pymysql.Connect(host, user, pwd, db, charset=charset)
        # 创建游标
        self.cursor = self.client.cursor()

    @classmethod
    def from_crawler(cls, crawler):
        host = crawler.settings['MYSQL_HOST']
        user = crawler.settings['MYSQL_USER']
        pwd = crawler.settings['MYSQL_PWD']
        db = crawler.settings['MYSQL_DB']
        charset = crawler.settings['CHARSET']
        return cls(host, user, pwd, db, charset)


    def process_item(self, item, spider):
        sql, data = item.insert_data_to_db(dict(item))

        try:
            self.cursor.execute(sql, data)
            self.client.commit()
            print('数据插入成功')
        except Exception as err:
            print(err)
            self.client.rollback()

        return item

    def colse_spider(self, spider):
        self.cursor.close()
        self.client.close()
