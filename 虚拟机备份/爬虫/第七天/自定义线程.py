import threading
class ThreadDowload(threading.Thread):
    def __init__(self,threadName):
        super(ThreadDowload, self).__init__()
        self.threadName = threadName
    def run(self):
        print(self.threadName)

        #可以在run方法中做任何你想要做的操作
        for i in range(0,123):
            print(i)


thread1 = ThreadDowload(threadName='王哲是一个大傻逼')
thread1.start()