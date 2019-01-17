from django.db import models
from models_tool.basemodel import BaseModel
from userapp.models import BlogUser
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Banner(BaseModel):
    title = models.CharField('标题', max_length=50)
    cover = models.ImageField('轮播图', upload_to='static/images/banner')
    link_url = models.URLField('图片链接', max_length=100)
    idx = models.IntegerField('索引')
    is_active = models.BooleanField('是否是active', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图'


class BlogCategory(BaseModel):
    name = models.CharField('分类名称', max_length=20, default='')

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = '博客分类'

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField('标签名称', max_length=20, default='')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'

    def __str__(self):
        return self.name


class Post(BaseModel):
    user = models.ForeignKey(BlogUser, verbose_name='作者')
    category = models.ForeignKey(BlogCategory, verbose_name='博客分类', default=None)
    tags = models.ManyToManyField(Tags, verbose_name='标签')
    title = models.CharField('标题', max_length=50)
    content = HTMLField('内容')
    # pub_date = models.DateTimeField('发布日期', default=datetime.now)
    cover = models.ImageField('博客封面', upload_to='static/images/post', default=None)
    views = models.IntegerField('浏览数', default=0)
    recommend = models.BooleanField('推荐博客', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = '博客'


class Comment(BaseModel):
    post = models.ForeignKey(Post, verbose_name='博客')
    user = models.ForeignKey(BlogUser, verbose_name='作者')
    pub_date = models.DateTimeField('发布时间')
    content = models.TextField('内容')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'


class FriendlyLink(models.Model):
    title = models.CharField('标题', max_length=50)
    link = models.URLField('链接', max_length=50, default='')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = '友情链接'

class TestModel(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextUploadingField()



class User(models.Model):
    # 性别
    gender = (
        ('male', '男'),
        ('female', '女')
    )

    name = models.CharField(max_length=128, unique=True)
    # 密码建议最少128位
    password = models.CharField(max_length=128)
    # 内置邮箱字段,并且唯一
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # 使用str帮助人性化显示对象信息
        return self.name

    class Meta:
        # (元选项/元信息/元数据)里面定义用户按照时间的反序排列
        ordering = ['-c_time']
        verbose_name = '用户'
        verbose_name_plural = verbose_name
