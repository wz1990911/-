# urlopen方法只能够实现简单的get或者post请求
# 如果设计到cookie和代理urlopen方法就不支持了
# 这是我们需要自定义handle处理器和opener对象

from urllib import request
import ssl

# request.urlopen()

# 假设出现了证书问题，我们要忽略证书错误
context = ssl._create_unverified_context()

# 创建一个httpshandler,支持发起https请求
# debuglevel设置为１：可以将收报和发包的报头打印出来
https_handler = request.HTTPSHandler(debuglevel=1, context=context)
# 实例化一个opener对象
opener = request.build_opener(https_handler)

# 使用opener.open()方法发起请求
response = opener.open('https://www.baidu.com/')
print(response.status)

# install_opener可以将自定义的opener对象设置为全局的opener
request.install_opener(opener)
# 下次再调用request.urlopen()方法的时候,使用的opener就是你设置的全局opener
request.urlopen()
