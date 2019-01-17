from urllib import parse

url = 'https://book.qidian.com/info/1004608738?wd=123&page=20#Catalog'
result = parse.urlparse(url)
print(result)
a = ('https','book.qidian.com','/info/1004608738','','wd=123&page=20','Catalog')
result = parse.urlunparse(a)
print(result)