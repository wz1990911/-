from urllib import request
from urllib import parse
import pymysql
import re





def biaoti():
    req_url = 'https://www.qidian.com/all'
    req_header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    }

    req = request.Request(url=req_url,headers=req_header)
    response = request.urlopen(req)
    if response.status == 200:
        yuanma = response.read().decode('utf-8')
        bt =re.compile('<li\sdata-rid.*?<a.*?data-bid.*?<img\ssrc="(.*?)">.*?<h4>.*?<a.*?target="_blank".*?>(.*?)</a.*?</h4>.*?<a\sclass="name".*?>(.*?)</a>.*?<a\sclass="go-sub-type".*?>(.*?)</a>.*?<p\sclass="intro">\s*(.*?)\r.*?</p>',re.S)
        name = {}
        content = re.findall(bt,yuanma)
        print(content)
        for i in content:
            print(i)
            name['图片'] = i[0],
            name['名字'] = i[1],
            name['作者'] = i[2],
            name['分类'] = i[3],
            name['内容'] = i[4],
            cun(name)



def cun(name):
    # 创建数据库链接
    client = pymysql.Connect('localhost', 'root', '1', 'qidian', 3306, charset='utf8')
    # 创建游标
    cursor = client.cursor()
    sql = '''
            INSERT INTO qidian(%s)
            VALUES (%s)
            ''' % (
        ','.join(name.keys()),
        ','.join(['%s'] * len(name))

    )
    try:
        cursor.execute(sql, [value for key, value in name.items()])
        client.commit()
    except Exception as err:
        print(err)
        client.rollback()










if __name__ == '__main__':
    biaoti()