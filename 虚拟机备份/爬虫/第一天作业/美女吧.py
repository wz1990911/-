from urllib.parse import urldefrag,urlencode
from urllib import request


def meinvba(startPage,endPage,keyword):
    req_header = {
        'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0Accept: */*',
    }

    for i in range(startPage,endPage+1):
        parmas = {
            'kw':keyword,
            'pn':(i-1)*50.
        }
        print(parmas)
        parmas_str = urlencode(parmas)
        full_url = 'https://tieba.baidu.com/f?'+parmas_str
        req = request.Request(url=full_url,headers=req_header)
        response = request.urlopen(req)
        filename = keyword+str(i)+'.html'
        html_str = response.read().decode('utf-8')
        print(filename)
        with open(filename,'w')as file:
            print('正在写入'+str(i)+'页')
            file.write(html_str)



if __name__ == '__main__':
    startPage = int(input('请输入起始页'))
    endPage = int(input('请输入截止页'))
    keyword = input('请输入关键字')
    meinvba(startPage,endPage,keyword)