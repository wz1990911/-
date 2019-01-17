import requests
import re
from lxml import etree
from pyquery import PyQuery as pq
import json
from pymongo import MongoClient


class dangdangwang(object):


    def chuanshu(self,req_url):
        req_headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
        }
        # 发起请求
        response = requests.get(url=req_url, headers=req_headers)
        return response


    def dangdang_list3(self,req_url):
        response = self.chuanshu(req_url)
        if response.status_code == 200:
            html_element = etree.HTML(response.text)

            # 获取列表页url
            div = html_element.xpath('//div[@name="m403752_pid5374_t9144"]/div/div/div/dl')
            for dl in div:
                name = dl.xpath('./dt/a/text()')[0].replace(' ', '')
                name_href = dl.xpath('./dd/a/@href')
                url_href = []
                for i in name_href:
                    # 获取到列表url修改下方便构建下一页
                    a = i.replace('cp', 'pg1-cp')
                    self.xiangqing(a)



    def xiangqing(self,req_url):

        response = self.chuanshu(req_url)
        if response.status_code == 200:
            # print(response.text)

            # 根据列表页获取详情页
            html_element = etree.HTML(response.text)
            # print(html_element)
            xiangqing_ul = html_element.xpath('//div[@ddt-area="451680112840"]/div//li/a/@href')
            for i in xiangqing_ul:
                self.xianxi(i)
            #构建下一页
            count_url = response.url
            pattern = re.compile(
                '.*?pg(\d+).*?', re.S
            )
            current_start = re.findall(pattern, count_url)[0]
            next_start = int(current_start) + 1
            pattern = re.compile('pg(\d+)')
            if next_start < 101:
                next_url = re.sub(pattern, 'pg' + str(next_start), count_url)
                # print(next_url)
                self.xiangqing(next_url)



    def xianxi(self,req_url):
        ddd ={}
        response = self.chuanshu(req_url)
        if response.status_code == 200:
            html_element = etree.HTML(response.text)
            #二级分类
            ddd['二级分类'] = html_element.xpath('.//div[@class="breadcrumb"]/a/text()')[0]
            #三级级分类
            ddd['三级分类'] = html_element.xpath('.//div[@class="breadcrumb"]/a/text()')[1]
            #封面图片
            ddd['封面图片'] = html_element.xpath('//div[@class="pic_info"]/div/a/img/@src')[0]
            #名字
            ddd['名字'] = html_element.xpath('//div[@class="name_info"]/h1/@title')[0]
            #简介
            ddd['简介'] = html_element.xpath('//div[@class="name_info"]/h2/span/@title')[0]
            #作者
            ddd['作者'] = html_element.xpath('//div[@class="messbox_info"]/span/a/text()')[0]
            #出版社
            ddd['出版社'] = html_element.xpath('//div[@class="messbox_info"]/span[@ddt-area="003"]/a/text()')[0]
            #出版时间
            ddd['出版时间'] = html_element.xpath('//div[@class="messbox_info"]/span[last()]/text()')[0]
            ddd['评论'] = html_element.xpath('//div[@class="pinglun"]/span[2]/a/text()')[0]

            # http://product.dangdang.com/index.php?r=callback%2Fget-bang-rank&productId=
            #拼接排名url
            url = re.compile('.*?//.*?/(.*?).html')
            paiming = re.findall(url,req_url)[0]
            pai_url = 'http://product.dangdang.com/index.php?r=callback%2Fget-bang-rank&productId='+str(paiming)
            response = self.chuanshu(pai_url)

            if response.status_code == 200:
                try:

                    if len(response.text) > 0:
                        data = json.loads(response.text)
                        ddd['排名']=data['data']['rank']
                except:
                    print('暂无排名')
            # 拼接价格url
            url = re.compile('.*?//.*?/(.*?).html')
            jiage = re.findall(url, req_url)[0]
            jia_url = 'http://product.dangdang.com/index.php?r=callback%2Fproduct-info&productId='+str(paiming)+'&isCatalog=0&shopId=0&productType=0'
            response = self.chuanshu(jia_url)
            if response.status_code == 200:
                xianjia = json.loads(response.text)
                try:
                    if len(xianjia['data']['spu']['promotion']['p102']['price']['directPrice']) > 0:
                        ddd['价格'] = xianjia['data']['spu']['promotion']['p102']['price']['directPrice']
                except:
                    ddd['价格'] = html_element.xpath('//div[@id="pc-price"]/div/p[2]/text()')[1]
            ddd['人气'] = html_element.xpath('//div[@class="share_div clearfix"]/a/text()')[0]
            self.chucun(ddd)
    def chucun(self,ddd):
        try:
            client = MongoClient(host='localhost', port=27017)
            db = client.dangdang
            db.stu.insert_one(ddd)
            print(ddd['名字'] + '写入成功')
        except:
            print(ddd['名字'] + '写入失败')

if __name__ == '__main__':
    dangdang = dangdangwang()
    req_url = 'http://book.dangdang.com/'
    dangdang.dangdang_list3(req_url)












