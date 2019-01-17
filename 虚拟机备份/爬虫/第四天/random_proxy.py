from urllib import request,error
import random
#构建一个代理池
proxy_list = [
    {'https':'121.69.13.242:53281'},
    {'https': '123.7.61.8:53281'},
    {'https': '58.240.7.195:32617'},
    {'https': '118.122.92.252:37901'},
    {'https': '117.64.225.1:808'},

]
#随机在列表中获取一个代理

proxy =random.choice(proxy_list)


#构建一个proxyhandler处理器对象
proxy_handler = request.ProxyHandler(proxies=proxy)
#自定义opener
opener = request.build_opener(proxy_handler)

url = 'https://httpbin.org/get'
try:
    response = opener.open(url)
    print(response.status)
    print(response.read().decode('utf-8'))
except error.HTTPError as err:
    print(err.reason)
except error.URLError as err:
    print(err.reason)





