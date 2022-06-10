from django.db import models
from django.contrib.auth.models import AbstractUser
from DjangoUeditor.models import UEditorField


# Create your models here.


class BlogUser(AbstractUser):
    phone = models.CharField(verbose_name='手机号', max_length=11)


class BaseModel(models.Model):
    is_delete = models.BooleanField(verbose_name='是否删除', default=False)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    class Meta:
        abstract = True


# 轮播图表
class Banner(BaseModel):
    title = models.CharField(verbose_name='标题', max_length=10)
    cover = models.ImageField(verbose_name='图片', upload_to='banner/%Y/%m/%d')
    link = models.URLField(verbose_name='跳转地址')
    position = models.IntegerField(verbose_name='排序', default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['position']
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name


# 分类表
class Category(BaseModel):
    name = models.CharField(verbose_name='标题', max_length=10)
    position = models.IntegerField(verbose_name='排序', default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['position']
        verbose_name = '分类'
        verbose_name_plural = verbose_name


# 标签表
class Tag(BaseModel):
    name = models.CharField(verbose_name='标题', max_length=10)
    position = models.IntegerField(verbose_name='排序', default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['position']
        verbose_name = '标签'
        verbose_name_plural = verbose_name


'''
文章-->标签 article.tag
标签-->文章 tag.article_set
'''


# 文章表
class Article(BaseModel):
    title = models.CharField(verbose_name='标题', max_length=100)
    intro = models.CharField(verbose_name='简介', max_length=255)
    vnum = models.IntegerField(verbose_name='浏览量', default=0)
    cover = models.ImageField(verbose_name='图片', upload_to='article/%Y/%m/%d')
    is_top = models.BooleanField(verbose_name='是否置顶', default=False)
    content = UEditorField(width=600, height=300, toolbars="full",
                           imagePath="article/content/%(basename)s_%(datetime)s.%(extname)s", filePath="files/")
    user = models.ForeignKey(to=BlogUser, on_delete=models.CASCADE)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(to=Tag)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_time']
        verbose_name = '文章'
        verbose_name_plural = verbose_name


# 评论表
class Comment(BaseModel):
    content = models.CharField(verbose_name='评论内容', max_length=255)
    users = models.ForeignKey(to=BlogUser, on_delete=models.CASCADE)
    article = models.ForeignKey(to=Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-created_time']
        verbose_name = '评论'
        verbose_name_plural = verbose_name


# 友情链接
class FriendLink(BaseModel):
    name = models.CharField(verbose_name='友情链接', max_length=255)
    link = models.URLField(verbose_name='跳转地址')
    position = models.IntegerField(verbose_name='排序', default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['position']
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

# 文章表
# 标签表
# 分类表
# 轮播图表
# 评论表
# 友情链接

# --- 广告表
