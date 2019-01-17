#1一个严格意义上的json串，必须是由数组(list)和字典(dict)两种数据结果组成
#2json串中的非数字类型的数据都必须使用双引号包裹
import  json


# json.dumps() #将python数据类型，转换为json字符串
data = {
    'classname':'1805',
    'classinfo':'1805是一个优秀的班集体，欢迎广大帅哥美女加入',
    'classnum':26,
    'peoplelist':['王哲','吕东泽','王伟录','李宜航'],
}
print(type(data))
#将python数据类型，转换为json字符串
json_str = json.dumps(data,ensure_ascii=False)  #ensure_ascii写为False不采用ascii码，默认是ascii编码，不采用默认的
print(json_str)
print(type(json_str))

# json.loads() #将json字符串，转换为python的数据类型
loads_data = json.loads(json_str)
print(type(loads_data))
print(loads_data)

# json.dump() #将python数据类型，转换为json字符串，并且可以将json字符串写入到本地
data1 = {
    'classname':'1805',
    'classinfo':'1805是一个优秀的班集体，欢迎广大帅哥美女加入',
    'classnum':26,
    'peoplelist':['王哲','吕东泽','王伟录','李宜航'],
}
json.dump(obj=data1,fp=open('data1.json','w'),ensure_ascii=False)

# json.load() #将本地文件中存储的json字符串，转换为python数据类型
load_data= json.load(open('data1.json'))
print(type(load_data))
print(load_data)