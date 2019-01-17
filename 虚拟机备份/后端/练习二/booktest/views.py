
#模型 序列化类
from booktest.models import zeiwang,TutanMing #模型类
from booktest.serializers import TutanMingSerializer,PublisherSerializer  #序列话类
#视图集 先导入模块
from rest_framework import viewsets

class ZeiwangList(viewsets.ModelViewSet):
    '''出版社app'''
    queryset = zeiwang.objects.all()
    serializer_class = PublisherSerializer

class TutanMingLIst(viewsets.ModelViewSet):
    '''图书app'''
    queryset = TutanMing.objects.all()
    serializer_class = TutanMingSerializer






# class ZeiwangList(generics.ListCreateAPIView):
#     queryset = zeiwang.objects.all()
#     serializer_class = PublisherSerializer
#     permission_classes = [IsOwnerOrReadOnly]
#
# class ZeiwangDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = zeiwang.objects.all()
#     serializer_class = PublisherSerializer
#     permission_classes = [IsOwnerOrReadOnly]
#
#
#
# class TutanMingLIst(generics.ListCreateAPIView):
#     queryset = TutanMing.objects.all()
#     serializer_class = TutanMingSerializer
#
#
# class TutanMingDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = TutanMing.objects.all()
#     serializer_class = TutanMingSerializer








