#分析网站提取目标url

#分类的url
#https://movie.douban.com/j/search_tags?type=movie&source=
#两个参数
# type: movie
# source:

#热门分类地址
#https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0

# type: movie 请求数据的类型
# tag: 热门　分类的关键字
# sort: recommend　筛选排序
# page_limit: 20　每页限制返回条数
# page_start: 20　每页起始偏移量

#https://movie.douban.com/j/search_subjects?type=movie&tag=%E6%9C%80%E6%96%B0&page_limit=20&page_start=0 最新
#https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%BB%8F%E5%85%B8&sort=time&page_limit=20&page_start=0 经典
#https://movie.douban.com/j/search_subjects?type=movie&tag=%E5%8F%AF%E6%92%AD%E6%94%BE&sort=time&page_limit=20&page_start=0 可播放

#通过各分类url链接对比发现　热门分类sort为recommend
#最新分类没有sort参数,
#其它的分类的sort都为time

#每一个电影的详信息的ajax请求接口
#https://movie.douban.com/j/subject_abstract?subject_id=26847920

import pymysql,json,re
from urllib import request
from urllib.parse import urlencode

class DoubanSpider(object):

    def __init__(self):
        #创建数据库链接
        self.client = pymysql.Connect('localhost','root','1','doubanmovie',3306,charset='utf8')
        #创建游标
        self.cursor = self.client.cursor()


    def start_spider(self):
        #１.根据分类的url接口,获取分类关键字,构造分类的url
        #目标url =
        req_url = 'https://movie.douban.com/j/search_tags?type=movie&source='
        #构建一个请求头
        req_header = {
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
        }
        #构建一个request请求对象
        req = request.Request(url=req_url,headers=req_header)
        #发起请求
        response = request.urlopen(req)
        #打印状态码
        print(response.status)
        #如果请求成功
        if response.status == 200:
            #获取数据
            # print(response.read().decode('utf-8'))

            #使用json.loads将json字符串,转换成python数据类型
            data = json.loads(response.read().decode('utf-8'))
            print(type(data))
            tags = data['tags']
            print(tags)

            for tag in tags:
            # 通过各分类url链接对比发现　热门分类sort为recommend
            # 最新分类没有sort参数,
            # 其它的分类的sort都为time

            #https://movie.douban.com/j/search_subjects?type=movie&tag=%E6%9C%80%E6%96%B0&page_limit=20&page_start=0
                base_url = 'https://movie.douban.com/j/search_subjects?type=movie&%s&page_limit=20&page_start=0'

                if tag == '热门':
                    parmas = {
                        'tag': tag, #分类关键字
                        'sort': 'recommend'
                    }

                elif tag == '最新':
                    parmas = {
                        'tag': tag,  # 分类关键字

                    }

                else:
                    parmas = {
                        'tag': tag,  # 分类关键字
                        'sort': 'time'
                    }
                # 使用urlencode将字典转换为url编码格式的字符串
                parmas_tranform = urlencode(parmas)
                full_url = base_url % parmas_tranform
                print(full_url)
                self.get_movie_list_data(full_url)
    #请求每个分类的每个分页的电影列表数据
    def get_movie_list_data(self,req_url):
        """
        req_url:每一个分页的url地址
        """
        # 构造一个请求头
        req_header = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        }
        # 构建一个request请求对象
        req = request.Request(url=req_url, headers=req_header)
        # 发起请求
        response = request.urlopen(req)
        # 打印状态吗
        print(response.status)
        # 如果请求成功
        if response.status == 200:
            #得到每一页的电影列表，提取每个电影的id,根据id构建电影详细信息的url
            # print(response.read().decode('utf-8'))
            json_str = response.read().decode('utf-8').replace(' ','')
            # print(json_str)
            data = json.loads(json_str)
            print(data)
            movie_list = data['subjects']
            if len(movie_list) > 0:
                for moive in movie_list:
                    id = moive['id']
                    title = moive['title']
                    coverImage = moive['cover']
                    print('正在获取'+title+'的详细信息')
                    #根据id构建电影详细信息的url
                    full_url = 'https://movie.douban.com/j/subject_abstract?subject_id=' + id
                    self.get_movie_detail_info(full_url,coverImage)



                #构造下一页的连接url地址：
                # https://movie.douban.com/j/search_subjects?type=movie&tag=%E6%9C%80%E6%96%B0&page_limit=20&page_start=0
                #获取当前分页的url
                current_url = response.url
                #提取当前分页的page_start偏移量
                pattern = re.compile('.*?page_start=(\d+)',re.S)
                current_satrt = re.findall(pattern,current_url)[0]
                print(current_satrt)
                #在当前url的page_start偏移量基础上加20，得到下一页起始偏移量
                next_start = int(current_satrt)+20
                print(next_start)

                # 将当前分页url的page_start偏移量替换为下一页的起始偏移量,得到完整的下一页url地址
                pattern = re.compile('page_start=\d+')
                next_url = re.sub(pattern,'page_start='+str(next_start),current_url)
                print(next_url)
                self.get_movie_list_data(next_url)
            else:
                print('没有数据了')
                return 


    #获取每一个电影的详细信息
    def get_movie_detail_info(self,req_url,coverImage):
        #构建请求头
        req_header = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
        }
        # 构建一个request请求对象
        req = request.Request(url=req_url, headers=req_header)
        # 发起请求
        response = request.urlopen(req)
        # 打印状态码
        print(response.status)
        # 如果请求成功
        if response.status == 200:
            # 获取电影详细信息相关数据
            data = json.loads(response.read().decode('utf-8'))
            movie_info = {}
            # 电影封面图片
            movie_info['coverimage'] = coverImage
            # 演员信息
            movie_info['actors'] = ','.join(data['subject']['actors'])
            # 时长
            movie_info['duration'] = data['subject']['duration']
            # 评分
            movie_info['rate'] = data['subject']['rate']
            # 来源
            movie_info['region'] = data['subject']['region']
            # 标题
            movie_info['title'] = data['subject']['title']
            # 电影类型
            movie_info['type'] = ','.join(data['subject']['types'])
            # 可播放状态
            movie_info['playable'] = data['subject']['playable']
            # 电影描述
            if len(data['subject']['short_comment']) > 0:
                # 说明有电影评论信息
                movie_info['content'] = data['subject']['short_comment']['content']
            else:
                # 没有评论信息
                movie_info['content'] = '暂无评论'

            # print(movie_info)
            self.write_data_to_db(movie_info)

    def write_data_to_db(self,info):
        '''
        into 要插入数据库的数据　字典类型
        :param info:
        :return:
        '''
        sql = '''
        INSERT INTO movie(%s)
        VALUES (%s)
        '''%(
            ','.join(info.keys()),
            ','.join(['%s']*len(info))

        )
        try:
            self.cursor.execute(sql,[value for key,value in info.items()])
            self.client.commit()
        except Exception as err:
            print(err)
            self.client.rollback()



if __name__ == '__main__':
    dbSpider = DoubanSpider()
    dbSpider.start_spider()






#注意：
#当我们使用json.loads将json字符串转化为python数据类型时
#如果出现：json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
#说明我们的json字符串不是严格意义上的json字符串  json字符串　不符合json规则