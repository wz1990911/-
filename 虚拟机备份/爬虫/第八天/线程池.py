

#使用线程池
from concurrent.futures import  ThreadPoolExecutor
import  threading,requests
import time,json
from lxml import etree

def download_article_list_by_url(req_url):
    #执行下载任务
    print(req_url,threading.currentThread().name)
    req_header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    response = requests.get(url=req_url,headers=req_header)
    if response.status_code == 200:
        #请求成功
        #可以直接在这里做数据解析
        return response.text,response.status_code


def download_dome(future):
    #获取线程执行完毕后的结果
    print(future.result())
    html = future.result()[0]
    code = future.result()[1]
    print(html,code)
    # 从数据队列中取出响应结果
    html_element = etree.HTML(html)
    # 获取文章列表
    article_divs = html_element.xpath('//div[@class="post floated-thumb"]')
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

        with open('jobbleartcle.json', 'a+') as file:
            print('正在写入', article_dict['title'], threading.currentThread().name)
            json_str = json.dumps(article_dict, ensure_ascii=False)
            file.write(json_str + '\n')
        # 解锁


if __name__ == '__main__':
    #创建线程池
    #线程迟总最大的线程数量max_workers
    pool= ThreadPoolExecutor(max_workers=10)

    #往线程池添加任务
    for i in range(50):
        full_url = 'http://blog.jobbole.com/all-posts/page/%s/' % str(i)
        handier = pool.submit(download_article_list_by_url,full_url)
        handier.add_done_callback(download_dome)


    #其实内部之心了join()方法
    pool.shutdown()
    print('爬虫结束')
    print('主线程结束')





