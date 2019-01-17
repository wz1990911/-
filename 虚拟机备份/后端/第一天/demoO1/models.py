from django.db import models

# Create your models here.
#ORM 模型类相当与数据库里的一张表
class Publisher(models.Model):
    """出版社"""
    title = models.CharField(max_length=100,verbose_name='标题')
    address = models.CharField(max_length=200 ,verbose_name='出版社地址')

    #操作者
    operator = models.ForeignKey('auth.User')
    def __str__(self):
        #人性化显示
        return self.title
    class Meta:
        verbose_name = '出版社'
        verbose_name_plural = verbose_name

class Book(models.Model):
    """书"""
    title = models.CharField(max_length=32,verbose_name='书名')
    publisher = models.ForeignKey('Publisher')

    def __srt__(self):
        #人性化显示
        return self.title

    class Meta:
        #界面显示
        verbose_name = '书'
        verbose_name_plural = verbose_name
