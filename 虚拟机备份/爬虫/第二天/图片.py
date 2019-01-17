from urllib import request
import re
def tiepaSpider(startpage,endpage):

    for pageNum in range(startpage,endpage+1):
        #请求每个页面的页面源码
        download_tieba_list_data(pageNum)

def download_tieba_list_data(pageNum):

    print('正在下载第'+str(pageNum)+'页')

    req_url = 'https://tieba.baidu.com/f?kw=%E7%BE%8E%E5%A5%B3&pn=' + str((pageNum-1)*50)

    print(req_url,str((pageNum-1)*50))

    req_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }

    req = request.Request(url=req_url, headers=req_headers)

    response = request.urlopen(req)

    if response.status == 200:
        print('请求成功')
        # 请求成功后，根据正则规则提取列表页中帖子的详情地址
        pattern = re.compile(
            '<li.*?class=" j_thread_list clearfix.*?>.*?<a.*?noreferrer.*?' +
            'href="(.*?)".*?j_th_tit.*?>.*?</li>', re.S)
        result = re.findall(pattern, response.read().decode('utf-8'))
        print('11111')
        for url in result:
            full_url = 'https://tieba.baidu.com'+url
            print(full_url)
            download_tizi_detail(full_url)

def download_tizi_detail(url):
    print('正在下载'+url)
    req_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    req = request.Request(url=url, headers=req_headers)
    response = request.urlopen(req)

    if response.status == 200:
        #请求成功后提取图片连接
        pattern = re.compile('<img.*?class="BDE_Image".*?src="(.*?)".*?>',re.S)
        result = re.findall(pattern,response.read().decode('utf-8'))
        print(result)
        for url in result:
            download_image(url)

#根据图片连接下载图片
def download_image(image_url):
    req_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    req = request.Request(url=image_url, headers=req_headers)
    response = request.urlopen(req)

    filename = image_url[-20:]
    #将获取的图片存储到本地
    with open('images/' + filename,'wb') as file:
        print('正在写入图片'+filename)
        file.write(response.read())



if __name__ == '__main__':
    startpage = int(input('输入起始页：'))
    endpage = int(input('输入结束页码：'))
    tiepaSpider(startpage,endpage)
