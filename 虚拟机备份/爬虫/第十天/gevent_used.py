#gevent的携程不需要你手动切换,内部会自动切换
import  gevent,requests


def download2(num):
    '''
    下载图片　比较耗时
    :return:
    '''
    print('222嘿嘿嘿',str(num),gevent.getcurrent())
    image_url  = 'http://5b0988e595225.cdn.sohucs.com/images/20170906/58cdb24be3624488ad3e8d3d00b4585f.jpeg'
    req_header = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }

    response = requests.get(url=image_url,headers=req_header)
    #又遇到耗时操作
    gevent.sleep(2)
    if response.status_code == 200:
        print('图片'+str(num)+'2下载完成')

if __name__ == '__main__':
    #创建两个协程00
    gevent1 = gevent.spawn(download2,1)
    gevent2 = gevent.spawn(download2,2)
    gevent3 = gevent.spawn(download2,3)
    gevent4 = gevent.spawn(download2,4)
    gevent5 = gevent.spawn(download2,5)


    gevent1.join()
    gevent2.join()
    gevent3.join()
    gevent4.join()
    gevent5.join()


