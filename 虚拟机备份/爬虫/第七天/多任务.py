#1同时执行多个任务（同时打开qq，微信，编辑器，浏览器，优酷）
#cpu：单核同时执行的任务数量只有一个，但看上去像是在执行多任务，是因为任务切换的间隔时间极端


#多喝cpu：同时可以执行多个人户，加入任务粮超过核心说在某个核心下面任务属于交替执行
# #并发和并行的概念：
# 并发：单核cpu同时执行多个任务,任务是同时发起的,但是并不是同时执行,而是交替执行，
# 并行：任务数量小于或等于核心数量，这个时候每一个和兴都在执行任务，任务是同时进行的
# 实现多任务的手段（方式）：
# 1.多线程
# 2.多进程
# 3协程
