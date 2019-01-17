from urllib import request
from urllib.parse import urlencode
import json
import time
from pymysql import  *
def douban():

    req_url = 'https://movie.douban.com/j/search_tags?type=movie&source='
    req_header = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
    }

    req = request.Request(url=req_url,headers=req_header)
    response = request.urlopen(req)
    print(response.status)
    json_str = response.read().decode('utf-8')
    json_1 = json.loads(json_str)
    print(json_1)
    postionResult = json_1['tags']
    print(postionResult)
    for postion in postionResult:
        postion = {
            'tag':postion
        }
        content(postion)


def content(postion):
    str1 = urlencode(postion)
    a = int(input('请输入你要查的篇数'))
    #标签下都有什么内容
    #yag = 内容
    #sort
    #https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=time&page_limit=20&page_start=0
    #https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=20&page_start=0
    for i in range(1,a+1):
        req_url = 'https://movie.douban.com/j/search_subjects?type=movie&'+str1+'&sort=time&page_limit=20&page_start=' + str((i + 1) * 20)
        req_header = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
        }
        req = request.Request(url=req_url, headers=req_header)
        response = request.urlopen(req)
        if response.status == 200:
            result = json.loads(response.read().decode('utf-8'))
            content = result['subjects']
            for i in content:
                b = i['id']
                xq(b)

def xq(b):
    req_url = 'https://movie.douban.com/j/subject_abstract?subject_id=' +str(b)
    req_header = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
    }
    req = request.Request(url=req_url, headers=req_header)
    response = request.urlopen(req)
    if response.status == 200:
        result = json.loads(response.read().decode('utf-8'))
        a = result['subject']


        Mysql(a)


def Mysql(a):
    #名字
    title = a['title']

    # 分钟
    duration = a['duration']

    # 地区
    region = a['region']

    # 类别
    types = str(a['types'])

    #状态
    playable =str(a['playable'])

    #评分
    rate = a['rate']

    # 演员
    actors = str(a['actors'])

    #封面图片
    url = a['url']

    #简介
    content = a['short_comment']['content']
    #创建Connection连接
    conn = connect(host='localhost', port=3306, database='pachong', user='root', password='1', charset='utf8')
    # 获得Cursor对象
    cs1 = conn.cursor()

    count = cs1.execute('insert into pachong(名称,时长,地区,类别,状态,评分,演员,封面图片,简介) VALUES("{}","{}","{}","{}","{}","{}","{}","{}","{}")'.format(
        title,duration,region,types,playable,rate,actors,url,content ))

    conn.commit()
    # 关闭Cursor对象
    cs1.close()
    # 关闭Connection对象
    conn.close()
    print('存入成功')
    time.sleep(5)








if __name__ == '__main__':

    douban()