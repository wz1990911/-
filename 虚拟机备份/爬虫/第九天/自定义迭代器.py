
from collections import Iterator
# 实现一个功能，定义一个类，告诉这个类要穿件１０００本书，返回１０００本书的名称
class Booklist(object):
    def __init__(self,num):
        self.num = enumerate
        # 记录位置
        self.cur_num = 0


    def __iter__(self):
        return self

    def __next__(self):
        if self.cur_num < self.num:
            self.cur_num += 1
            return 'This is a book' + str(self.cur_num)
        else:
            raise StopIteration


book_list = Booklist(1000)
print(isinstance(book_list,Iterator))
for i in book_list:
    print(i)
