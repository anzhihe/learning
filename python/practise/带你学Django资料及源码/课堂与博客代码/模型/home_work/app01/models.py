from django.db import models


# Create your models here.

class Person(models.Model):
    edus = (
        (0, '小学'),
        (1, '初中'),
        (2, '高中'),
        (3, '本科'),
        (4, '硕士'),
        (5, '博士'),
    )
    genders = (
        (0, '男'),
        (1, '女'),
        (2, '未知'),
    )
    name = models.CharField(verbose_name='名字', max_length=10, null=False)
    age = models.IntegerField(verbose_name='年龄')
    edu = models.IntegerField(verbose_name='学历', choices=edus)
    gender = models.IntegerField(verbose_name='性别', choices=genders)
    hobby = models.TextField(verbose_name='爱好')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '简历'
        verbose_name_plural = verbose_name
