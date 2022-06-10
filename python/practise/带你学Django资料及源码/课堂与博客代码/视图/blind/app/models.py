from django.db import models


# Create your models here.


class User(models.Model):
    genders = (
        (0, '男'),
        (1, '女')
    )
    phone = models.CharField(verbose_name='手机号', max_length=11, unique=True, null=False)
    nickname = models.CharField(verbose_name='昵称', max_length=15, null=False)
    pwd = models.CharField(verbose_name='密码', max_length=64, null=False)
    gender = models.CharField(verbose_name='性别', choices=genders, null=False, max_length=10)
    hobby = models.CharField(verbose_name='爱好', max_length=255, null=False)
    avator = models.ImageField(verbose_name='头像', upload_to='upload/%Y/%m/%d')
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name='创建时间', auto_now=True)

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
