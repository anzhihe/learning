## 反向解析

随着功能越来越多，模板上的超链接也会越来越多，如果根据路由一旦变化，那模板上的超链接都需要变化，改起来就是一件特别麻烦的事情。所以就需要用到反向生成超链接

> 反向解析应用在两个地方：模板中的超链接，视图中的重定向。

编写视图

```python
def reverse(request):
    return render(request, 'reverse.html')


def center(request):
    return HttpResponse('center')
```

配置路由

```python
    path('reverse/', views.reverse),
    path('center/', views.center),
```

编写模板

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<a href="/center">普通超链接</a>
</body>
</html>
```

效果如下

![](http://tp.jikedaohang.com/20191212214345_42LTQJ_Screenshot.jpeg)





![](http://tp.jikedaohang.com/20191212214554_y80DXh_Screenshot.jpeg)

## 利用反向解析

编写路由

```python
  path('reverse/', views.reverse, name='reverse'),
  path('center/', views.center, name='center'),
```

编写模板

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<a href="/center">普通超链接</a>
<a href="{% url 'news:center' %}">反向超链接</a>
</body>
</html>
```

![](http://tp.jikedaohang.com/20191212214930_6UxkAM_Screenshot.jpeg)

## URL参数

有些url配置项正则表达式中是有参数的，接下来讲解如何传递参数。

编写路由

```python
path('center/<int:id>_<int:id1>', views.center1, name='center1'),
```

编写视图

```python
def center1(request, id, id1):
    return HttpResponse('center')
```

编写模板

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<a href="/center">普通超链接</a>
<a href="{% url 'news:center' %}">反向超链接</a>
<a href="{% url 'news:center1' 0 1 %}">反向参数超链接</a>
</body>
</html>
```

## 关键字传参

编写路由

```
re_path('center1/(?P<id>[0-9]+)_(?P<id1>[0-9]+)', views.center1, name='center1'),
```

编写模板

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<a href="/center">普通超链接</a>
<a href="{% url 'news:center' %}">反向超链接</a>
<a href="{% url 'news:center1' 0 1 %}">反向参数超链接</a>
<a href="{% url 'news:center1' id=100 id1=99 %}">反向关键字参数超链接</a>
</body>
</html>
```



## 反向解析

不带参数

```
from django.shortcuts import redirect,reverse
return redirect(reverse('news:center1'))
```

普通参数

```python
return redirect(reverse('news:center1', args=(0,1)))
```

关键字参数

```
return redirect(reverse('news:center1', kwargs={'id':100,'id1':98}))
```

