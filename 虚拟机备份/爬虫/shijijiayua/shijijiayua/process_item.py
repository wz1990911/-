#将数据从redis数据库中取出,存如mongodb数据库
import pymongo
import redis
import json
import pymysql

def get_redis_data_to_mongodb():
    #创建redis数据库链接
    redis_cli = redis.StrictRedis('127.0.0.1',6379)
    #创建mongodb数据库链接
    mongo_cli = pymongo.MongoClient('127.0.0.1',27017)
    db = mongo_cli['shijijiayuan']
    col = db['sjjy']

    while True:
        key,data = redis_cli.blpop('sjjy:items',timeout=10)
        #data取出来的是一个二进制(bytes)数据类型
        data = data.decode('utf-8')
        data = json.loads(data)

        try:
            col.insert(data)
            print('插入成功')

        except Exception as err:
            print(err,'插入失败')


def get_redis_data_to_mysql():
    #创建redis数据库链接
    redis_cli = redis.StrictRedis('127.0.0.1',6379)
    #创建mysql数据库链接
    mysql_cli = pymysql.Connect('127.0.0.1','root','1','shijijiayuan',charset='utf8')
    cursor = mysql_cli.cursor()

    while True:
        key,data = redis_cli.blpop('sjjy:items',timeout=10)
        #data取出来的是一个二进制(bytes)数据类型
        data = data.decode('utf-8')
        data = json.loads(data)

        try:
            sql = '''
            INSERT INTO sjjy(%s)
            VALUES (%s)
            '''%(','.join(data.keys()),
                 ','.join(['%s']*len(data))
                 )
            cursor.execute(sql,list(data.values()))
            mysql_cli.commit()
            print('插入成功')

        except Exception as err:
            print(err,'插入失败')
            mysql_cli.rollback()



if __name__ == '__main__':
    get_redis_data_to_mongodb()
    get_redis_data_to_mysql()