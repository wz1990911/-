from django.contrib import admin

# Register your models here.
from xiaoshuo.models import Fenlei,Biaoti,Tshujianjie,ZhangjieMing,Content
admin.site.register(Fenlei)
admin.site.register(Biaoti)
admin.site.register(Tshujianjie)
admin.site.register(ZhangjieMing)
admin.site.register(Content)