# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QunawangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #标题
    wz_title = scrapy.Field()
    #介绍
    wz_jieshao = scrapy.Field()
    #价格
    wz_price = scrapy.Field()
    #历史成交
    wz_chengjiao = scrapy.Field()
    #编号
    wz_bianhao = scrapy.Field()
    #评论
    wz_pinglun = scrapy.Field()
    #套餐
    wz_taocan = scrapy.Field()
    #图片
    wz_image = scrapy.Field()
    #行程包含
    wz_baohan = scrapy.Field()
    #儿童政策
    wz_et_zhengce = scrapy.Field()
    #老人政策
    wz_lr_zhengce = scrapy.Field()
    #行程不含
    wz_buhan = scrapy.Field()