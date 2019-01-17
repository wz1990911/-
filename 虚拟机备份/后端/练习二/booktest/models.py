from django.db import models

# Create your models here.

class zeiwang(models.Model):
    name = models.CharField(max_length=30,verbose_name='名字')
    set = models.BooleanField(default=True)
    guoshi = models.CharField(max_length=30,verbose_name='果实')
    # 操作者
    operator = models.ForeignKey('auth.User')
    def __str__(self):
        return self.name


    class Meta:
        verbose_name = '人物信息'
        verbose_name_plural = verbose_name

class TutanMing(models.Model):
    title = models.CharField(max_length=30,verbose_name='海贼团名')
    zeiwang = models.ForeignKey('zeiwang')


    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '团名'
        verbose_name_plural = verbose_name





