# 静态文件 

在我们项目中，css、js、一些图片都会属于静态资源，我们会把这些静态资源放到指定的目录下，方便我们使用，Django提供了静态文件配置。

## 设置文件文件

```python 
# 静态文件
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```

## 静态文件目录

![](http://tp.jikedaohang.com/20191214222328_6L1nPz_Screenshot.jpeg)



## 编写视图



```python
def show_pic(request):
    return render(request, 'show_pic.html')
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
<img src="/static/image/shuaige.jpeg" alt="">

</body>
</html>
```

## 效果入戏

![](http://tp.jikedaohang.com/20191214222924_1EnVAp_Screenshot.jpeg)

## 反向解析

编写模板

```html 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<img src="/static/image/shuaige.jpeg" alt="">

{% load staticfiles %}
<img src="{% static 'image/shuaige.jpeg' %}">
</body>
</html>
```



这样又有什么好处呢？我们修改一些Settings里面的文件

```python
STATIC_URL = '/abc/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

```

看下源代码

![](http://tp.jikedaohang.com/20191214223325_WZlUUG_Screenshot.jpeg)