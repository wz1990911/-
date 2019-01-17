# 使用requests的session对象可以吧维持同一个会话

import requests

# 实例化一个session对象

req_session = requests.Session()

# 模拟登录人人网
url = 'http://www.renren.com/PLogin.do'

# 构建一个请求头
req_header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

formdata = {
    'email': '17634060573',
    'password': 'wz990911',
}

response = req_session.post(url=url, data=formdata, headers=req_header)

if response.status_code == 200:

    # 模拟登录成功后访问个人主页
    url = 'http://www.renren.com/968831829/profile'

    # 完成登录后，再次使用session发起请求，会携带cookies等参数
    response = req_session.get(url, headers=req_header)

    if response.status_code == 200:
        with open('page.html', 'w') as file:
            file.write(response.text)

# 如果遇到访问网页出现证书错误,我们需要将varfity参数改为False
response = req_session.get(url, headers=req_header, verify=False)
