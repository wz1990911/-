from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from blogapp.models import Banner, Post, BlogCategory,FriendlyLink,Tags
from django.views.generic.base import View
from django.db.models import Q
# Create your views here.
from blogapp.models import *
from .models import User
from blogapp.forms import UserForm,RegisterForm
from django.core.paginator import Paginator
# Create your views here.


class SearchView(View):
    def get(self,request):
        pass
    def post(self,request):
        keyword = request.POST.get('keyword')
        return redirect(reverse('blog_list', kwargs={'category_id':keyword ,'cate_type':'ss','pIndex':1,'tid':-1}))


def index(request):
    banner_list = Banner.objects.all()
    recomment_list = Post.objects.all()
    biog_list = Post.objects.all().order_by('-pub_date')
    categroy_list = BlogCategory.objects.all()
    friendlyLink_list = FriendlyLink.objects.all()
    new_comment_list = Post.objects.filter(comment__content__isnull=False)
    new_comment_list2 = []
    for blog in new_comment_list:
        if blog in new_comment_list2:
            pass
        else:
            new_comment_list2.append(blog)

    return render(request, 'index.html', locals())

def blog_list(request,pIndex,category_id,cate_type,tid):

    tags_list = Tags.objects.all()


    title = '全部博客'
    new_comment_list = Post.objects.filter(comment__content__isnull=False)
    new_comment_list2 = []
    for blog in new_comment_list:
        if blog in new_comment_list2:
            pass
        else:
            new_comment_list2.append(blog)



    if cate_type == 'ss':
        list1 = Post.objects.filter(Q(title__contains=category_id) | Q(content__contains=category_id))

        p = Paginator(list1, 3)
        # 如果当前没有传递页码信息，则认为是第一页，这样写是为了请求第一页时可以不写页码
        if pIndex == '':
            pIndex = '1'
        # 通过url匹配的参数都是字符串类型，转换成int类型
        pIndex = int(pIndex)
        # 获取第pIndex页的数据
        blogs = p.page(pIndex)
        # 获取所有的页码信息


        plist = p.page_range

    else:
        if category_id == '0':


            # 查询所有的博客信息
            list1 = Post.objects.all()
            # 将地区信息按一页10条进行分页
            p = Paginator(list1, 3)
            # 如果当前没有传递页码信息，则认为是第一页，这样写是为了请求第一页时可以不写页码
            if pIndex == '':
                pIndex = '1'
            # 通过url匹配的参数都是字符串类型，转换成int类型
            pIndex = int(pIndex)
            # 获取第pIndex页的数据
            blogs = p.page(pIndex)
            # 获取所有的页码信息
            plist = p.page_range
        else:
            category_id = int(category_id)
            blogs = BlogCategory.objects.get(id = category_id).post_set.all()
            title = BlogCategory.objects.get(id = category_id).name
        print(blogs)
    if cate_type=='jjj':
        a = Tags.objects.get(id=tid)
        b = a.name
        blogs = Post.objects.filter(tags__name=b)

    else:
        pass

    return  render(request,'list.html',locals())


def show(request,blog_id):
    print(blog_id)
    blog =Post.objects.get(id=blog_id)
    print(blog.title)
    blog.views +=1
    blog.save()
    new_comment_list = Post.objects.filter(comment__content__isnull=False)
    new_comment_list2 = []
    for blog in new_comment_list:
        if blog in new_comment_list2:
            pass
        else:
            new_comment_list2.append(blog)


    return  render(request,'show.html',locals())



def login(request):
    #不允许重复登录
    if request.session.get('is_login',None):
        return redirect('/index/')
    if request.method == 'POST':
        login_form = UserForm(request.POST)
        message = '请检查填写内容'
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = User.objects.get(name=username)
                if user.password == password:
                    #通过下面三句话　往session字典里面写入用户状态和数据
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/index/')
                else:
                    message = '密码不正确'
            except:
                message = '用户不存在'

        return render(request,'login.html',locals())
    login_form = UserForm()
    return render(request,'login.html',locals())





def register(request):
    if request.session.get("is_login",None):
        #登录状态不允许注册。你可以修改这条原则！
        return redirect('/index/')
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        message = '请检查填写内容'
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:
                message = '两次输入的密码不同'
                return render(request,'register.html',locals())
            same_email_user = User.objects.filter(name = username)
            if same_email_user:
                message = '用户已经存在，请重新选择用户名'
                return render(request,'register.html',locals())
            same_email_user = User.objects.filter(email=email)
            if same_email_user:
                message = '该邮箱地址已被注册，请使用别的邮箱'
                return render(request,'login/regiseter.html',locals())
            #当一切都ok的情况下，创建新用户
            new_user = User()
            new_user.name = username
            new_user.password = password1
            new_user.email = email
            new_user.sex = sex
            new_user.save()
            return redirect('/login/') #自动跳转到登录页面

    #实例化一个表单对象
    register_form = RegisterForm()
    return render(request, 'register.html',locals())
def logout(request):
    """退出登录后重定向到首页"""
    if not request.session.get('is_login', None):
        # 如果本来就未登录,也就没有登出一说
        return redirect('/index/')
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']

    return redirect("/index/")






