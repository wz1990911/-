
import requests
import re
from urllib import parse
import pymysql

#创建数据库
client = pymysql.Connect('localhost','root','1','qidian',charset='utf8')
#创建游标
cursor = client.cursor()


def qidianpider(req_url):
    #请求头
    req_headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
    }
    #发起请求
    #params:字典类型的参数，存放的是get请求后拼接的参数
    response = requests.get(url=req_url,headers=req_headers)

    if response.status_code == 200:

        # with open('page.html','w') as file:
        #     file.write(response.text)
        #根据正则提取想要的目标数据
        pattern = re.compile(
            '<div.*?book-img-box.*?<img.*?src="(.*?)">'+
            '.*?<h4>.*?<a.*?href="(.*?)".*?>(.*?)</a>'+
            '.*?<a.*?class="name".*?>(.*?)</a>'+
            '.*?<a.*?>(.*?)</a>'+
            '.*?<a.*?>(.*?)</a>'+
            '.*?<p.*?intro.*?>(.*?)</p>',
            re.S
        )
        result = re.findall(pattern,response.text)
        # print(result[0][2])
        if len(result)>0:
            for noval in result:
                noval_dict = {}
                noval_dict['coverimage'] = parse.urljoin(req_url,noval[0])
                noval_dict['novalurl'] = parse.urljoin(req_url,noval[1])
                noval_dict['title'] = noval[2]
                noval_dict['author'] = noval[3]
                noval_dict['tags'] = noval[4]+noval[5]
                noval_dict['content'] = noval[6].replace('\r','').replace(' ','')
                # write_noval_data_to_db(noval_dict)



            #构建下一页请求
            pattern = re.compile('.*?page=(\d+)',re.S)
            #匹配出当前页的页码
            result = re.findall(pattern,req_url)
            current_page = result[0]
            #构造下一页页码
            next_page = int(current_page)+1
            #
            pattern = re.compile('page=\d+',re.S)
            next_url = re.sub(pattern,'page='+
                              str(next_page),
                              req_url)
            qidianpider(next_url)


def write_noval_data_to_db(novalInfo):


    sql = '''
    INSERT INTO qidian(%s)
    VALUES (%s)
    '''%(
        ','.join(novalInfo.keys()),
        ','.join(['%s']*len(novalInfo))
    )

    print('正在存储')
    try:

        cursor.execute(sql,list(novalInfo.values()))

        client.commit()
    except Exception as err:
        print(err)
        client.rollback()


if __name__ == '__main__':

    #找目标url
    #https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=1
    #https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=2
    #https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=3
    start_url = 'https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=1'
    qidianpider(start_url)