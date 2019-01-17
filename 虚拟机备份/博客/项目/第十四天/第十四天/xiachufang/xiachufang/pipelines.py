# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ImagesPipeline进行图片下载
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
import scrapy
import os
from scrapy.utils.project import get_project_settings
from xiachufang.items import XiachufangItem
IMAGE_STORE = get_project_settings().get('IMAGES_STORE')
class ChinazImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        #从这个方法中获取图片地址发起请求
        if isinstance(item,XiachufangItem):
            #获取图篇链接诶
            webCoverImage = item['coverImage']
            yield scrapy.Request(webCoverImage)
    def item_completed(self, results, item, info):
        if isinstance(item,XiachufangItem):
            #从结果列表取出图片毒储存路径
            paths = [ subdict['path'] for status,subdict in results if status ]
            if len(paths) > 0:
                os.rename(IMAGE_STORE+'/'+paths[0],IMAGE_STORE+'/'+item['title']+'.jpj')
                item['localImagePath'] = IMAGE_STORE+'/'+item['title']+'.jpj'
            else:
                #如果下在不成功我们就不存处
                raise DropItem('图片没有下载成功')
        return item



import pymongo
#数据的异步插入
from twisted.enterprise import adbapi
class XiachufangPipeline(object):
    """
       将数据保存到数据库(mongodb)
       """

    def __init__(self, host, port, db):
        # 在初始化方法中创建数据库连接
        self.client = pymongo.MongoClient(host, port)
        # 获取数据库
        self.db = self.client[db]

    @classmethod
    def from_crawler(cls, crawler):
        """
        是一个类方法,crawler:可以从crawler里面
        获取到爬虫的核心组件（从settings.py设置文件
        中获取相关参数）
        :param crawler:
        :return:
        """
        host = crawler.settings['MONGO_HOST']
        port = crawler.settings['MONGO_PORT']
        db = crawler.settings['MONGO_DB']
        return cls(host, port, db)

    def process_item(self, item, spider):

        try:
            col_name = self.db['jiachang']
            col_name.insert(dict(item))
            print('插入成功')
        except Exception as err:
            print('插入失败')
            print(err)

        return item

    def close_spider(self, spider):

        self.client.close()




