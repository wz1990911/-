import requests,gevent
from lxml import etree
from gevent import pool, monkey
import time
import re
from pymongo import MongoClient


monkey.patch_all()

def qingqiu(req_url):
    req_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }

    response = requests.get(req_url, headers=req_headers)
    return response

def fenlei(req_url):
    response = qingqiu(req_url)
    response.encoding = 'gbk'
    if response.status_code == 200:
        html_element = etree.HTML(response.text)
        fenlei = html_element.xpath('//ul[@class="channel-nav-list"]/li/a/@href')
        return fenlei





def xiangqing_url(req_url):

    response = qingqiu(req_url)
    response.encoding = 'gbk'
    if response.status_code == 200:
        html_element = etree.HTML(response.text)
        noval_lis = html_element.xpath('//section[@class="section board-list board-list-collapse"]/ul/li/a[1]/@href')
        # print(noval_lis)
        for xq in noval_lis:
            # a = xq.xpath('.//li/a/@href')[0]
            xiangqing(xq)

def xiangqing(req_url):
    # print(req_url)

    response = qingqiu(req_url)
    response.encoding = 'gbk'
    if response.status_code == 200:
        html_element=etree.HTML(response.text)
        url = html_element.xpath('//div[@class="b-oper"]/a[1]/@href')[0]
        mulu(url)

def mulu(req_url):
    response = qingqiu(req_url)
    response.encoding = 'gbk'
    if response.status_code == 200:
        html_element = etree.HTML(response.text)
        conten_url = html_element.xpath('//div[@class="clearfix dirconone"]/li')
        for i in conten_url:
            req_url = i.xpath('.//a/@href')[0]
            content(req_url)

def content(req_url):
    a= {}

    response = qingqiu(req_url)
    response.encoding = 'gbk'
    if response.status_code == 200:
        print('aaj')

        html_element = etree.HTML(response.text)
        a['章节'] = html_element.xpath('//div[@class="bookInfo"]/h1/strong/text()')[0]
        conteht_1 = html_element.xpath('//div[@class="mainContenr"]/text()')
        for i in conteht_1:
            a['内容'] = str(i.replace(' ',''))
            print(i)
#             chucun(a)
#
#
# def chucun(a):
#     try:
#         client = MongoClient(host='localhost', port=27017)
#         db = client.quanshu
#         db.booke.insert_one(a)
#         print(a['章节'] + '写入成功')
#     except:
#         print(a['章节'] + '写入失败')






if __name__ == '__main__':
    url = 'http://www.quanshuwang.com/'

    list = fenlei(url)
    xiangqing_url(url)

    pool = pool.Pool(3)
    for list_url in list:

        gevent.joinall(
            [
                pool.spawn(xiangqing_url, list_url)
            ]
        )



