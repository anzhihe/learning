from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=10)
    avator = models.ImageField(verbose_name='头像', upload_to='upload/%Y/%m/%d')
