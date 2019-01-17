from urllib import request
#导入这个模块是为了创建一个context忽略
import ssl
#指定url
url = 'http://www.eduxiao.com/zuowen1/'

# url, 设置目标url
# data=None,默认为None表示是一个get请求如果不为None表示是一个post请求
# timeout 指定超时时间
# cafile=None,可以指定证书文件(一般用不到)
# capath=None, 指明证书路径
# cadefault=False, 可以使用默认证书
# context=None位赋值测表示忽略未认证的ssl证书

#根据url发起请求,得到响应结果
#创建context目的是为了忽略为认证毒ca证书
context = ssl._create_unverified_context()
response= request.urlopen(url=url,timeout=0.1,context=context)
#从响应结果可以得到二进制文件
html = response.read()
print(html)
html_srt = html.decode('gb2312')
#将获取的html页面源码文本写入本地文件
with open('page.html','w')as file:
    file.write(html_srt)

status = response.status
print(status)


#获取响应头
response_headers = response.getheaders()
print(response_headers)


#显示文本长度
Content_length = response.getheader('Content-Length')
print(Content_length)


#获取响应原因
response_reason = response.reason
print(response_reason)


#获取响应地址
response_url = response.url
print(response_url)

# 如果不指定请求头中的 user_agent:python3.5-urllib/3.py