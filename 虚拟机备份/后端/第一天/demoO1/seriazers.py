# 一个模块serializers是大润发系列话模块
from rest_framework import serializers
from demoO1 import models


class PubliserSerial(serializers.ModelSerializer):
    # 读取用户名
    # operator = serializers.ReadOnlyField(source='operator.username')
    class Meta:
        model = models.Publisher  # 我们要使用的模型

        # 我们要使用的字段
        fields = (
            "__all__"
        )


class BookSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:

        model = models.Book

        # 我们要使用的字段
        fields = ("__all__")


