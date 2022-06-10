from django.db import models
from datetime import datetime


# Create your models here.


class Category(models.Model):
    name = models.CharField(verbose_name='分类名', max_length=20)
    '''
    创建时间
    更新时间
    是否显示/是否删除
    排序
     
    
    '''

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    name = models.CharField(verbose_name='标签', max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name


class Artcile(models.Model):
    title = models.CharField(verbose_name='文章名称', max_length=50)
    content = models.TextField(verbose_name='文章内容', max_length=4000)
    vnum = models.IntegerField(verbose_name='浏览量', default=0)
    cnum = models.IntegerField(verbose_name='评论量', default=0)
    created_time = models.DateTimeField(verbose_name='创建日期', default=datetime.now())

    cat = models.ForeignKey(verbose_name='属于哪个分类', to=Category, on_delete=models.CASCADE,related_name='articles')

    tag = models.ManyToManyField(to=Tag, verbose_name='属于标签')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
