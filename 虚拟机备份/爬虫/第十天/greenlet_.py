#pip3 install greenlet

from greenlet import greenlet
import requests


def download1():
    '''
    下载图片　比较耗时
    :return:
    '''
    print('１１１真在')
    image_url  = 'http://5b0988e595225.cdn.sohucs.com/images/20170906/58cdb24be3624488ad3e8d3d00b4585f.jpeg'
    req_header = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }

    response = requests.get(url=image_url,headers=req_header)
    #遇到耗时操作，切换协程
    greenlet2.switch()

    if response.status_code == 200:
        print('hei./.１１下载完成')
    greenlet2.switch()

def download2():
    '''
    下载图片　比较耗时
    :return:
    '''
    print('222嘿嘿嘿')
    image_url  = 'http://5b0988e595225.cdn.sohucs.com/images/20170906/58cdb24be3624488ad3e8d3d00b4585f.jpeg'
    req_header = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }

    response = requests.get(url=image_url,headers=req_header)
    #又遇到耗时操作
    greenlet1.switch()
    if response.status_code == 200:
        print('2下载完成')



if __name__ == '__main__':
    #创建两个协程
    greenlet1 = greenlet(download1)
    greenlet2 = greenlet(download2)

    #switch()能够切换到指定协程
    greenlet1.switch()