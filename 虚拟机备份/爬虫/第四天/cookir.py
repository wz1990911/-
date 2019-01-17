#处理cookie;
#会用到cookiejar库用来构建cookiejar对象存储cookie#
#好人和HTTPCookieProcessor处理器;用来管理cookiejar对象,斌构建一个handler处理器
#cookiejar库中报刊Cookiejar/FileCookirjar.MozillaXookiejar,LWPCookiejar
#cookiejar;用来管理Http的cookies值,起到cookies数据,将数据都储存在内存中
#一点cookiejar实例进行了垃圾回收,这样的话,我们的cookies就不存在了

#MozillaCookiejar;用来管理和储存cookies的,cookies数据可以写入本地文件
from urllib import request
from http import cookiejar
#创建一个cookiejar对象来储存cookies信息

cookies_jar= cookiejar.CookieJar()
#穿件一个HTTPCokieProcess处理对象
cookie_hander = request.HTTPCookieProcessor(cookiejar=cookies_jar)

#自定以opener
opener = request.build_opener(cookie_hander)


#根据opener.opener发起请求

# url = 'https://www.baidu.com'
# response = opener.open(url)
# print(cookies_jar)
# print(type(cookies_jar))
# cookie_str = ' '
#
# for cookie in cookies_jar:
#     print('name:',cookie.name)
#     print('value:',cookie.value)
#     cookie_str = cookie_str  + cookie.name+'='+cookie.value+'; '
# cookie_str = cookie_str[0:-2]
# print(cookie_str)
#
# opener.open('')





