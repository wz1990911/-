import  requests

url = 'https://httpbin.org/post'
#构建一个字典类型的参数里面存放的元素是要上传的文件数据
filter ={
    'txt':open('class.text','r'),
    'file':open('image.jpeg','rb')
}
#发起请求 拿到响应结果
response = requests.post(url=url,files=filter)
print(response.status_code)
print(response.text)