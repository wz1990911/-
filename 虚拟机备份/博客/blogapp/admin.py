from django.contrib import admin
from blogapp.models import Banner,Post,Tags,BlogCategory,FriendlyLink,Comment
from .models import User
from django.contrib import admin
from blogapp.models import *
# Register your models here.
admin.site.register(Banner)
admin.site.register(Post)
admin.site.register(Tags)
admin.site.register(BlogCategory)
admin.site.register(FriendlyLink)
admin.site.register(Comment)
admin.site.register(User)
# class GoodsInfoAdmin(admin.ModelAdmin):
#     list_display = ['id']
# admin.site.register(GoodsInfo,GoodsInfoAdmin)