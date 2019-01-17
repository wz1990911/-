from urllib import  request,error
#1.要请求携带代理,我们必须创建一个handler代理处理器
#
#proxies:对应的是一个字典
proxy = {
    'http':'61.138.33.20:808',
    'https':'120.69.82.110:44693',
}
proxy_handler=request.ProxyHandler(proxies=proxy)


#根据proxy_handler代理处理器实例话一个opener对象
opener = request.build_opener(proxy_handler)


#使用opener的open方法发起请求
# url = 'https://www.baidu.com/'
#通过http://httpbin.org/get可以验证使用的代理
url = 'http://httpbin.org/get'
try:
    response = opener.open(url)
    print(response.status)
    print(response.read().decode('utf-8'))
except error.HTTPError as err:
    print(err.reason)
except error.URLError as err:
    print(err.reason)




