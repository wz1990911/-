#parse模块:定义了url的标准借口,可以实现url的抽取,一般可用用这个模块完成url的解析.合并.编码解码
from urllib import parse

#parse.urlparse()可以实现url的识别和分段
url = 'https://book.qidian.com/info/1004608738?wd=123&page=20#Catalog'


result = parse.urlparse(url)
print(result)
#url:表示拆分的url地址
#scheme='':可以设置默认的协议(前期是你要拆分的url缺少协议的情况下)
#allow_fragments=T



'''
scheme='https', 表示协议
netloc='book.qidian.com', 表示域
path='/info/1004608738',    表示资源路径
params='', 参数
query='wd=123&page=20',    查询参数
fragment='Catalog'    锚点
'''
print(result.scheme)

#parse.urlunparse()可以实现url组合
#parse.urlunparse()长度必须为6

parmas =   ('https','book.qidian.com','/info/1004608738','','wd=123&page=20','Catalog')
a = parse.urlunparse(parmas)
print(a)


#parse.urljoin:同样是拼接,需要传递一个基类url,另一个参数是一个不完整的url
#参照基类url将不完整的那个的url拼接完整

base_url = 'https://book.qidian.com/info/1004608738?wd=123&page=20#Catalog'
sub_url = '/info/100860010'

#base:基类url
#url:一般情况下传递一个不完整的url
full_url =  parse.urljoin(base_url,sub_url)
print(full_url)
#parse.urlencode().将字典参数序列化为url编码后的字符串
parmas = {
    'wd':'123',
    'page':20,
    'key':'刑凯',
}
result = parse.urlencode(parmas)
print(result)
'''
wd=123&page=20&key=%E5%88%91%E5%87%AF
'''
full_url = 'https://book.qidian.com/info/1004608738?'+result
print(full_url)

#parse.parse_qs()将url编码后的字符串反序列化为字典类型
parmas_dict = parse.parse_qs(result)
print(parmas_dict)

#parse.quote()可以将中文转为url编码格式
keyword = '邢凯'
result = parse.quote(keyword)
print(result)


#parse.unquote():将编码格式的中文字符转换为中文
result= parse.unquote(result)
print(result)