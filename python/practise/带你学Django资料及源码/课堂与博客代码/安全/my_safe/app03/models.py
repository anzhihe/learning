from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(verbose_name='名字', max_length=100)
