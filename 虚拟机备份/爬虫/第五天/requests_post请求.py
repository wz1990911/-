import requests

req_url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

# 分析表单数据
formdata = {
    'i': '老鼠爱大米',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION',
    'typoResult': 'false',
}

response =requests.post(url=req_url,data=formdata)
print(response.status_code)
print(response.text)
#response.json()这个可以将json字符串转换为python数据类型
#注意:必须确保获取到的json字符串是一个严格意义上的json字符串,否则会报错
json_data = response.json()
print(type(json_data))
print(json_data)