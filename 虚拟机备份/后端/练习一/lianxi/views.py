from django.shortcuts import render
from django.http import HttpResponse
from .models import Publisher
import json
from lianxi import sera
# Create your views here.
from django.core import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET'])
def Xikailianxi(request):
    if request.method == 'GET':
        querysel = Publisher.objects.all()

        s = sera.zijidelei(querysel, many=True)
        return Response(s.data)


@api_view(['GET', 'POST', 'PUT', 'DETELE'])
def publishers(request):
    p = Publisher.objects.all()
    s = sera.zijidelei(p, many=True)
    if request.method == 'GET':
        return Response(s.data)
    elif request.method == 'POST':
        s = sera.zijidelei(data=p.data)
        if s.is_valid():
            return Response(s.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_402_PAYMENT_REQUIRED)


@api_view(['GET', 'POST', 'PUT', 'DETELE'])
def publisher_delail(request, p):
    try:
        c = Publisher.objects.get(pk=p)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        s = sera.zijidelei(c)
        return Response(s.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        s = sera.zijidelei(c, data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_200_OK)
    if request.method == 'DETELE':
        c.delete()
        return Response(status=status.HTTP_200_OK)
