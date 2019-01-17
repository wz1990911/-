
import requests
import re
from urllib import parse
import pymysql
import json

#创建数据库
client = pymysql.Connect('localhost','root','1','qidian',charset='utf8')
#创建游标
cursor = client.cursor()


def qidianpider(req_url):
    #请求头
    req_headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
    }
    #发起请求
    #params:字典类型的参数，存放的是get请求后拼接的参数
    response = requests.get(url=req_url,headers=req_headers)

    if response.status_code == 200:

        # with open('page.html','w') as file:
        #     file.write(response.text)
        #根据正则提取想要的目标数据
        pattern = re.compile(
            '<div.*?book-img-box.*?<img.*?src="(.*?)">'+
            '.*?<h4>.*?<a.*?href="(.*?)".*?>(.*?)</a>'+
            '.*?<a.*?class="name".*?>(.*?)</a>'+
            '.*?<a.*?>(.*?)</a>'+
            '.*?<a.*?>(.*?)</a>'+
            '.*?<p.*?intro.*?>(.*?)</p>',
            re.S
        )
        result = re.findall(pattern,response.text)
        for i in result:
            # print(i[1])
            full_url = 'https:'+i[1]+'#Catalog'
            mulu(full_url)

def mulu(full_url):
    pattern = re.compile(
        '\d+'
    )
    result = re.findall(pattern,full_url)[0]
    # print(result)
    url = 'https://book.qidian.com/ajax/book/category?_csrfToken=IiqTByCQkNgRGIpJfsun8sN6Rw4lrC9ImRsKH43s&bookId='+str(result)
    # print(url)
    req_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
    }
    # 发起请求
    # params:字典类型的参数，存放的是get请求后拼接的参数
    response = requests.get(url=url, headers=req_headers)

    if response.status_code == 200:
        # print(response.text)
        result = response.content.decode('utf-8')
        data = json.loads(result)

        movie_info = data['data']['vs'][0]['cs']
        for i in movie_info:
            name =i['cN']
            req_url=i['cU']
            content(req_url,name)

def content(req_url,name):
    url = 'https://read.qidian.com/chapter/'
    req_url = url+req_url
    # print(req_url)
    req_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
    }
    # 发起请求
    # params:字典类型的参数，存放的是get请求后拼接的参数
    response = requests.get(url=req_url, headers=req_headers)

    if response.status_code == 200:
        result = response.text
        pattern = re.compile('<h3\sclass="j_chapterName">(.*?)</h3>.*?<div\sclass="read-content.*?>.*?(.*?)</div>',re.S)
        content = re.findall(pattern,result)
        pattern = re.compile('\n*\s*<p>*\u3000*</p>*',re.S)
        xiaoshuo = {}
        for i in content:
            xiaoshuo['目录'] = i[0]
            content =i[1]
            xiaoshuo['内容'] = re.sub(' ','',content).replace('<p>','').replace('\u3000','').replace('\n','')
        chucun(xiaoshuo)


def chucun(xiaoshuo):
    # 创建数据库
    client = pymysql.Connect('localhost', 'root', '1', 'xiaoshuo', charset='utf8')
    # 创建游标
    cursor = client.cursor()
    sql = '''
    INSERT INTO xiaoshuo(%s)
    VALUES (%s)
    ''' % (
        ','.join(xiaoshuo.keys()),
        ','.join(['%s'] * len(xiaoshuo))
    )

    print('正在存储')
    try:

        cursor.execute(sql, list(xiaoshuo.values()))

        client.commit()
    except Exception as err:
        print(err)
        client.rollback()

    # print(content_1)





if __name__ == '__main__':

    #找目标url
    #https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=1
    #https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=2
    #https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=3
    start_url = 'https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=1'
    qidianpider(start_url)