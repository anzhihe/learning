# 模型类关系

关系型数据库的关系包括三种类型：

- ForeignKey：一对多，将字段定义在多的一端中。
- ManyToManyField：多对多，将字段定义在任意一端中。
- OneToOneField：一对一，将字段定义在任意一端中。
- 可以维护递归的关联关系，使用'self'指定，详见"自关联"。

## 一对多关系

新闻和分类模型

```python
# 分类表
class Category(models.Model):
    title = models.CharField(max_length=20)

    position = models.IntegerField(default=1)  # 用来排序

    isshow = models.BooleanField(default=True)  # 用于是否展示

    isdelete = models.BooleanField(default=False)  # 用于是否删除

    create_time = models.DateTimeField(auto_now_add=True)  # 用于表示创建时间

    update_time = models.DateTimeField(auto_now=True)  # 用于表示更新时间

    def __str__(self):
        return self.title


#文章表
class Article(models.Model):
    title = models.CharField(max_length=100)

    content = models.TextField(max_length=5000)

    Category = models.ForeignKey(to=Category,on_delete=models.CASCADE)  # 一对多 必须写在多的里面

    def __str__(self):
        return self.title
```



## 多对多关系
新闻和标签模型
```python
# 标签
class Tag(models.Model):
    title = models.CharField(max_length=20)  # 标签名字

    isdelete = models.BooleanField(default=False)  # 用于是否删除

    create_time = models.DateTimeField(auto_now_add=True)  # 用于表示创建时间

    update_time = models.DateTimeField(auto_now=True)  # 用于表示更新时间


# 文章表
class Article(models.Model):
    title = models.CharField(max_length=100)

    content = models.TextField(max_length=5000)

    tag = models.ManyToManyField(to=Tag)  # 多对多写在哪里都可以

    def __str__(self):
        return self.title
```


## 自关联

省市区模型

```
#定义地区模型类，存储省、市、区县信息
class Area(models.Model):
    title=models.CharField(max_length=30)#名称
    parent=models.ForeignKey('self',null=True,blank=True)#关系
```

## 查询

- 一对多查询

```python
category = Category.objects.get(id=1)
category.article_set.all()
```
- 多到一查询:

```python
article = Article.objects.get(id=1)
article.category
```


- 多对多查询->正向查询

```
article = Article.objects.get(id=1) 
article.tag.all() # 取一篇文章的所有标签
```

- 多对多查询->反向查询

```
tag = Tag.objects.get(id=1)
tag.article_set.all()
```

- 反向查询简化

  可以在ForeignKey字段的定义中，category = ForeignKey(Category, on_delete=models.CASCADE, related_name=’articles’)`

```
c = Category.objects.get(id=1)
c.articles.all() 
```

