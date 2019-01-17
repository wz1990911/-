from gevent import pool,monkey
import requests
import gevent

#打个补丁(如果有好事操作我们就需要打补丁)
#将程序中用到的好事操作,换位gevent 自己实现的模块
monkey.patch_all()

def download1_data(url):
    req_header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    response = requests.get(url,headers=req_header)
    if response.status_code == 200 :
        print('执行download1',len(response.text),url,'下载完成','========')


def download2_data(url):
    print('执行方法二','正在下载')
    req_header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    response = requests.get(url, headers=req_header)
    if response.status_code == 200 :
        print('执行download2',len(response.text),url,'下载完成','======')

if __name__ == '__main__':
    #创建一个携程池
    pool = pool.Pool(3)
    gevent.joinall(
        [
            pool.spawn(download1_data,'https://www.yahoo.com/'),
            pool.spawn(download1_data,'https://www.taobao.com/'),
            pool.spawn(download1_data,'https://github.com/'),
            pool.spawn(download2_data,'https://www.yahoo.com'),
            pool.spawn(download2_data,'https://www.taobao.com/'),
            pool.spawn(download2_data,'https://github.com/')

        ]
    )


'''
关于携程:因为携程占用资源保存在cpu寄存器的上下文中
携程切换的速到非常苦熬(比线程和进程快),当遇到耗时操作,会先暂停,将资源保存(cpu寄存器的上下文中),切换到其他
携程中之赐你个其他任务,一旦好事啊操作啊执行完毕,就会切换之前暂停位置,继续执行

'''

