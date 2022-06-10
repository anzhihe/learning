from django.db import models


# Create your models here.

class BaseModel(models.Model):
    isdelete = models.BooleanField(verbose_name='是否删除', default=False)
    ext = models.CharField(verbose_name='扩展字段', default='{}', max_length=1024)
    created_time = models.DateTimeField(verbose_name='名字', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='名字', auto_now=True)

    class Meta:  # 如果该类不生成表，把该类写成抽象类，只做为继承作用
        abstract = True


# 分类表
class Category(BaseModel):
    name = models.CharField(verbose_name='名字', max_length=6, null=False, unique=True)
    position = models.IntegerField(verbose_name='排序', null=False)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        ordering = ['-position']

    def __str__(self):
        return self.name


# 新闻类
class News(BaseModel):
    title = models.CharField(verbose_name='标题', max_length=255, null=False, unique=True)
    content = models.TextField(verbose_name='内容', null=False, max_length=4000)
    src = models.URLField(verbose_name='封面', null=False)
    vnum = models.IntegerField(verbose_name='浏览量', default=0)
    isoriginal = models.BooleanField(verbose_name='是否原创')
    istop = models.BooleanField(verbose_name='是否置顶', default=False)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '新闻'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


'''
scr/1111.jpg 
http://www.baidu.com/src/1.jpg

'''
