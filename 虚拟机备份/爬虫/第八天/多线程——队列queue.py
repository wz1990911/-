import queue

#创建一个队列
#maxsize:允许存储最大的量
queue_obj = queue.Queue(maxsize=40)

for i in range(0,40):
    # 存值
    queue_obj.put(i)

# 取值
print(queue_obj.get(i))


#获取队列大小
print(queue_obj.qsize())
#判断队列是否满了
print(queue_obj.full())
#判断队列是否为空
print(queue_obj.empty())

#注意：队列是线程安全的，list,dict是非线程安全的（最好加上安全锁）






