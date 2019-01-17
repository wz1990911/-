from urllib import request
from http import cookiejar
from urllib import parse

#创建一个CookieJar对象用来存储cookies信息
cookie_jar = cookiejar.CookieJar()

#创建一个HTTPCookieProcess处理器对象
#cookiejar:该参数需要传递一个CookieJar对象
cookie_hander = request.HTTPCookieProcessor(cookiejar=cookie_jar)

#自定义opener
opener = request.build_opener(cookie_hander)

#根据opener.open方法发起请求
# 豆瓣登录接口
url = 'https://www.douban.com/accounts/login'

form_data = {
    'source': 'index_nav',
    'form_email': '17634060573',
    'form_password': 'wz990911',
}

#将字典中的参数转为url编码格式的二进制数据
post_data = parse.urlencode(form_data).encode('utf-8')

#添加一个请求头
req_header = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

#构建一个request对象
req = request.Request(url=url,headers=req_header,data=post_data)

#发起请求
response = opener.open(req)

if response.status == 200:
    #个人主页地址
    url = 'https://www.douban.com/people/187595671/'

    response = opener.open(url)

    html = response.read().decode('utf-8')

    with open('doubanpage.html','w') as file:
        print('成功获取到了个人主页数据')
        file.write(html)