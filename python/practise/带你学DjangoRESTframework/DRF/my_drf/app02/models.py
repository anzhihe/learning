from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(verbose_name='分类', max_length=10)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(verbose_name='标签名字', max_length=10)
    created_time = models.DateTimeField()

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(verbose_name='标题', max_length=100)
    vum = models.IntegerField(verbose_name='浏览量')
    content = models.TextField(verbose_name='内容')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='articles')
    tags = models.ManyToManyField(to=Tag, related_name='articles')

    def __str__(self):
        return self.title
