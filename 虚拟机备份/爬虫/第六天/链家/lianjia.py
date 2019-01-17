import requests
import json
import pymysql
from lxml import etree
import re




def wz_zufang(req_url):
    req_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
    }
    # 发起请求
    response = requests.get(url=req_url, headers=req_headers)

    if response.status_code == 200:
        html_element = etree.HTML(response.text)
        #获取ul下的li
        noval_lis = html_element.xpath('//ul[@class="house-lst"]/li')
        content = {}
        for wz_li in noval_lis:
            # 封面图片
            if len(wz_li.xpath('./div[@class="pic-panel"]/a/img/@data-img'))>0:
                # print(wz_li)
                content['wz图片'] = wz_li.xpath('./div[@class="pic-panel"]/a/img/@data-img')[0]
            else:
                content['wz图片'] = "暂无图片"
            # print(content['wz图片'])

            #标题
            content['wz标题']=wz_li.xpath('./div[@class="info-panel"]/h2/a/text()')[0]
            #地点
            content['wz地点'] = wz_li.xpath('.//span[@class="region"]/text()')[0]

            #样式
            content['wz样式'] = wz_li.xpath('.//span[@class="zone"]/span/text()')[0]
            #平米
            content['wz平米'] = wz_li.xpath('.//span[@class="meters"]/text()')[0]
            #方向
            content['wz方向'] = wz_li.xpath('.//div[@class="where"]/span[last()]/text()')[0]
            #房东
            content['wz房东'] = wz_li.xpath('.//div[@class="con"]/a/text()')[0]
            #楼层
            content['wz楼层']= wz_li.xpath('.//div[@class="con"]/text()')[0]
            #优势
            content['wz优势'] = wz_li.xpath('.//div[@class="view-label left"]/span/span/text()')
            #月租
            content['wz月租'] = wz_li.xpath('.//div[@class="price"]/span/text()')[0]

            #看房
            content['wz看房'] = wz_li.xpath('.//div[@class="square"]/div/span/text()')[0]

            cunchu(content)
        # 构建下一页）
        pattern = re.compile('.*?pg(\d+)', re.S)
        # 匹配出当前页的页码
        result = re.findall(pattern, req_url)
        print('当前页码'+result)
        current_page = result[0]
        # print(current_page)
        # 构造下一页页码
        next_page = int(current_page)+1
        # print(next_page)
        #
        pattern = re.compile('pg\d+', re.S)
        next_url = re.sub(pattern, 'pg' +
                          str(next_page),
                          req_url)

        wz_zufang(next_url)
def cunchu(contnt):
    # 创建数据库
    client = pymysql.Connect('localhost', 'root', '1', 'zufang', charset='utf8')
    # 创建游标
    cursor = client.cursor()
    sql = '''
       INSERT INTO zufang(%s)
       VALUES (%s)
       ''' % (
        ','.join(contnt.keys()),
        ','.join(['%s'] * len(contnt))
    )

    print('正在存储')
    try:

        cursor.execute(sql, list(contnt.values()))

        client.commit()
    except Exception as err:
        print(err)
        client.rollback()


if __name__ == '__main__':
    req_url = 'https://bj.lianjia.com/zufang/pg1/'
    wz_zufang(req_url)
