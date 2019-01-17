import  threading
import time

def run(num,classname):
    print(num,classname)
    for i in range(num):
        print(threading.currentThread().name,i)
        time.sleep(1)


if __name__ == '__main__':
    print('主线程开始'+threading.currentThread().name)
    thread1 = threading.Thread(target=run,name='thread-1',args=(10,'1805'))
    #设置daemon为True，表示主线程结束的时候，不会检查子线程任务是否完成
    #一旦主线程结束，子线程也会同时结束
    thread1.daemon=True
    thread1.start()
    print('主线程结束' + threading.currentThread().name)