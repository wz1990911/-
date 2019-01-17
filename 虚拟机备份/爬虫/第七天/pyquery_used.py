#pyqyery:相当于jquery的python版本实现他同样可以事项提取html页面的节点
#获取节点的属性和文本
#pip3 install pyqyery
from pyquery import PyQuery as pq
from lxml import etree
from urllib import parse
import json
#第一步构建一个pyqueryduixiang
# html_pq = pq('html文本')
# #传入lxml
# html_pq = pq(etree.fromstring('html文本'))
#
# #可以直接传如一个url
# html_pq = pq(url='')
# #传入文件
# pq = pq(filename = '文件名称')

'''
.html():获取某个HTML代码
.text():获取标签文本内容
.(selector):根据css选择器获取目标节点
.eq（index）：根据索引获取制定标签（节点）
.find（）查找子节点
.filter（）根据class,id过滤节点
.attr('属性名‘）：获取节点的属性值

'''

#第一页url
# https://hr.tencent.com/position.php
import requests

def tencent_spider(start_url):
    get_job_list_by_url(start_url)



def get_job_list_by_url(req_url):
    '''
    根据分页url
   获取职业列表

    '''
    req_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
    }
    # 发起请求

    response = requests.get(url=req_url, headers=req_headers)

    if response.status_code == 200:
        # 构建一个跑去兑现
        html_pq = pq(response.text)
        #tr_even = html_pq('tr').filter('.even')
        tr_even = html_pq('tr.even')
        # tr_odd = html_pq('tr').filter('odd')
        tr_odd = html_pq('tr.odd')
        jobs = tr_even+tr_odd
        print(type(jobs))
        #PyQuer对象不是一个可迭代对象
        #如果要遍历需要加items()
        for tr in jobs.items():
            #拿到后提取先要的信息
            #使用text（）目的是获取标签文本
            title = tr('td.l.square a').text()
            #获取标签属性
            url= tr('td.l.square a').attr('href')
            # print(url)
            #获取职位类型
            #.eq(1):根据索引取标签
            tags = tr('td').eq(1).text()
            #人数
            renshu = tr('td').eq(2).text()
            print('人数：'+renshu)
            #地址
            address = tr('td').eq(3).text()
            print("地址："+address)
            #时间
            time = tr('td').eq(4).text()
            print("时间:"+time)

        #下一页
        # next = etree.HTML(response.text)
        # xyy = next.xpath('//div[@class="pagenav"]/a[last()]/@href')
        next = pq(response.text)
        xyy = next('#next').attr('href')
        url = parse.urljoin(req_url,xyy)
        xiangqing(url)


def xiangqing(req_url):
    req_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
    }
    # 发起请求

    response = requests.get(url=req_url, headers=req_headers)

    if response.status_code == 200:
        html_pq = pq(response.text)
        9







        # print(type(html_pq))



if __name__ == '__main__':
    start_url = 'https://hr.tencent.com/position.php?&start=0'
    tencent_spider(start_url)