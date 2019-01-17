

from django.conf.urls import url,include
from django.contrib import admin
from booktest import views
from rest_framework.routers import DefaultRouter

from rest_framework.schemas import get_schema_view
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='图书管理系统')

router = DefaultRouter()
router.register(r'books',views.TutanMingLIst)
router.register(r'Publisher',views.ZeiwangList)

urlpatterns = [
    url(r'^admin/', admin.site.urls),


    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'',include(router.urls)),
    url(r'^docs/', schema_view),



]