#线程使用的模块
import threading
import time


def saysirry():
    for i in range(5):
        print('对不起'+str(i)+threading.current_thread().name)
        # time.sleep(1)



if __name__ == '__main__':
    #创建线程执行任务
    for i in range(5):
        thred = threading.Thread(target=saysirry,name='线程'+str(i))
        thred.start()

        #结论线程之间的执行顺序是无序的，不确定的是
