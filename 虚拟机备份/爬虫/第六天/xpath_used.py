#使用xpath语法提取数据
#什么是xpath?:是一门在xml文档中提取信息数据的语言
#可以用来在xml文档中对元素(标签)的属性进行遍历
#xml:是一个可扩展的标记语言,语法和我们的html相似,
#里面的节点可以自己定义,被设计的目的用来进行数据的传递和保存
#lxml
#pip3 install lxml

#以起点网为例
#notename : 查找出html多有标签名为notename的节点
#/:表示从根节点开始查找(相对性的)
#//:从任意位置匹配出你想要的节点
#.:选取当前节点
#..:选取当前父节点
#@ : 表示选择属性
#text():标签文本内容
#notename[1]:取出标签名为notename第一个节点
#notename[last()]   取出标签名为notename最后一个
#notename[last()-1]   取出标签名为notename倒数第二
import requests
from lxml import etree
import re
import json



def qidianSpider(start_url):

    get_noval_list_by_url(start_url)


def get_noval_list_by_url(req_url):
    '''
    根据分页的url获取分页的页面源码提取小说的信息
    req_url:表示每一个分页的url
    '''
    req_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
    }
    # 发起请求
    response = requests.get(url=req_url, headers=req_headers)
    if response.status_code == 200:
        #提取小说信息
        #使用etree.HTML方法可以见html文档源码转为一个element对象,
        #然后才能使用xpath语法
        html_element =etree.HTML(response.text)
        # div = html_element.xpath('/html/body/div[@class="share-img"]')
        # div = html_element.xpath('//div[@class="share-img"]/img/@src')[0]
        #提取小说列表
        noval_lis = html_element.xpath('//ul[@class="all-img-list cf"]/li')
        # print(len(noval_lis))
        # print(noval_lis)
        for noval_li in noval_lis:
            #封面图片
            coverImage = noval_li.xpath('./div[@class="book-img-box"]/a/img/@src')[0]
            # coverImage = noval_li.xpath('./div[@class="book-img-box"]//img/@src')[0]
            #标题
            title = noval_li.xpath('./div[@class="book-mid-info"]/h4/a/text()')[0]
            #详情url
            xiangqing = noval_li.xpath('./div[@class="book-mid-info"]/h4/a/@href')[0]
            author= noval_li.xpath('.//a[@class="name"]/text()')[0]
            fenlei = noval_li.xpath('.//p[@class="author"]/a[last()-1]/text()')[0]
            fenlei_1 = noval_li.xpath('.//p[@class="author"]/a[last()]/text()')[0]
            jianjie = noval_li.xpath('.//p[@class="intro"]/text()')[0].replace(' ','')

            # print(coverImage,title,author,fenlei,fenlei_1)
            # print(xiangqing)

            req_url = 'https:'+ xiangqing + '#Catalog'
        naxt = html_element.xpath('//a[@class="lbf-pagination-next "]/@href')[0]
        mulu(req_url)
        url = 'https:'+naxt
        get_noval_list_by_url(url)
def mulu(req_url):
    pattern = re.compile(
        '\d+'
    )
    result = re.findall(pattern, req_url)[0]
    url = 'https://book.qidian.com/ajax/book/category?_csrfToken=IiqTByCQkNgRGIpJfsun8sN6Rw4lrC9ImRsKH43s&bookId=' + str(
        result)
    # print(url)
    req_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
    }
    # 发起请求
    # params:字典类型的参数，存放的是get请求后拼接的参数
    response = requests.get(url=url, headers=req_headers)

    if response.status_code == 200:
        # print(response.text)
        result = response.text.decode('utf-8')
        result = json.loads(result)
        print(result)

        # movie_info = data['data']['vs'][0]['cs']
        # # print(movie_info)
        # for i in movie_info:
        #     name = i['cN']
        #     req_url = i['cU']
        #     print(name,req_url)






if __name__ == '__main__':
    statt_url ='https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=1'

    qidianSpider(statt_url)