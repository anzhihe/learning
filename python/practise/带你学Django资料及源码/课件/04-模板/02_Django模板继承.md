

# 模板继承

模板的继承和面向对象里面的继承的思想是一样的，都为了复用。我们可以发现大部分网页都会有头部和尾部信息。


## 父模板

如果发现在多个模板中某些内容相同，那就应该把这段内容定义到父模板中。

标签block：用于在父模板中预留区域，留给子模板填充差异性的内容，名字不能相同。 为了更好的可读性，建议给endblock标签写上名字，这个名字与对应的block名字相同。父模板中也可以使用上下文中传递过来的数据。
```html
{%block 名称%}
预留区域，可以编写默认内容，也可以没有默认内容
{%endblock  名称%}
```
## 子模板

标签extends：继承，写在子模板文件的第一行。
```
{% extends "父模板路径"%}
```
子模版不用填充父模版中的所有预留区域，如果子模版没有填充，则使用父模版定义的默认值。

填充父模板中指定名称的预留区域。
```
{%block 名称%}
实际填充内容
{{block.super}}用于获取父模板中block的内容
{%endblock 名称%}
```



创建父模板

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}名称{% endblock %}</title>
</head>
<body>

<h1>我头部</h1>
{% block content %}
{% endblock %}
<h1>我尾部</h1>

</body>
</html>
```

编写子模板1

```html
{% extends 'base.html' %}
{% block title %}孩子1{% endblock %}
{% block content %}

    我是孩子1
{% endblock %}
```

编写子模板2

```html
{% extends 'base.html' %}
{% block title %}孩子2{% endblock %}
{% block content %}
    我是孩子2
{% endblock %}
```



编写视图

```python 
from django.shortcuts import render


# Create your views here.

def son1(request):
    return render(request, 'son1.html')


def son2(request):
    return render(request, 'son2.html')

```

配置路由

```python
from django.contrib import admin
from django.urls import path
from news import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('son1/', views.son1),
    path('admin/', views.son2),
]
```

效果如下：

![](http://tp.jikedaohang.com/20191212201410_AQqNCc_Screenshot.jpeg)

![](http://tp.jikedaohang.com/20191212201440_qFcAJs_Screenshot.jpeg)