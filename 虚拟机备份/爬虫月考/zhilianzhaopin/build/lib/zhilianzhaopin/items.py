# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhilianzhaopinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #标题
    wz_title = scrapy.Field()
    #工资
    wz_gongzi = scrapy.Field()
    #地址
    wz_dizhi = scrapy.Field()
    #年龄
    wz_nianling = scrapy.Field()
    #学历
    wz_xueli = scrapy.Field()
    #待遇
    wz_daiyu = scrapy.Field()
    #公司名称
    wz_mingzi = scrapy.Field()
    #企业类型
    wz_qiyeleix = scrapy.Field()
    #人数规模
    wz_guimo = scrapy.Field()
    #状态
    wz_zhuangtai = scrapy.Field()

    def get_collection_name(self):
        return 'zhaopin'

class Zhilianzhaopin_dataItem(scrapy.Item):
    # 公司名字
    wz_gs_name = scrapy.Field()
    # 公司信息
    wz_gs_xinxi = scrapy.Field()
    # 公司url
    wz_gs_url = scrapy.Field()
    # 公司信息介绍
    wz_gs_jieshao =scrapy.Field()

    def get_collection_name(self):
        return 'gongsi'
