from django.db import models

# Create your models here.
class Fenlei(models.Model):
    fenlei = models.CharField(max_length=20,verbose_name='分类')

    def __str__(self):
        return self.fenlei


    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

class Biaoti(models.Model):
    flbt = models.CharField(max_length=20,verbose_name='分类标题')
    title = models.CharField(max_length=20,verbose_name='书名')
    # leibie = models.ForeignKey(Fenlei)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "书名"
        verbose_name_plural = verbose_name

class Tshujianjie(models.Model):
    image = models.CharField(max_length=255,verbose_name="图片")
    jianjie = models.CharField(max_length=255,verbose_name="简介")
    name = models.CharField(max_length=25,verbose_name="作者")
    zhuangtai = models.CharField(max_length=255,verbose_name="状态")
    zishu = models.CharField(max_length=20,verbose_name="字数")



    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "作者"
        verbose_name_plural = verbose_name

class ZhangjieMing(models.Model):
    zhangjie = models.CharField(max_length=20,verbose_name='章节名字')
    #外检关系没写
    def __str__(self):
        return self.zhangjie

    class Meta:
        verbose_name = "章节"
        verbose_name_plural = verbose_name


class Content(models.Model):
    content = models.TextField(verbose_name="内容")
    # shu = models.ForeignKey(Tshujianjie)

    class Meta:
        verbose_name = "内容"
        verbose_name_plural = verbose_name




