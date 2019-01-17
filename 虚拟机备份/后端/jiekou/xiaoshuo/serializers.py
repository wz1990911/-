# 一个模块serializers是大润发系列话模块
from rest_framework import serializers
from xiaoshuo import models


class FenleiSerial(serializers.ModelSerializer):

    class Meta:
        model = models.Fenlei  # 我们要使用的模型

        # 我们要使用的字段
        fields = (
            "__all__"
        )

class BiaotiSerial(serializers.ModelSerializer):

    class Meta:
        model = models.Biaoti  # 我们要使用的模型

        # 我们要使用的字段
        fields = (
            "__all__"
        )

class TshujianjieSerial(serializers.ModelSerializer):

    class Meta:
        model = models.Tshujianjie  # 我们要使用的模型

        # 我们要使用的字段
        fields = (
            "__all__"
        )

class ZhangjieMingSerial(serializers.ModelSerializer):

    class Meta:
        model = models.ZhangjieMing  # 我们要使用的模型

        # 我们要使用的字段
        fields = (
            "__all__"
        )

class ContentSerial(serializers.ModelSerializer):

    class Meta:
        model = models.Content  # 我们要使用的模型

        # 我们要使用的字段
        fields = (
            "__all__"
        )


