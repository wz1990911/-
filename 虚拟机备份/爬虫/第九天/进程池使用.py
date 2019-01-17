
from multiprocessing import Pool
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
    print('执行了回调方法')
    print(future)
    code = future[0]
    imageName = future[1]
    with open(imageName,'wb') as file:
        file.write(future[2])


if __name__ == '__main__':

    #创建一个进程池
    pool = Pool(4)

    for i in range(40):
        #往进程池添加任务
        #同步的方法，执行效率比较低
        #pool.apply()
        """
         func,对应的任务的函数名称
         args=(),传递参数(元组) 
         kwds={}, 传递参数(字典)
         callback=None,(执行成功后的回调)
         error_callback=None,(执行错误之后的回调)
        """
        #apply_async是一个异步方法,可以提高任务执行的效率
        imageurl = 'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2811473792,2413507956&fm=11&gp=0.jpg'

        pool.apply_async(
            func=download_image,
            args=(imageurl, 'image' + str(i) + '.jpg'),
            callback=download_done
        )

    #关闭进程池
    pool.close()
    #让紫禁城中的任务执行完毕后，回到主进程继续执行
    pool.join()



