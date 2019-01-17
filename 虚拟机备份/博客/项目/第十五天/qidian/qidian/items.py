# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QidianNovalItem(scrapy.Item):
    #封面图片
    coverImage = scrapy.Field()
    #小说名称
    novalTitle = scrapy.Field()
    #作者
    author = scrapy.Field()
    #分类
    category = scrapy.Field()
    #状态
    status = scrapy.Field()
    #简介
    content = scrapy.Field()

    def get_cllection_name(self):
        return 'novals'




class QidianZhangJieItem(scrapy.Item):
    #小说名称
    noval_name = scrapy.Field()
    #小说标题
    noval_title = scrapy.Field()
    #章节字数
    zj_zi_shu = scrapy.Field()
    #发布时间
    fb_data = scrapy.Field()
    #小说内容
    content = scrapy.Field()

    def get_cllection_name(self):
        return 'chpaters'







