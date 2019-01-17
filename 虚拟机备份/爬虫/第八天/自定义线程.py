# 1.jobbole案例
# 1.任务队列
# 2.爬取线程（多个）
# 3.数据队列（存储爬取线程得到的响应结果）
# 4.解析线程(多个)
# 5.最终将解析的任务存储到本地
import queue, threading, requests, json
from lxml import etree

#自定义爬取线程
class CrawlThread(threading.Thread):
    def __init__(self,task_queue,data_queue,threadName):
        super(CrawlThread,self).__init__()
        #任务队列
        self.task_queue = task_queue
        #数据队列
        self.data_queue = data_queue
        #线程名称
        self.threadName = threadName


    def run(self):
        '''
           根据分页的url获取分页中的文章列表
           '''
        req_header = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        }
        # task_queue.empty()为True:表示没有任务,为False:表示不为空
        # while task_queue.empty() != True:
        while not self.task_queue.empty():
            # 从队列中取数据
            req_url = task_queue.get()
            response = requests.get(url=req_url, headers=req_header)
            if response.status_code == 200:
                print(response.url, '获取成功')
                self.data_queue.put(response.text)


def parse_data_by_queue(data_queue,threadLock):
    # 从数据队列中取出响应结果
    html = data_queue.get()
    html_element = etree.HTML(html)
    # 获取文章列表
    article_divs = html_element.xpath('//div[@class="post floated-thumb')
    for article_div in article_divs:
        article_dict = {}
        # 标题
        article_dict['title'] = article_div.xpath('.//a[@class="archive-title"]/text()')[0]
        # 获取发布时间
        article_dict['publish'] = article_div.xpath('.//div[@class="post-meta"]/p[1]/text()')[0]
        # 获取分类
        article_dict['catotry'] = article_div.xpath('.//div[@class="post-meta"]/p[1]/a[2]/text()')[0]
        # 评论数
        commentnum = article_div.xpath('.//div[@class="post-meta"]/p[1]/a[3]/text()')
        if len(commentnum) > 0:
            article_dict['commentnum'] = commentnum[0]
        # 简介
        article_dict['content'] = article_div.xpath('.//span[@class="excerpt"]/p/text()')[0]

        # 将数据写入本地：
        # 加锁
        threadLock.acquire()
        with open('jobbleartcle.json','a+') as file:
            print('正在写入',article_dict['title'],threading.currentThread().name)
            json_str = json.dumps(article_dict, ensure_ascii=False)
            file.write(json_str + '\n')
        #解锁
        threadLock.release()


if __name__ == '__main__':
    # 寻找目标url
    # 第一页：http://blog.jobbole.com/all-posts/page/1/
    # 第二页：http://blog.jobbole.com/all-posts/page/2/
    # 第三页：http://blog.jobbole.com/all-posts/page/3/
    # 1.任务队列
    task_queue = queue.Queue()

    # 创建数据队列
    data_queue = queue.Queue()

    for i in range(1, 564):
        full_url = 'http://blog.jobbole.com/all-posts/page/%s/' % str(i)
        task_queue.put(full_url)
    # 创建爬取线程（创建4个爬取线程）
    crawlThreadName = ['吕东泽1号', '吕东泽2号', '吕东泽3号', '吕东泽4号']
    crawlThread = []
    for name in crawlThreadName:
        thread = threading.Thread(
            target=dowmload_article_list_by_url,
            name=name,
            args=(task_queue, data_queue)
        )
        # 启动线程
        thread.start()
        crawlThread.append(thread)
    # 添加join()的目的，是为了让任务队里中的所有请求都执行完毕
    for thread in crawlThread:
        thread.join()
    # 创建解析线程
    # 线程锁
    threadLock = threading.Lock()
    parseThreadName = ['娜娜1号', '娜娜2号', '娜娜3号', '娜娜4号']
    parseThread = []
    for name in parseThreadName:
        thread = threading.Thread(
            target=parse_data_by_queue,
            name=name,
            args=(data_queue,threadLock)
        )
        thread.start()
        # 将创建的解析线程放进来
        parseThread.append(thread)
    for thread in parseThread:
        thread.join()
    print('爬虫结束')
    print('主线程结束')
