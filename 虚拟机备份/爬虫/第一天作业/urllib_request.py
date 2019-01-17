#如果要添加请求就要添加request对象
from urllib import request

#设置请求头信息
#常见的请求头参数一般有三个:User_Agent, refere,cookie,
# req_headers = (
#     'User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
# )

#使用第三方库随机

from fake_useragent import UserAgent
ua = UserAgent()


#随机一个浏览器的User-Agent
user_agent = ua.random

req_headers={
    'User-Agent':user_agent,
}



req_url = 'http://www.eduxiao.com/zuowen1/'
#根据请求头创建一个request对象
# url:要求请的目标url
# data = None 如果是None,表示为一个get请求,反之位post请求
# headers = {} 设置请求头参数,对应是个字典类性的数据
# method = None 设置请求方式get或post
req = request.Request(url=req_url,headers=req_headers,method='GET')
#以另一种方式添加请求头
req.add_header('Referer','http://www.eduxiao.com/')

#获取request对象请求头中设置的参数
refere = req.get_header('Referer')
print(refere)

response = request.urlopen(req)

print(response.status)