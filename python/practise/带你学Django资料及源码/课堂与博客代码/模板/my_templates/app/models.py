from django.db import models


# Create your models here.

class Dog(models.Model):
    name = models.CharField(verbose_name='名字', max_length=10)
    age = models.IntegerField(verbose_name='年龄')
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '狗'
        verbose_name_plural = verbose_name

    def gender(self):
        return '母'
