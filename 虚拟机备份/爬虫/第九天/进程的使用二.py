from concurrent.futures import ProcessPoolExecutor
import requests

def download_image(imageUrl,imageName):
    print(imageUrl,imageName)
    req_header = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    response = requests.get(imageUrl,headers=req_header)
    if response.status_code == 200:
        #请求成功
        return response.status_code,imageName,response.content

def download_done(future):
    print('执行了回到掉函数')
    print(future.result())


if __name__ == '__main__':

    #创建进程池
    pool = ProcessPoolExecutor(4)

    for i in range(40,80):
        imageurl = 'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2811473792,2413507956&fm=11&gp=0.jpg'
        #往进程池添加任务
        handler =  pool.submit(download_image,imageurl,'image'+str(i)+'.jpg')
        #添加回调方法
        handler.add_done_callback(download_done)

    #实质都是执行join方法
    pool.shutdown()
