# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-10 03:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('denglu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='user_type',
            field=models.CharField(choices=[(1, '普通用户'), (2, 'vip'), (3, 'svip')], max_length=64, verbose_name='用户类型'),
        ),
    ]
