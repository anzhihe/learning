from django.db import models


# Create your models here.

class Goods(models.Model):
    name = models.CharField(verbose_name='商品名字', max_length=100)
    content = models.TextField(verbose_name='商品名字')
