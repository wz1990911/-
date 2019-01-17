#每一个进程都有自己独立的存储空间，是操作系统分配资源的基本单元

from multiprocessing import Process
import os

def run1(name,classname):
    print(name,classname)
    for i in  range(40):
        #getpid 获取当前id
        #getppid 获取父id
        print('process1',i,os.getpid(),os.getppid())
def run2(name,classname):
    print(name, classname)
    for i in  range(40):
        print('process2',i,os.getpid(),os.getppid())



if __name__ == '__main__':
    print('主进程开始')
    # group = None, 进程要处理的任务
    # target = None, 给进程一个名字
    # name = None 任务要传递的参数
    #创建子进程
    process1 = Process(target=run1,name='进程一号',args=('王美丽',1805))
    process2 = Process(target=run2,name='进程二号',args=('邢凯',1805))
    print(process1.name)
    print(process2.name)


    process1.start()
    process2.start()
    #添加join   timeout参数目的设置阻塞时间
    process1.join()
    process2.join()
    print('主进程结束')