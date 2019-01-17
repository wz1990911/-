#http://www.eduxiao.com/zuowen1/
#http://www.eduxiao.com/zuowen1/list_1_2.html


#二年级
#http://www.eduxiao.com/zuowen2/
#http://www.eduxiao.com/zuowen2/list_2_2.html
#http://www.eduxiao.com/zuowen2/list_2_3.html

#三年级
#http://www.eduxiao.com/zuowen3/
#http://www.eduxiao.com/zuowen3/list_3_2.html
#http://www.eduxiao.com/zuowen3/list_3_3.html


#写人作文
#http://www.eduxiao.com/xeiren/
#http://www.eduxiao.com/xeiren/list_8_2.html
#http://www.eduxiao.com/xeiren/list_8_3.html

#小学生
#http://www.eduxiao.com/riji/
#
#
from urllib import request
from  urllib.parse import urlencode
import re
import os


class EduxiaoSpider(object):
    def __init__(self):
        pass


    def start_spider(self):
        #根据每一个分类的分页地址获取作文列表
        start_url = [
            'http://www.eduxiao.com/zuowen1/list_1_1.html',
            'http://www.eduxiao.com/zuowen2/list_2_1.html',
            'http://www.eduxiao.com/zuowen3/list_3_1.html',
            'http://www.eduxiao.com/zuowen4/list_4_1.html',
            'http://www.eduxiao.com/zuowen5/list_5_1.html',
            'http://www.eduxiao.com/zuowen6/list_6_1.html',
            'http://www.eduxiao.com/xeiren/list_8_1.html',
            'http://www.eduxiao.com/riji/list_9_1.html',
        ]
        for req_url in start_url:
            req_header = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
            }

            # 构建一个request请求对象
            req = request.Request(url=req_url, headers=req_header)
            # 发起请求
            response = request.urlopen(req)

            if response.status == 200:
                #请求成功,提取苏剧
                #step1,从url中提取分类,和当前url的页码
                pattern = re.compile('http://www.eduxiao.com/(.*?)/list_\d+_(\d+).html')
                result = re.findall(pattern,response.url)
                print(result)
                #获取分类
                tag = result[0][0]
                #获取当前分页页码
                current_page = result[0][1]
                #根据分类创建文件夹
                dirPath = 'xzw/'+tag
                if not os.path.exists(dirPath):
                    os.mkdir(dirPath)

                #提取数据
                #提取分页下的作文详情地址和标题
                #step1:先将整个文章列表的div块取出来
                pattern = re.compile('<div\sclass="listbox">.*?</div>',re.S)
                #数组越界IndexError: list index out of range

                div_html = re.findall(pattern,response.read().decode('gbk'))[0]
                pattern= re.compile('<li>.*?<a.*?href="(.*?)".*?class="title".*?>(.*?)</a>',re.S)
                zuowen_lsit = re.findall(pattern,div_html)
                print(zuowen_lsit)
                for zuowen in zuowen_lsit:
                    print('正在获取'+zuowen[1]+'详情数据')
                    zuowen_url = zuowen[0]
                    self.get_zuowen_datail_by_url(zuowen_url)
    #根据作文详情地址获取作文详情数据
    def get_zuowen_datail_by_url(self,req_url):
        '''
        req_url:作文闲情数据
        tag:分类
        '''
        req_header = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
        }

        # 构建一个request请求对象
        req = request.Request(url=req_url, headers=req_header)
        # 发起请求
        response = request.urlopen(req)

        if response.status == 200:
            #构建一个正则表达式对象,提取文章详情信息
            pattern = re.compile(
                '<div\sclass="title">.*?<h2>(.*?)</h2>'+
                '.*?</small>(.*?)<small>作者:</small>(.*?)'+
                '<small>来源:</small>(.*?)</div>',re.S)
            result = re.findall(pattern,response.read().decode('gbk'))
            article_info = {}
            print(result)
            article_info['title'] = result[0][0]
            article_info['time'] = result[0][1]
            article_info['autor'] = result[0][2]
            article_info['soure'] = result[0][3]

            #提取文章内容所在的div模块
            pattern = re.compile('<div\sclass="content">.*?</div>',re.S)
            div_content = re.findall(pattern,response.read().decode('gbk'))[0]
            pattern = re.compile('<p>(.*?)</p>',re.S)
            content = ';'.join(re.findall(pattern,div_content))
            article_info['content'] = content
            print(article_info)



if __name__ == '__main__':
    spoder = EduxiaoSpider()
    spoder.start_spider()