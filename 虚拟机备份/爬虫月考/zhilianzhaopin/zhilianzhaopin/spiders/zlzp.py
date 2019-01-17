# -*- coding: utf-8 -*-
import scrapy
import json
from zhilianzhaopin.items import ZhilianzhaopinItem, Zhilianzhaopin_dataItem
import re

class ZlzpSpider(scrapy.Spider):
    name = 'zlzp'
    allowed_domains = ['zhaopin.com']
    start_urls = [
        'https://fe-api.zhaopin.com/c/i/sou?start=60&pageSize=60&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&_v=0.30011246&x-zp-page-request-id=552209489e0e4801b937abd1d7c9f9b1-1544679828231-104477']

    # https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&_v=0.98217538&x-zp-page-request-id=7c7a9a23903b4d79b7b0268ab52b865c-1544679546354-17427
    # https://fe-api.zhaopin.com/c/i/sou?start=60&pageSize=60&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&_v=0.98217538&x-zp-page-request-id=7c7a9a23903b4d79b7b0268ab52b865c-1544679546354-17427

    def parse(self, response):
        item = ZhilianzhaopinItem()

        shuju = json.loads(response.text)['data']['results']
        for i in shuju:

            # 标题
            item['wz_title'] = i['jobName']
            # 工资
            item['wz_gongzi'] = i['salary']
            # 地址
            item['wz_dizhi'] = i['city']['display']
            # 年龄
            item['wz_nianling'] = i['workingExp']['name']
            # 学历
            item['wz_xueli'] = i['eduLevel']['name']
            # 待遇
            if len(i['welfare']) > 0:
                item['wz_daiyu'] = i['welfare']
            else:
                item['wz_daiyu'] = '暂无'
            # 公司名称
            item['wz_mingzi'] = i['company']['name']
            # 企业类型
            item['wz_qiyeleix'] = i['company']['type']['name']
            # 人数规模
            item['wz_guimo'] = i['company']['size']['name']
            # 状态
            item['wz_zhuangtai'] = i['timeState']
            yield item
            url = i['company']['url']

            yield scrapy.Request(url, callback=self.gongsixingq)
        pattern = re.compile('pageSize=(\d+)')
        result = re.findall(pattern, response.url)[0]
        num = int(result) + 60

        urll = 'https://fe-api.zhaopin.com/c/i/sou?pageSize=' + str(
            num) + '&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&_v=0.60193457&x-zp-page-request-id=9053d92ba8e6494f80bd1615536a371b-1544680916594-675614'
        yield scrapy.Request(urll, callback=self.parse)

    def gongsixingq(self, response):
        item = Zhilianzhaopin_dataItem()

        if len(response.xpath('//h1[@class="detail-info__title__txt"]/text()').extract_first('')) > 0:
            # 公司名字
            item['wz_gs_name'] = response.xpath('//h1[@class="detail-info__title__txt"]/text()').extract_first('')
            # 公司信息
            gs = []
            xinxi = response.xpath('//div[@class="detail-info__main__number clearfix"]/span')
            for i in xinxi:
                gs_xinxi = ''.join(i.xpath('./text()').extract())
                gs.append(gs_xinxi)
                item['wz_gs_xinxi'] = ','.join(gs)
            # 公司url
            item['wz_gs_url'] = response.xpath('//p[@class="company-info__detail-info__url"]/a/@href').extract_first('')
            # 公司信息介绍
            item['wz_gs_jieshao'] = ''.join(response.xpath('//p[@class="MsoNormal"]/span/text()').extract()).replace(
                '\n', '').replace('\r', '')
            yield item

