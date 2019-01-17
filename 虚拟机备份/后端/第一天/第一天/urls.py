"""第一天 URL Configuration

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
from demoO1 import views
from rest_framework.routers import DefaultRouter

from rest_framework.schemas import get_schema_view
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='图书管理系统')

router = DefaultRouter()
router.register(r'books',views.BookViewSet)
router.register(r'Publisher',views.PublisherViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),


    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'',include(router.urls)),
    url(r'^docs/', schema_view),



]
