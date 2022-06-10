from django.db import models


# Create your models here.


class BaseModel(models.Model):
    is_show = models.BooleanField(verbose_name='是否显示', default=True)
    ext = models.CharField(verbose_name='扩展字段', default='', max_length=256, null=True, blank=True)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    class Meta:
        abstract = True


# 导航分类表
class NavCategory(BaseModel):
    name = models.CharField(verbose_name='名称', max_length=10)
    position = models.IntegerField(verbose_name='排序', default=0)
    vnum = models.IntegerField(verbose_name='浏览量', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '导航分类'
        verbose_name_plural = verbose_name


# 导航表
class Nav(BaseModel):
    name = models.CharField(verbose_name='名称', max_length=10)
    position = models.IntegerField(verbose_name='排序', default=0)
    href = models.URLField(verbose_name='跳转地址')
    nav_cat = models.ForeignKey(to=NavCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-position','updated_time']
        verbose_name = '导航'
        verbose_name_plural = verbose_name
