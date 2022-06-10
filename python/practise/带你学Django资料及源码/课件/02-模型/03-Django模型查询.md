## 字段查询

###  查询等

exact：表示判等。

```python
list=Article.objects.filter(id__exact=1)
可简写为：
list=Article.objects.filter(id=1)
```

### 查询单一对象

```
Article.objects.get(pk=1)
```

> **注意**：使用get()方法和使用filter()方法然后通过[0]的方式分片，有着不同的地方。看似两者都是获取单一对象。但是，**如果在查询时没有匹配到对象，那么get()方法将抛出DoesNotExist异常**。这个异常是模型类的一个属性，在上面的例子中，如果不存在主键为1的Entry对象，那么Django将抛出`Entry.DoesNotExist`异常。
>
> 类似地，**在使用get()方法查询时，如果结果超过1个，则会抛出MultipleObjectsReturned异常**，这个异常也是模型类的一个属性。



###  模糊查询

contains：是否包含。

```python
list = Article.objects.filter(btitle__contains='新')
```
**startswith、endswith：以指定值开头或结尾。**

```python
list = Article.objects.filter(btitle__endswith='哈哈')
```
> 以上运算符都区分大小写，在这些运算符前加上i表示不区分大小写，如iexact、icontains、istartswith、iendswith.

### 空查询

**isnull：是否为null。**

```python
list = Article.objects.filter(title__isnull=False)
```

### 范围查询

**in：是否包含在范围内。**

```python
list = Article.objects.filter(id__in=[1, 3, 5])
```

###  比较查询


**gt、gte、lt、lte：大于、大于等于、小于、小于等于。**

```python
list = Article.objects.filter(id__gt=3)
```
**不等于**

**不等于的运算符，使用exclude()过滤器。**

```python
list = Article.objects.exclude(id=3)
```

### 日期查询

**year、month、day、week_day、hour、minute、second：对日期时间类型的属性进行运算。**

```python
list = Article.objects.filter(create_time__year=2019)
```
查询2019年1月1日后发表的文章。
```python
list = Article.objects.filter(create_time__gt=date(2019, 1, 1))
```

## F对象**


**两个属性做比较**

例：查询阅读量大于等于评论量的文章。
```python
from django.db.models import F
...
list = Article.objects.filter(vnum__gte=F('cnum'))
```
可以在F对象上使用算数运算。

例：查询阅读量大于2倍评论量的文章。
```python
list = Article.objects.filter(bread__gt=F('bcomment') * 2)
```

## Q对象

并且关系

例：查询阅读量大于20，并且编号小于3的文章。
```python
list=Article.objects.filter(vnum__gt=20,id__lt=3)
或
list=Article.objects.filter(vnum__gt=20).filter(id__lt=3)
```
例：查询阅读量大于20的文章，改写为Q对象如下。
```python
from django.db.models import Q
...
list = Article.objects.filter(Q(vnum__gt=20))
```
例：查询阅读量大于20，或编号小于3的文章，只能使用Q对象实现
```python
list = Article.objects.filter(Q(vnum__gt=20) | Q(id__lt=3))
```
例：查询编号不等于3的文章。
```python
list = Article.objects.filter(~Q(pk=3))
```


## 聚合函数


使用aggregate()过滤器调用聚合函数。聚合函数包括：Avg，Count，Max，Min，Sum，被定义在django.db.models中。

例：查询文章的总阅读量。
```python
from django.db.models import Sum
...
list = Article.objects.aggregate(Sum('vnum'))
```
注意aggregate的返回值是一个字典类型，格式如下：
```
  {'聚合类小写__属性名':值}
  如:{'sum__vnum':3}
```

