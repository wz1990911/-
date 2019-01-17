import requests

url = 'https://www.sine.com/'

response = requests.get(url)
'''
    :param method: 请求方式
    :param url: 要发起请求的url
    :param params: get请求后面拼接的参数(字典类型)
    :param data: 发起post请求要传递的表单数据(字典类型)
    :param json: 同样是发起post请求时传奇的参数(json数据类型)
    :param headers: 请求头
    :param cookies: 发起请求携带cookies参数( Dict or CookieJar object) 
    :param files: 上传文件
    :param auth: 网页认证
    :param timeout: 设置请求超时时间
    :param allow_redirects: 设置是否允许重定向(bool值的类型)
    :type allow_redirects: bool
    :param proxies: 设置代理(字典型参数)
    :param verify: 是否忽略证书验证(默认为True,表示认证),设置为False表示忽略证书认证
 
'''

# print(response.text)
# 使用response.text获取页面数据出现乱码的时候,方案一
# html_str = response.content.decode('utf-8')
# print(html_str)


# 使用response.text获取页面数据出现乱码的时候,方案二
response.encoding = "utf-8"
html_str = response.text
print(html_str)
