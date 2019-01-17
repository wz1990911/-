from multiprocessing import Process,Queue
import os
#使用multiprocessing 模块下的Queue, 可以帮助我们实现进程自检的通讯

def write_data(dataqueue):
    for i in range(40):
        # 网队列里存值
        dataqueue.put(i)
    print(os.getpid(),'执行完毕')

def read_data(dataqueue):
    # 如果队列不为空就取值
    while not dataqueue.empty():
        print(dataqueue.get())


if __name__ == '__main__':
    #数据队列
    q = Queue()
    process1 = Process(target=write_data,args=(q,))
    process1.start()
    process1.join()

    #进程二
    process2 = Process(target=read_data, args=(q,))
    process2.start()
    process2.join()