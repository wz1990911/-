#如何使用requests发起get 请求


import requests
#目表url
#params:get请求携带的参数
parmas={
    'wd':'美女'
}
#如果get请求后又查询参数,咱们一般会吧参数放在字典里,然后字典传递给parmas参数
response = requests.get('https://www.baidu.com/s?',params=parmas)

#可以得到解码后的字符串
html_test = response.text
# print(html_test)

#获取返回的二进制数据
b_html = response.content
print('二进制数据')
print(b_html)

#响应状态马
status =response.status_code
print('状态码')
print(status)

#获取请求头
req_header = response.request.headers
print('请求头')
print(req_header)
#响应头
response_headers = response.headers
print('响应头')
print(response_headers)
#获取编码类型
encodeing = response.encoding
print('编码类型')
print(encodeing)
