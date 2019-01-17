from django.shortcuts import render
from django.http import HttpResponse

from django.views import View


# Create your views here.
class StudentsView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("GET")

    def post(self, request, *args, **kwargs):
        return HttpResponse("POST")

    def put(self, request, *args, **kwargs):
        return HttpResponse("PUT")

    def delete(self, request, *args, **kwargs):
        return HttpResponse("DELETE")
