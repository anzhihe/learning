from django.db import models


# Create your models here.
class Group(models.Model):
    name = models.CharField(verbose_name='小组名字', max_length=5)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(verbose_name='学生名字', max_length=10)
    age = models.IntegerField(verbose_name='学生年龄')
    group = models.ForeignKey(to=Group, on_delete=models.CASCADE)
