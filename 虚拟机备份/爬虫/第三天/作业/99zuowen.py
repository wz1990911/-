from urllib import request
from urllib.parse import urlencode
import re
import os

class zuowen_99 (object):
    def fenlei(self):
        req_url = 'https://www.99zuowen.com/xiaoxuezuowen/ynjzuowen/'
        req_header = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
        }
        # 构建一个request请求对象
        req = request.Request(url=req_url, headers=req_header)
        # 发起请求
        response = request.urlopen(req)
        # 打印状态码
        print(response.status)
        # 如果请求成功
        if response.status == 200:
            yuanma = response.read().decode('utf-8')
            # pattern = re.compile('<div\sclass="xbt"><i\sclass="line_bt">.*?title="更多".*?<div\sclass="banner clearfloat">',re.S)
            # biaoqian = re.findall(pattern,response.read().decode('utf-8'))
            pattern = re.compile('<div\sclass="xbt">.*?<span.*?>.*?<a.*?href="(.*?)".*?>.*?<h3>(.*?)</h3>',re.S)
            content = re.findall(pattern,yuanma)
            print(content[1])
            for i in content:
                dirpath = '99作文/'+i[1]
                if not os.path.exists(dirpath):
                    os.mkdir(dirpath)

                req_url = i[0]
                if 'https://www.99zuowen.com' not in req_url:
                    req_url = 'https://www.99zuowen.com' + req_url
                    self.huoqu(req_url,dirpath)
    def huoqu(self,req_url,dirpath):
        req_headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        }
        print('正在请求' + req_url)
        # 构建request对象
        req = request.Request(req_url, headers=req_headers)
        # 发起请求
        response = request.urlopen(req)
        if response.status == 200:
            html = response.read().decode('utf-8')
            pattern = re.compile('<li\sclass="lis">.*?<a.*?href="(.*?)".*?>(.*?)</a>', re.S)
            zuowen_list = re.findall(pattern, html)
            print(zuowen_list)

            for zuowen in zuowen_list:
                print('正在获取' + zuowen[1])
                self.huoqu_1(zuowen[0], dirpath)
    def huoqu_1(self,req_url,dirpath):
        req_headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        }
        print('正在请求' + req_url)
        # 构建request对象
        req = request.Request(req_url, headers=req_headers)
        # 发起请求
        response = request.urlopen(req)
        if response.status == 200:
            # print(response.read().decode('utf-8'))
            html = response.read().decode('utf-8')
            # 空字典，一会存放提取的作文数据
            content_nr = {}
            # 提取作文详情中的作文数据
            pattern1 = re.compile(
                '<div.*?class="title">.*?<h1>(.*?)</h1>' +
                '.*?<div.*?>.*?<span>来源:.*?<a.*?>(.*?)</a>' +
                '.*?<span>(.*?)</span>' +
                '.*?<span>(.*?)</span>'
                , re.S
            )
            info = re.findall(pattern1, html)[0]
            content_nr['标题'] = info[0]
            content_nr['来源'] = info[1]
            content_nr['作者'] = info[2]
            content_nr['发布时间'] = info[3]

            pattern2 = re.compile('<div\sclass="content">.*?<div\sclass="article_page">', re.S)
            div_content = re.findall(pattern2, html)[0]

            pattern3 = re.compile('<p>(.*?)</p>', re.S)
            content = ';'.join(re.findall(pattern3, div_content))
            content_nr['内容'] = content

            print(content_nr)
            self.chucun(content_nr,dirpath)
    def chucun(self,content_nr,dirpath):
        filename = dirpath + '/' + content_nr['标题']

        with open(filename, 'w') as file:
            file.write(
                '标题：' + content_nr['标题'] + '\n' +
                '来源:' + content_nr['来源'] + '\n' +
                content_nr['作者'] + '\n' +
                '发布时间：' + content_nr['发布时间'] + '\n' +
                content_nr['内容']
            )

            #https://www.99zuowen.com/xiaoxuezuowen/ynjxieren/
            #https://www.99zuowen.com/xiaoxuezuowen/ynjxieshi/
if __name__ == '__main__':
    a = zuowen_99()
    a.fenlei()