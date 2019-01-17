from django.shortcuts import render, redirect
from .models import wz
from django.http import HttpResponse


# Create your views here.
def wz_index(request):
    return render(request, 'index.html')


def tijiao_zt(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    comment = request.POST.get('comment')

    z = wz()
    z.name = name
    z.email = email
    z.phone = phone
    z.comment = comment
    z.save()
    return redirect('show')


def show(request):
    z = wz.objects.all()

    return render(request, 'show_zt.html', locals())

