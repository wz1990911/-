from django.db import models

# Create your models here.
class UserInfo(models.Model):
    type = (
        (1,'普通用户'),
        (2,'vip'),
        (3,'svip'),
    )

    user_type = models.CharField(max_length=64,choices=type,verbose_name="用户类型")
    username = models.CharField(max_length=64,verbose_name='用户名',unique=True)
    password = models.CharField(max_length=256,verbose_name='密码')


class UserToken(models.Model):
    user = models.OneToOneField(UserInfo)
    token = models.CharField(max_length=256)