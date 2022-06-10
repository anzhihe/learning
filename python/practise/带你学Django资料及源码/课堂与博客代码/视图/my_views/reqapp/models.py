from django.db import models


# Create your models here.
class User(models.Model):
    phone = models.CharField(verbose_name='手机号', max_length=11)
    pwd = models.CharField(verbose_name='密码', max_length=64)
    gender = models.CharField(verbose_name='性别', max_length=3)
    hobby = models.CharField(verbose_name='爱好', max_length=128)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
