from django.db import models


# Create your models here.
# ORM 模型类相当与数据库里的一张表
class Publisher(models.Model):
    name = models.CharField(max_length=100, verbose_name='名字')
    address = models.CharField(max_length=200, verbose_name='地址')
    nianlin = models.CharField(max_length=200,verbose_name='年龄')
