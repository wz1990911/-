from multiprocessing import Pool,Manager
import os,time

def write_data(queue,num):
    for i in range(num):
        queue.put(i)
    print('存储任务执行完毕了',os.getpid())

def read_date(queue):
    while not queue.empty():
        print(queue.get())
    print('取值任务执行完毕了',os.getpid())


if __name__ == '__main__':

    #使用manager Queue()创建一个队列
    #可以实现在进程池的进程中实现数据的共享(通讯)
    q = Manager().Queue()

    #创建一个进程池
    pool = Pool(4)

    #往进程池中添加一个任务
    pool.apply_async(write_data,(q,40))

    time.sleep(2)

    #读取队列中的数据
    pool.apply_async(read_date,(q,))

    #关闭
    pool.close()
    #让进程池中的子进程全部执行完毕，然后回到主进程中继续执行
    pool.join()