from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Fenlei, Biaoti, Tshujianjie, ZhangjieMing, Content
from xiaoshuo import serializers
from rest_framework.views import APIView


# Create your views here.
def index(request):
    return HttpResponse('ok')


class FenleiViewSt(viewsets.ModelViewSet):
    queryset = Fenlei.objects.all()
    serializer_class = serializers.FenleiSerial


class BiaotiViewSt(viewsets.ModelViewSet):
    queryset = Biaoti.objects.all()
    serializer_class = serializers.BiaotiSerial


class TshujianViewSt(viewsets.ModelViewSet):
    queryset = Tshujianjie.objects.all()
    serializer_class = serializers.TshujianjieSerial


class ZhangjieViewSt(viewsets.ModelViewSet):
    queryset = ZhangjieMing.objects.all()
    serializer_class = serializers.ZhangjieMingSerial


class ContentViewSt(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = serializers.ContentSerial


class PublisherList(APIView):
    def get(self, request, format=None):
        queryset = Content.objects.all()  # 查询出所有出版社


        return HttpResponse('ok')
