from rest_framework import serializers
from booktest import models


class PublisherSerializer(serializers.ModelSerializer):
    # 读取用户名
    # operator = serializers.ReadOnlyField(source='operator.username')
    class Meta:
        model = models.zeiwang  # 我们要使用的模型

        # 我们要使用的字段
        fields = "__all__"

class TutanMingSerializer(serializers.HyperlinkedModelSerializer):
    # hzeiwang = serializers.StringRelatedField(source='hzeiwang.name')

    class Meta:
        model = models.TutanMing
        fields = "__all__"

