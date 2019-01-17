from urllib import request
from urllib.parse import urlencode
import json
req_url = 'https://www.lagou.com/jobs/positionAjax.json?px=new&needAddtionalResult=false'

def lagouSpidr():
    keyword = 'java'
    #构建url发起请求
    req_url = 'https://www.lagou.com/jobs/positionAjax.json?px=new&needAddtionalResult=false'

    for pagenum in range(30):
        #构建post请求数据
        form_data = {
            'first':'false',
            'pn':1,
            'kd':keyword
        }

        #将表单转为url编码格式的二进制数据
        data_trandfrom = urlencode(form_data).encode('utf-8')

        req_header={
            'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
            'Referer':'https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput='
        }
        req = request.Request(url=req_url,data=data_trandfrom,headers=req_header)
        #发起请求
        response = request.urlopen(req)
        #做一个判断请求成功在这里做数据处理
        print(response.status)
        if response.status == 200:
            #print(response.read().decode('utf-8'))
            parse_data(response.read().decode('utf-8'))



def parse_data(text):
    #分析发现返回的结果为json字符串
    #1需要将json字符串,转换为python字符串
    result = json.loads(text)
    postionResult = result['content']['positionResult']['result']
    print(len(postionResult))
    for postion in postionResult:
        postion_dict={}
        postion_dict['companyFullName']  =  postion['companyFullName']
        postion_dict['formatCreateTime']  =  postion['formatCreateTime']

        json_str = json.dumps(postion_dict,ensure_ascii=False)

        #文件读写
        #w写入,如果没有则写入,如果没有则覆盖
        #w+;读写模式
        #wb:写入二进制数据,如果没有则写入,如果有则覆盖
        #a:追加,从末尾追加
        #a+:追加并具有读写模式
        #ab:追加二进制数据
        with open('lagou.json','a')as file:
            file.write(json_str+'\n')



    print(type(result))
if __name__ == '__main__':
    lagouSpidr()





