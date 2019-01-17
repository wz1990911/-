#使用urllib发起一个post请求
from urllib import request
from urllib.parse import urlencode

#目标url
#可以从响应结果中看到你发送给对方服务器毒参数
req_url = 'https://httpbin.org/post'


#构造一个表单数据
formdata= {
    'name':'行开',
    'age':'17',
    'gender':'男',
    'class':'1805',
}


#数据经过两步处理
#1.需要将表单数据转化为url编码格式(urlencoding)
#2.将装换后的字符串在转为二进制数据(encode)
data_tranfrom = urlencode(formdata).encode('utf-8')
print(data_tranfrom)


#发送请求如果不需要请求头
response = request.urlopen(url=req_url,data=data_tranfrom)


#状态码
print(response.status)

#获取响应的响应体
print(response.read().decode())