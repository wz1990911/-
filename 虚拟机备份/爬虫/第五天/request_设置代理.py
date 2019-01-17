
import requests
# #设置代理
# #构建一个字典.将我么您的代理放到字典里
# proxy = {
#     'http':'58.53.128.83:3128',
#     'https':'120.69.82.110:44693'
#
# }
#
url= 'http://httpbin.org/get'
# #将代理参数赋值
# response = requests.get(url=url,proxies=proxy)
# print(response.text)


#对于一些私密代理需要账号密码验证
proxy = {
    'http':'username:pwd@ip:post',
    'https':'username:pwd@ip:post',
}
response = requests.get(url=url,proxies=proxy)
print(response.text)