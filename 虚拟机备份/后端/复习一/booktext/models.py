from django.db import models

# Create your models here.


class TypeInfo(models.Model):
    '''
    表示我们的新闻类型
    '''
    #新闻类型的名字
    tname = models.CharField(max_length=20)


class NewsInfo(models.Model):
    '''
    具体的某一则
    '''
    #新闻标题
    ntitle = models.CharField(max_length=50)
    #内容
    ncontent = models.CharField(max_length=30)
    #发布时间
    npub_data = models.DateTimeField(auto_now_add=True)
    #对应时间
    ntype = models.ManyToManyField('TypeInfo')