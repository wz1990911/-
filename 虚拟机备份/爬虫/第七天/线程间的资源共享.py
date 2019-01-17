import  threading
import time
data_list=[]
def add_data_to_list(num):
    for i in range(num):

        global  data_list

        time.sleep(1)
        data_list.append(i)

def get_list_data():
    print(data_list)

if __name__ == '__main__':
    thread1 = threading.Thread(target=add_data_to_list,args=(10,))
    thread1.start()
    thread1.join()
    thread2 = threading.Thread(target=get_list_data)
    thread2.start()
    #结论：由此现象可知线程1添加任务之后的数据，线程二能获取到说明线程之间资源是共享的






