#由于线程之间的资源是共享的，可能导致多个线程同时访问同一块资源
#那么可能会造成数据的紊乱，这设我们需要确保同一时刻只有一个线程
#在访问资源，就需要我们添加线程锁

import threading

global_num = 0

def add_num1(num):

    global  global_num

    for i in range(num):
        th_lock.acquire()
        global_num+=1
        th_lock.release()

    print(threading.currentThread().name,global_num)

def add_num2(num):

    global  global_num

    for i in range(num):
        th_lock.acquire()
        global_num+=1
        th_lock.release()

    print(threading.currentThread().name,global_num)
#创建一个线程锁
th_lock = threading.Lock()
print('进程开始',threading.currentThread().name)
thread1 = threading.Thread(target=add_num1,args=(1000000,))
thread2 = threading.Thread(target=add_num2,args=(1000000,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print('-------',global_num)