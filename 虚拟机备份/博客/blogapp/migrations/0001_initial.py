# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-12 12:12
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isDelete', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('cover', models.ImageField(upload_to='static/images/banner', verbose_name='轮播图')),
                ('link_url', models.URLField(max_length=100, verbose_name='图片链接')),
                ('idx', models.IntegerField(verbose_name='索引')),
                ('is_active', models.BooleanField(default=False, verbose_name='是否是active')),
            ],
            options={
                'verbose_name_plural': '轮播图',
                'verbose_name': '轮播图',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isDelete', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('name', models.CharField(default='', max_length=20, verbose_name='分类名称')),
            ],
            options={
                'verbose_name_plural': '博客分类',
                'verbose_name': '博客分类',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isDelete', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(verbose_name='发布时间')),
                ('content', models.TextField(verbose_name='内容')),
            ],
            options={
                'verbose_name_plural': '评论',
                'verbose_name': '评论',
            },
        ),
        migrations.CreateModel(
            name='FriendlyLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('link', models.URLField(default='', max_length=50, verbose_name='链接')),
            ],
            options={
                'verbose_name_plural': '友情链接',
                'verbose_name': '友情链接',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isDelete', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('content', tinymce.models.HTMLField(verbose_name='内容')),
                ('cover', models.ImageField(default=None, upload_to='static/images/post', verbose_name='博客封面')),
                ('views', models.IntegerField(default=0, verbose_name='浏览数')),
                ('recommend', models.BooleanField(default=False, verbose_name='推荐博客')),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blogapp.BlogCategory', verbose_name='博客分类')),
            ],
            options={
                'verbose_name_plural': '博客',
                'verbose_name': '博客',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20, verbose_name='标签名称')),
            ],
            options={
                'verbose_name_plural': '标签',
                'verbose_name': '标签',
            },
        ),
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=32)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '用户',
                'ordering': ['-c_time'],
                'verbose_name': '用户',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='blogapp.Tags', verbose_name='标签'),
        ),
    ]
