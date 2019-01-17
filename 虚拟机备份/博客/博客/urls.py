"""博客 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from blogapp import  views
from django.conf import settings
from django.conf.urls.static import static
from blogapp.views import SearchView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'blog_list/(?P<pIndex>[0-9]*)/(?P<category_id>.*)/(?P<cate_type>.*)/(?P<tid>.*)/',views.blog_list,name='blog_list'),
    url(r'^search/',views.SearchView.as_view(),name='search'),
    url(r'^show/(\d+)',views.show,name='show'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^logout/', views.logout),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^tags_list/(?P<tid>\d)',views.blog_list,name='taglist')

]


