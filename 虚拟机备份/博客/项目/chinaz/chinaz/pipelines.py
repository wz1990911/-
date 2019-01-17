# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#在这里做数据的过滤和持久化
#在循环之前我们要先激活管道,在settings文件中激活

# class ChinazPipeline(object):
#     def __init__(self):
#         # 一般在初始化方法里面创建数据库连接,货值是文件
#         self.file = open('chinaz.json','a+')
#         self.wile = open('wangzhan.json','a+')
#     def open_spider(self,spider):
#         '''
#         可选方法，当我们ｓｐｉｄｅｒ被开启的时候会执行一次只调用一次
#         :param spider:
#         :return:
#         '''
#         print('爬虫开始')
#     def process_item(self, item, spider):
#         '''
#         #所有的数据都会经过这个方法
#         :param item:
#         :param spider:
#         :return:
#         '''
#
#         print('经过管道')
#         print(type(item))
#         #将item数据转换为一个字典
#         item_dict = dict(item)
#         #可以将数据写入到json文件中
#         json_str = json.dumps(item_dict,ensure_ascii=False)
#         self.file.write(json_str+"\n")
#         #将不同的item 对象存到不同的不同的ｊｓｏｎ文件中
#         if isinstance(item,ChinazItem):
#             self.file.write(json_str + "\n")
#             print('分类')
#         elif isinstance(item,Paihangbang):
#
#             self.wile.write(json_str + "\n")
#             print('网站')
#
#         return item
#     def close_spider(self,spider):
#         '''
#         可选方法在爬虫结束的时候调用改犯法（执行一次
#         :param spider:
#         :return:
#         '''
#         #关闭文件
#         self.file.close()
#         self.wile.close()
#         print('爬虫结束')

import pymongo
import pymysql
import json
from chinaz.items import ChinazItem,Paihangbang
import time
# class ChinazPipeline1(object):
#
#     def process_item(self, item, spider):
#         #return item的作用：这里如果不返回item那么下一个管道
#         # 文件没有办法接受到item对象
#         return item
# class ChinazPipeline(object):
#     def __init__(self,host,port,db):
#         self.client = pymongo.MongoClient(host,port)
#         self.db = self.client[db]
#
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         '''
#         类方法，crawler可以从crawler里面获取到爬虫的核心组件(从settings.py设置文件中获取相关参数)
#         :param crawler:
#         :return:
#         '''
#         host = crawler.settings['MONGO_HOST']
#         port = crawler.settings['MONGO_PORT']
#         db = crawler.settings['MONGO_DB']
#         return cls(host,port,db)
#
#     def process_item(self, item, spider):
#         # # 将数据存储到数据库即可中
#         # if isinstance(item,ChinazItem):
#         #     print('分类')
#         #     col_name = self.db['category']
#         #     col_name.insert(dict(item))
#         # elif isinstance(item,Paihangbang):
#         #     print('这是网站的ｉｔｅｍ数据')
#         try:
#             col_name = self.db[item.get_collection_name()]
#             col_name.insert(dict(item))
#         except:
#
#             print('插入失败')
#         #这里如果不返回item下一个就无法获得item对象
#         return item
#
#     def close_spider(self, spider):
#
#
#
#
#        self.client.close()


#在这里执行图片下载操作
#ImagesPipeline进行图片下载
from scrapy.contrib.pipeline.images import ImagesPipeline
#DropItem如果数据不符合要求就丢弃数据
from scrapy.exceptions import DropItem
from chinaz.items import ChinazItem,Paihangbang
import scrapy,os
#get_project_settings可以获取到settings文件中的数据
from  scrapy.utils.project import get_project_settings
#从settings文件中获取到IMAGES_STORE图片的文件家路径
IMAGE_STORE = get_project_settings().get('IMAGES_STORE')
class ChinazImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        #从这个方法中获取图片地址发起图片下载请求
        if isinstance(item,Paihangbang):
            #获取图片链接
            Image = 'http:'+item['Image']
            #注意.这里使用yield
            yield scrapy.Request(Image)
    def item_completed(self, results, item, info):
        '''
        图片请求发起成功后的回调
        :param results: 图片请求后的一个结果状态[(True,{'path':'图片存储地址哦'}]
        :param item: 数据
        :param info: 其他参数
        :return:
        '''
        if isinstance(item,Paihangbang):
            # 从结果列表中取出图片的存储路径
            paths = [subdict['path'] for status,subdict in results if status]
            if len(paths) > 0:
                #/home/cui/桌面/chinazimage
                #full/463fddb12670b1ff13cca60e8902c7b89923e8df.jpg
               #os.rename:修改文件
                os.rename(IMAGE_STORE+'/'+paths[0],IMAGE_STORE+'/'+item['title']+'.jpg')
                item['localImagePath'] = IMAGE_STORE+'/'+item['title']+'.jpg'
            else:
                #如果图片下载不成功,我们就布储存item
                raise  DropItem('图片没有下载成功')
        #return item 为了 将item数据传递给下一个管道
        return item


class ChinazPipeline(object):
    def __init__(self,host,user,pwd,db,charset):
        self.client = pymysql.Connect(host,user,pwd,db, charset=charset)
        #创建游标
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
        sql,data = item.insert_data_to_db(dict(item))

        try:
            self.cursor.execute(sql, data)
            self.client.commit()
            print('数据插入成功')
        except Exception as err:
            print(err)
            # print('数据插入错误')
            self.client.rollback()

        return item

    def colse_spider(self, spider):
        self.cursor.close()
        self.client.close()

#数据的异步插入
from twisted.enterprise import adbapi
class ChinazPipelineAdbapi(object):
    def __init__(self,dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_crawler(cls,crawler):
        #host,port,user,pwd,db,charset
        host = crawler.settings('MYSQL_HOST')
        port = crawler.settings('MYSQL_PORT')
        user = crawler.settings('MYSQL_USER')
        pwd = crawler.settings('MYSQL_PWD')
        db = crawler.settings('MYSQL_DB')
        charset = crawler.settings('CHARSET')
        parmas = {
            'host':host,
            'port':port,
            'user':user,
            'pwd':pwd,
            'db':db,
            'charset':charset,
        }

        dbpool = adbapi.ConnectionPool('pymysql',**parmas)
        return cls(dbpool)
    def process_item(self,item,spider):
        #让连接池去执行数据插入的方法
        hanler = self.dbpool.runInteraction(
            self.inster_data_to_db_with_data,
            item,spider,
        )
        hanler.addErrback(
            self.handler_error,
            item
        )
        return item
    def inster_data_to_db_with_data(self,cursor,item,spider):

        sql,data = item.insert_data_to_db(dict(item))
        try:
            cursor.excute(sql,data)
        except Exception as err:
            print(err)
    def handler_error(self,failure,item):
        '''
        在这个方法中处理数据插入异常的结果要做什么看自己需求
        :param failure:
        :param item:
        :return:
        '''
        print(failure,'插入失败')
