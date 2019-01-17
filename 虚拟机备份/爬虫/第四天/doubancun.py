from http import cookiejar
#将cookies数据保存到自定文件下
from urllib import  request
filename = 'doubancookies.text'

#实例画一个MozillaCookieJar对象
mz_cookiejar = cookiejar.MozillaCookieJar(filename)



#构建一个HTTPCookieProcessor对象来管理cookiejar
cookiejar_handler = request.HTTPCookieProcessor(mz_cookiejar)


#自定义opener
opener = request.build_opener(cookiejar_handler)


#使用自定义的opener发起请求