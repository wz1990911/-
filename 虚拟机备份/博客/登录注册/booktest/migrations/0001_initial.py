# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-28 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=256)),
                ('password', models.CharField(max_length=256)),
                ('isActivate', models.BooleanField(default=False)),
            ],
        ),
    ]
