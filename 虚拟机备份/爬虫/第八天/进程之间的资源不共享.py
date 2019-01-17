from  multiprocessing import Process


data=[]
def write_num(num):
    global data
    for i in range(40):
        data.append(i)
    print(data)

def read_num():
    print(data)



if __name__ == '__main__':
    #创建两个进程
    process1= Process(target=write_num,args=(40,))
    process1.start()
    process1.join()


    process2 = Process(target=read_num)
    process2.start()
    process2.join()