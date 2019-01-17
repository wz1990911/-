#有些网站访问的时候需要输入认证信息,即(账号和密码)


import requests
#构建一个阐述输入王铮要认证的账号和密码
auth = ('username','password')
url = '要访问的地址'

response =requests.get(url=url,auth=auth)
