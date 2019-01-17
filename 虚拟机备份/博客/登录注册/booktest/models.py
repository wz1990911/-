from django.db import models

# Create your models here.
class Register_Model(models.Model):
    account = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    isActivate = models.BooleanField(default=False)
    activate_code = models.IntegerField()