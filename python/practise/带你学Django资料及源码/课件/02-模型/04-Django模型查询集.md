### 一、什么是查询集(结果集)

查询集表示从数据库中获取的对象集合。

### 二、查询集两大特性
- #### 惰性查询

只有在实际使用查询集中的数据的时候,才会发生对数据库的真正查询，

```python
list=Article.objects.all()
```

- 
  #### 查询集的缓存

当使用的是同一个查询集时，第一次的时候会发生实际数据库的查询,然后把结果缓存起来,之后再使用这个查询集时,使用的是缓存中的结果集

- 不缓存

```python 
from .models import Article
[article.id for book in Article.objects.all()]
[article.id for book in Article.objects.all()]
```
- 缓存

```python 
list=Article.objects.all()
[article.id for article in list]
[article.id for article in list]
```


### 三、切片
```python
list=Article.objects.all()[0:2]
```



