"""jiekou URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from xiaoshuo import views
from rest_framework.schemas import get_schema_view
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
# from .models import Fenlei,Biaoti,Tshujianjie,ZhangjieMing,Content
from rest_framework_swagger.views import get_swagger_view

router = DefaultRouter()
router.register(r'fenlei', views.FenleiViewSt)
router.register(r'biaoti', views.BiaotiViewSt)
router.register(r'tshujian', views.TshujianViewSt)
router.register(r'zhangjie', views.ZhangjieViewSt)
router.register(r'content', views.ContentViewSt)

schema_view = get_swagger_view(title='书')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'index/', views.PublisherList.as_view()),

    url(r'api/', schema_view),
    url(r'^docs/', include_docs_urls(title='小说')),
    url(r'', include(router.urls)),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
