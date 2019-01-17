import pymongo

from bson.objectid import  ObjectId

#创建一个mongd的客户端链接
mongo_client = pymongo.MongoClient(
    host = "127.0.0.1",
    port = 27017
)
#切换到指定数据库
# db = mongo_client.mongo1805
db = mongo_client['mongo1805']
#使用集合(存在直接使用,不存在就直接创造)
col_name = db['students']
def insert_data():
    document2 = {
        'name':'xk',
        'num':'110',
        'gender':'1'
    }
    document1 = {
        'name': 'xk2',
        'num': '110',
        'gender': '1'
    }

    result = col_name.insert([document2,document1])
    print(result)
    # remover_data()

def remover_data():
    #,ulti = True,表示删除多条
    resuly = col_name.remove({'name':'xk'})
    #删出一条
    resuly = col_name.remove({'name': 'xk'},multi=False)

    #删除一条
    col_name.delete_one()
    #删除多条
    col_name.delete_many()

    print(resuly)
def update_data():
    #指定属性更新
    col_name.update({'name':'xk2'},{'$set':{'name':'xk3000'}})






















    [
















    ]

insert_data()
if __name__ == '__main__':

    update_data()


