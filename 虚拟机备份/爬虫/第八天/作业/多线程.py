# １．分析首先需要从首页中获取所有分类的url
# ２．根据分页的url构造每个分类首页的url,发起请求，获取响应
# ３．从分页url的响应结果里面获取每本书籍的详情url地址，发起请求
# ４．获取详情页中的数据，并做数据的持久化
# ５．每一页的数据提取完毕后，构造下一页请求，发起请求，继续执行第３步
import requests,threading

from lxml import etree
from urllib.parse import urljoin
import re, pymysql, json
from concurrent.futures import ThreadPoolExecutor


def get_cotagry_url(start_url):
    req_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }


    response = requests.get(start_url, headers=req_headers)
    if response.status_code == 200:

        html_etree = etree.HTML(response.text)
        # 获取人文社科的三级分类url
        cotagry_urls = html_etree.xpath(
            '//div[@class="con flq_body"]/div[8]//div[@class="col eject_left"]/dl//dd/a/@href')
        cotagry_titles = html_etree.xpath(
            '//div[@class="con flq_body"]/div[8]//div[@class="col eject_left"]/dl//dd/a/@title')

        # print(cotagry_urls)
        # print(cotagry_titles)

        # 获取到后会发现，里面有一个更多的url:http://book.dangdang.com/01.26.htm?ref=book-01-A，
        # 把跟多的过滤掉，他不是分类url
        i = 0
        for first_page_url in cotagry_urls:
            # 分类第一页url
            # http://category.dangdang.com/cp01.36.01.00.00.00.html
            # 分类第二页url
            # http://category.dangdang.com/pg2-cp01.36.01.00.00.00.html
            # 分类第三页url
            # http://category.dangdang.com/pg2-cp01.36.01.00.00.00.html
            list_url = []
            if 'ref=book-01-A' not in first_page_url:
                # 获取每个分类第一页的数据
                list_url.append(first_page_url )
            i += 1
            return list_url

        # 测试使用
        # download_book_list_by_url('http://category.dangdang.com/cp01.36.01.00.00.00.html','历史')


def download_book_list_by_url(i,threadLock):
    print('正在获取分页：', i)
    req_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    response = requests.get(i, headers=req_headers)
    if response.status_code == 200:
        html_etree = etree.HTML(response.text)

        # 获取每一本书的url详情地址
        book_urls = html_etree.xpath('//div[@id="search_nature_rg"]/ul/li/a[1]/@href')
        print(book_urls)
        for book_url in book_urls:
            return book_url,threadLock

        # 获取下一页地址
        # next_url = html_etree.xpath('//div[@class="paging"]/ul/li[@class="next"]/a/@href')
        # if len(next_url) > 0:
        #     full_next_url = urljoin(response.url,next_url[0])
        #     download_book_list_by_url(full_next_url)


def download_book_detail_by_url(future):
    """
    根据书籍详情地址，获取书籍详情的内容
    :param req_url:
    :return:
    """
    print(future.result())

    req_url = future.result()[0]

    req_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    response = requests.get(req_url, headers=req_headers)
    if response.status_code == 200:
        html_element = etree.HTML(response.text)
        book_dict = {}
        # 获取书籍信息
        # 大分类
        book_dict['big_cotagry'] = html_element.xpath('//div[@class="breadcrumb"]/a[2]/text()')[0]
        # 二级分类
        book_dict['small_catogry'] = html_element.xpath('//div[@class="breadcrumb"]/a[3]/text()')[0]
        # 标题
        book_dict['title'] = html_element.xpath('//div[@class="name_info"]/h1/@title')[0]
        # 封面图片
        book_dict['coverImage'] = html_element.xpath('//img[@id="largePic"]/@src')[0]
        # 简介
        book_dict['content'] = html_element.xpath('//span[@class="head_title_name"]/text()')[0].replace('\r\n',
                                                                                                        '').replace(' ',
                                                                                                                    '')
        # 作者
        author_info = html_element.xpath('//span[@id="author"]/a/text()')
        book_dict['author'] = author_info[0]
        if len(author_info) == 3:
            book_dict['biming'] = author_info[1]
            book_dict['chuping'] = author_info[2]
        elif len(author_info) == 2:
            book_dict['biming'] = '暂无'
            book_dict['chuping'] = author_info[1]
        else:
            book_dict['biming'] = '暂无'
            book_dict['chuping'] = '暂无'
        # book_dict['author'] = html_element.xpath('//span[@id="author"]/a[1]/text()')[0]
        # book_dict['biming'] = html_element.xpath('//span[@id="author"]/a[2]/text()')[0]
        # book_dict['chuping'] = html_element.xpath('//span[@id="author"]/a[3]/text()')[0]
        book_dict['publish_company'] = html_element.xpath('//div[@class="messbox_info"]/span[2]/a/text()')[0]
        book_dict['publist_time'] = html_element.xpath('//div[@class="messbox_info"]/span[3]/text()')[0]
        comment = html_element.xpath('//a[@class="comm_num_down"]/text()')
        if len(comment):
            book_dict['commentnum'] = comment[0]
        book_dict['qg_price'] = ''.join(html_element.xpath('//p[@id="dd-price"]/text()')).replace('\r\n', '').replace(
            ' ', '').replace('\t', '')
        d_price = html_element.xpath('//a[@id="e-book-price"]/text()')
        if len(d_price) > 0:
            book_dict['d_price'] = d_price[0]
        else:
            book_dict['d_price'] = '暂无电子书价格'
        hot = html_element.xpath('//a[@id="collect_left"]/text()')[0]
        book_dict['hotnum'] = re.search('\d+', hot).group()

        # 排名和团购价格在如下接口中获取，为json数据
        # step:获取商品的id
        book_id = re.search('\d+', response.url).group()
        # http://product.dangdang.com/index.php?r=callback%2Fproduct-info&productId='这里是商品id需要动态变换'&isCatalog=0&shopId=0&productType=0
        # step2:构建完整的url地址,发起请求
        full_url = 'http://product.dangdang.com/index.php?r=callback%2Fproduct-info&productId={}&isCatalog=0&shopId=0&productType=0'.format(
            book_id)
        book_dict['t_price'], book_dict['qg_price'], book_dict['zekou'] = get_book_other_info_by_url(full_url)
        threadLock = future.result()[1]
        write_data_to_db(book_dict, threadLock)


def get_book_other_info_by_url(req_url):
    req_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    response = requests.get(req_url, headers=req_headers)
    if response.status_code == 200:

        json_data = json.loads(response.text)
        # 判断如果拼团这个key存在，并且对应的值的长度大于０，则说明有拼团活动
        if 'pintuanInfo' in json_data['data']['spu'] and len(json_data['data']['spu']['pintuanInfo']) > 0:
            # 拼团价格
            t_price = json_data['data']['spu']['pintuanInfo']['pintuan_price']
        else:
            t_price = '暂无拼团价格'
        # 这里要判断一下,有没有限时抢购
        if 'p102' in json_data['data']['spu']['promotion']:
            # 抢购价
            qg_price = json_data['data']['spu']['promotion']['p102']['price']['directPrice']
            # 折扣
            zekou = json_data['data']['spu']['promotion']['p102']['limitNumber']

            return t_price, qg_price, zekou
        else:
            # 原价价格
            org_price = json_data['data']['spu']['price']['originalPrice']
            return t_price, org_price, '暂无折扣'


def write_data_to_db(bookinfo,threadLock):
    print(bookinfo['title'], '完成')
    print(bookinfo)
    # sql = '''
    #       INSERT INTO bookinfo(%s)
    #       VALUES (%s)
    #       ''' % (
    #     ','.join(bookinfo.keys()),
    #     ','.join(['%s'] * len(bookinfo))
    # )
    #
    # print('正在存储')
    # try:
    #     cursor.execute(sql, list(bookinfo.values()))
    #     mysql_client.commit()
    # except Exception as err:
    #     mysql_client.rollback()
    #     print(err)


if __name__ == "__main__":
    # 创建mysql的客户端连接
    # mysql_client = pymysql.Connect('localhost','root','password','dangdang',charset='utf8')
    # # #创建游标
    # cursor = mysql_client.cursor()
    # 起始url
    start_url = 'http://book.dangdang.com/'


    # 开始爬取任务
    list_url = get_cotagry_url(start_url)
    pool = ThreadPoolExecutor(max_workers=10)
    threadLock = threading.Lock()
    for i in list_url:
        handler = pool.submit(download_book_list_by_url,i,threadLock)
        handler.add_done_callback(download_book_detail_by_url)
    pool.shutdown()


    print('爬虫结束')
    print('主线程结束')




