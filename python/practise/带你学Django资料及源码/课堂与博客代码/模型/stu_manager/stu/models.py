from django.db import models


# Create your models here.


class Grades(models.Model):
    name = models.CharField(verbose_name='班级名字', max_length=10)

    created_time = models.DateTimeField(auto_now_add=True)

    update_time = models.DateTimeField(auto_now=True)


class Student(models.Model):
    name = models.CharField(verbose_name='学生姓名', max_length=10)
    age = models.IntegerField(verbose_name='学生年龄')


    # 数据源
    genders = (
        (0, '男'),
        (1, '女'),
        (2, '未知'),
    )
    gender = models.IntegerField(verbose_name='性别', choices=genders)

    created_time = models.DateTimeField(auto_now_add=True)  # 创建时间

    update_time = models.DateTimeField(auto_now=True)  # 更新时间

    grades = models.ForeignKey(to=Grades, on_delete=models.CASCADE)
