from  django.db import models


class BaseModel(models.Model):
    isDelete = models.BooleanField(default=False)
    pub_date = pub_date = models.DateTimeField('创建时间',auto_now_add=True)
    class Meta:
        abstract = True