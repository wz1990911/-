import requests

# 获取cookie

req_url = 'http://www.baidu.com/'
req_header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

response =requests.get(url=req_url,headers=req_header)
cookies = response.cookies
#获取cookies
print(type(cookies))
#将RequestsCookieJar转换为一个字典
cookies_dict = requests.utils.dict_from_cookiejar(cookies)
print(type(cookies_dict))
print(cookies_dict)
#发起请求携带cookies参数
#get请求中cookies参数;可以是一个字典类型的数据一额可以是一个cookiejar对象
response =requests.get(url=req_url,headers=req_header,cookies=cookies_dict)