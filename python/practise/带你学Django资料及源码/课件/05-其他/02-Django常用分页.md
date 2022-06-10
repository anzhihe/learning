

### 分页

Django默认提供了分页，当然也有第三方扩展分页，咱们就用第三方扩展分页。



### 文档

https://github.com/jamespacileo/django-pure-pagination

## 安装

```python
pip install django-pure-pagination
```

### 注册应用

```
INSTALLED_APPS = (
    'pure_pagination',
)
```

### 配置设置

```python
PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 1,
    'MARGIN_PAGES_DISPLAYED': 2,
    'SHOW_FIRST_PAGE_WHEN_INVALID': True,
}
```



![](http://tp.jikedaohang.com/20191215104740_Xxwo7q_Screenshot.jpeg)

### 编写视图

```python 

def index(request):
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    arts = Article.objects.all()
    p = Paginator(arts, per_page=1, request=request)
    articles = p.page(page)
    return render(request, 'index.html', locals())

```

### 配置路由

```python
path('', views.index),
```

## 编写模板

```html 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<ul>
    {% for art in articles.object_list %}
        <li>{{ art.title }}</li>
    {% endfor %}
</ul>


{% include '_pagination.html' %}
</body>
</html>
```

_pagination.html

```python
{% load i18n %}
<div class="pagination">
    {% if articles.has_previous %}
        <a href="?{{ articles.previous_page_number.querystring }}"
           class="prev">上一页</a>
    {% else %}
        <span class="disabled prev">上一页 </span>
    {% endif %}
    {% for page in articles.pages %}
        {% if page %}
            {% ifequal page articles.number %}
                <span class="current page">{{ page }}</span>
            {% else %}
                <a href="?{{ page.querystring }}" class="page">{{ page }}</a>
            {% endifequal %}
        {% else %}
            ...
        {% endif %}
    {% endfor %}
    {% if page_obj.has_next %}
        <a href="?{{ articles.next_page_number.querystring }}" class="next">下一页</a>
    {% else %}
        <span class="disabled next">下一页</span>
    {% endif %}
</div>
```



## 效果如下

![](http://tp.jikedaohang.com/20191215110310_im5gWQ_Screenshot.jpeg)













































