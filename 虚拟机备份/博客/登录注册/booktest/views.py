from django.shortcuts import render,redirect
from .models import Register_Model
# Create your views here.
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.core.urlresolvers import reverse
import random
...
def send(request):
    msg='<a href="#" target="_blank">点击激活</a>'
    send_mail('注册激活','',settings.EMAIL_FROM,
                ['wz990911@163.com'],
                html_message=msg)
    return HttpResponse('ok')

def register(request):
    return render(request,'register.html')



def register_handle(request):
    account = request.POST.get('account')
    pwd1 = request.POST.get('pwd1')
    pwd2 = request.POST.get('pwd2')
    if pwd1 != pwd2:
        return redirect('/register/')
    else:
        try:
            a = Register_Model.objects.get(account=account)
            return HttpResponse('对不起,账号已存在')
        except:
            a = Register_Model()
            a.account = account
            a.password = pwd1
            actiavte_code = random.randint(1,19)
            a.activate_code = actiavte_code
            a.save()
            msg ='<a href={}/{}>点击注册</a>'.format('127.0.0.1:8000/activate',actiavte_code)
            send_mail('注册激活','',settings.EMAIL_FROM,['WZ990911@163.COM'],html_message=msg)
            return HttpResponse('ok')
def actiavte(request,activate):
    try:
        a = Register_Model.objects.get(activate_code=activate)
        a.isActivate = True
        a.save()
        return HttpResponse('激活成功')
    except:
        return HttpResponse('验证码不对')