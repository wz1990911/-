# from django.shortcuts import render
# from django.http import HttpResponse
#
# from django.forms import model_to_dict  #可以砖字典f
# from django.core import serializers  #django 提供序列化类
# #本质上是
# from demoO1 import seriazers
#
# from demoO1.models import Publisher
#
# #导入一个DRF 的响应框架 继承
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status
# import json
# # Create your views here.
#
# #请求和响应 请求 (客户端) Get post
# #实际的梨子  现在我要请求什么  展示所有出版信息
#
# #@api_view 让我们普通师徒成为一个drf视图 被允许请求的方式
# @api_view(['GET'])
# def publishers(request):
#     #可以先判端前端工程师个我们穿过来的请求
#     if request.method == "GET":
#         s_list = Publisher.objects.all()
#         #序列化
#         s = seriazers.PubliserSerial(s_list,many=True)
#         #返回响应
#         return Response(s.data)
#     #当用户提交一个新的出版设的时候 前端工程师 新怎一个资源
#     if request.method == "POST":
#
#         s = seriazers.PubliserSerial(data=request.data)
#         if s.is_valid():#校验数据
#             s.save()
#             return Response(status=status.HTTP_201_CREATED)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#
#
# #刚刚我们是获取所有数据 和提交一个新的数据
# #新的需求 是更新删除获取一个单个出版社
#
# @api_view(['GET','PUT','DELETE'])
# def publisher_detail(request,pk):
#     #get   更新 put  删除 delete
#     try:
#         p = Publisher.objects.get(pk=pk)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#
#     #获取单个出版社
#     if request.method =='GET':
#
#         s = seriazers.PubliserSerial(p)
#         return Response(s.data,status.HTTP_201_CREATED)
#
#
#     #跟新某个出版社
#     if request.method == 'PUT':
#         #第一个参数是模型类对象 你要修改的出版设  前段要修改的内容
#         s = seriazers.PubliserSerial(p,data=request.data)
#
#         if s.is_valid():
#             s.save()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         else:
#             return Response(status=status.HTTP_200_OK)
#         pass
#     if request.method == 'DELETE':
#         #删除出版社
#         p.delete()
#         #删除成功
#         return Response(status=status.HTTP_200_OK)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# '''
#     def publisher(request):
#
#     #p_list 是一个列表这个列表里面装这一个个对象每一个对象就是数据库的以条数据
#     p_list = Publisher.objects.all()
#
#     #将数据系列化
#     # s=serializers.serialize('json',p_list)
#     s =seriazers.PubliserSerial(p_list,many=True)
#
#     # #能去打数据对象--->json  dict--->json
#     # data = []  #最终砖话程字典的列表
#     # for p in p_list:
#     #     d = {
#     #         'title':p.title,
#     #         'address':p.address
#     #     }
#     #     data.append(d)
#     # #进行序列化 s就是一个json字符串
#     # #你就可以把他作为数据进型传输
#     # s = json.dumps(data)
#     # return  Response(s.data)
# '''


# ==============================================================

#基于类的视图 响应 状态吗

#基于类的视图
from rest_framework import permissions
from rest_framework.views import APIView

#基于函数的视图
#from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework import status

#模型 序列化类
from demoO1.models import Publisher,Book #模型类

from demoO1.seriazers import PubliserSerial,BookSerializers  #序列话类
#要想使用混合视图我们需要先导入
from rest_framework import mixins
from rest_framework import generics
from demoO1 import permissions
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
# from

#视图集 先导入模块
from rest_framework import viewsets

class PublisherViewSet(viewsets.ModelViewSet):
    '''出版社app'''
    queryset = Publisher.objects.all()
    serializer_class = PubliserSerial

class BookViewSet(viewsets.ModelViewSet):
    '''图书app'''
    queryset = Book.objects.all()
    serializer_class = BookSerializers





'''
#浏览api
@api_view(['GET'])
def api_root(request,format=None):
    return Response(
        {
            'publishers': reverse('publisher-list',request=request, format=format),
            'books': reverse('book-list',request=request,format=format)
        }
    )


#在自定义权限之前我们西安将 def这个框架给我们提供和的权限

class PublisherList(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PubliserSerial
    permission_classes = [permissions.IsOwnerOrReadOnly]

class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PubliserSerial
    permission_classes = [permissions.IsOwnerOrReadOnly]

class Booklist(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    # permission_classes = [permissions.IsOwnerOrReadOnly]

class BookDelist(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    # permission_classes = [permissions.IsOwnerOrReadOnly]
'''













#
# class Publisherlist(APIView):
#     #get 获取所有出版设信息
#     def get(self,request):
#         #先从数据库里面取出所有出版社相关的数据
#         queryset = Publisher.objects.all()
#         #序列话
#         s = PubliserSerial(queryset,many=True)
#         #返回数据
#         return Response(s.data,status=status.HTTP_200_OK)
#
#
#     #post  获取单个出版社信息
#     def post(self,request):
#         #提交数据　把数据袋到出版社相关数据
#         s = PubliserSerial(data=request.data)
#         if s.is_valid():
#             s.save() #保存数据库
#             return Response(s.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(s.errors,status=status.HTTP_404_NOT_FOUND)
#
#
# #修改删除单个　出版社信息
# class PublisherDetail(APIView):
#     def get_object(self,pk):
#         # 查数据库:用来获取具体的某一个出版社信息 容错
#         try:
#             p =Publisher.objects.get(pk=pk)
#             return p
#         except Publisher.DoesNotExist:  #捕捉精准的某一个错误
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#     #获取GET 删除DELETE 修改PUT
#     def get(self,request,pk):
#         p = self.get_object(pk)
#         s = PubliserSerial(p)
#         return Response(s.data,status=status.HTTP_200_OK)
#
#     def PUT(self,request,pk):
#         #先取数据 request.data
#         s = PubliserSerial(data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#
#     def delete(self,request,pk):
#         #删除数据 先找到你要删除的数据
#         p = self.get_object(pk)
#         p.dekete()
#         return Response(status=status.HTTP_200_OK)
#
#








