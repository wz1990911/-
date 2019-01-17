# from bs4 import BeautifulSoup

# 目标url:
# 第一页
# https://www.autohome.com.cn/all/1/
# 第二页
# https://www.autohome.com.cn/all/2/
# 第三页
# https://www.autohome.com.cn/all/3/
# 第四页
# https://www.autohome.com.cn/all/4/

import requests
from bs4 import BeautifulSoup
import re


def qczjSpider(req_url):
    get_qcnoval_list_by_url(req_url)


def get_qcnoval_list_by_url(req_url):
    '''
    根据url获取文章的列表
    req_url:每一个分页的url地址

    '''
    req_header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
    }

    response = requests.get(url=req_url, headers=req_header)
    if response.status_code == 200:
        # 请求成功解解析数据
        # 将获取到的页面源码写入本地对比是否获取到了真实数据
        # 并且有助于分析网页结构
        # with open('qichezhijia.html','w') as file:
        #     file.write(response.text)

        # 首先创建一个soup对象
        # lxml:说明使用的是lxml.html解析器(速度快，容错性也比较高)
        # html.parser:python自带的html解析器
        html_soup = BeautifulSoup(response.text, 'html.parser')
        # html_soup.prettify():可以将html源码格式化输出，
        # print(html_soup.prettify())

        # 查找符合条件的第一个节点
        # html_soup.find()
        # 查找符合条件的所有节点
        '''
        name=None:可以是一个字符串，可以是一个列表，正则表达式 (标签的名称)
        attrs={}:是一个字典，(标签的属性)
        text=None:是个字符串，列表，正则表达式  (会查找出所有跟text文本一致的内容)
        '''
        # html_soup.find_all('li'):查找所有的li标签 字符串
        # html_soup.find_all(['li','a']):查找所有的li和a标签  列表
        # html_soup.find_all(re.compile('^b')) 查找出所有符合正则表达式的标签 正则表达式
        # 根据类找
        # html_soup.find_all(name='ul',attrs={'class':'article'})
        # 根据id找
        # html_soup.find_all(name='ul', attrs={'id': 'Ul1'})
        # print(type(html_soup))
        # <class 'bs4.BeautifulSoup'> 对象能使用find_all方法
        soup_ul = html_soup.find_all(name='ul', attrs={'class': 'article'})[0]
        # print(soup_ul)
        # print(type(soup_ul))
        # <class 'bs4.element.ResultSet'> 不能使用find_all方法
        # soup_ul = soup_ul.find_all('li')
