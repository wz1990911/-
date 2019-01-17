from django.shortcuts import render,redirect

from django.http import *
from .models import User1
import random

def index_wz(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        message = '所有字段都必须填写'

        if username and password:
            username = username.strip()

            try:
                user = User1.objects.get(name=username)
                if user.password == password:
                    message = '登陆成功'
                    #return redirect('/user/ok/')
                else:
                    message = '密码不正确'
            except:
                message = '用户名不存在'
        return render(request, 'signup.html', {'message': message})
    else:
        return render(request, 'index.html')

def signup_wz(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:  # 判断两次密码是否相同
            message = "两次输入的密码不同！"
            return render(request, 'signup.html', locals())
        else:
            same_name_user = User1.objects.filter(name=username)
            if same_name_user:  # 用户名唯一
                message = '用户已经存在，请重新选择用户名！'
                return render(request, 'signup.html', locals())

                # 当一切都OK的情况下，创建新用户


            new_user = User1()
            new_user.name = username
            new_user.password = password1

            new_user.save()
            return redirect('/user/index/')  # 自动跳转到登录页面
    else:
        return render(request, 'signup.html', locals())



