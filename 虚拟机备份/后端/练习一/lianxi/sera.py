from rest_framework import serializers
from lianxi import models
class zijidelei(serializers.ModelSerializer):
    class Meta:
        model = models.Publisher
        fields = '__all__'
