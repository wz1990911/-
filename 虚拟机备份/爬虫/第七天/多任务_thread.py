#线程使用的模块
import threading
import time


def saysirry():
    for i in range(5):
        print('对不起'+str(i)+threading.current_thread().name)
        time.sleep(1)


def dosome_thing():
    for i in range(5):
        print('捏捏腿'+str(i)+threading.current_thread().name)
        time.sleep(1)

if __name__ == '__main__':
    print('主线程开始'+threading.current_thread().name)

    #创建子线程
    '''
    target = None, 线程执行的任务
    name = None,    线程的名称
                
    args = ()       执行函数传递的参数
    daemon = None   None，默认为False，在主线程结束时，压减产子线程中任务是否结束
            如果子线程还在运行，则主线程还在等待
            如果设为True，主线程结束时，不会检查子线程是否完成，主线程结束子线程也会结束
    '''
    stat_time = time.time()
    thread1 =threading.Thread(target=saysirry,name='县城一号')
    thread2 = threading.Thread(target=dosome_thing,name='县城二号')
    #开启线程，执行任务
    thread1.start()
    thread2.start()
    #阻塞的作用，必须等于子线程中任务执行完毕
    #然后才能回到主线程继续执行
    thread1.join()
    thread2.join()
    end_time = time.time()
    print(end_time-stat_time)
    print("主线程结束"+threading.currentThread().name)


