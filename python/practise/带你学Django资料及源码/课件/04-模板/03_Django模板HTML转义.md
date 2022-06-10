# HTML转义
模板对上下文传递的字符串进行输出时，会对以下字符自动转义。
```
小于号< 转换为 &lt;

大于号> 转换为 &gt;

单引号' 转换为 &#39;

双引号" 转换为 &quot;

与符号& 转换为 &amp;
```

编写视图

```python 
from django.shortcuts import render

def escape(request):
    ctx = {'content': '<h1>hi python</h1>'}
    return render(request, 'escape.html', ctx)
```

编写路由

```python
from django.contrib import admin
from django.urls import path
from news import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('escape/', views.escape),
]
```

编写模板

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

{{ content }}
</body>
</html>
```

> 注意：转义后标记代码不会被直接解释执行，而是被直接呈现，防止客户端通过嵌入js代码攻击网站.

效果如下

![](http://tp.jikedaohang.com/20191212202147_gHu31u_Screenshot.jpeg)

## 关闭转义

```python
{{data|safe}}
```

## 开启转义

Django默认是开启转义

```
{{content|escape}}
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

{{ content|safe }}
</body>
</html>
```
效果如下

![](http://tp.jikedaohang.com/20191212202409_VAY7li_Screenshot.jpeg)

标签autoescape：通过on、off来开启或关闭转义
```
{%autoescape off%}
...
{%endautoescape%}
```




## 硬编码

在模板中硬编码的html字符串，不会转义。

编写模板

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
{{ content1|default:'<h1>hello</h1>' }}
</body>
</html>
```

效果如下

![](http://tp.jikedaohang.com/20191212202745_6R51jp_Screenshot.jpeg)

如果想要转义，就需要手动

编写模板
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
{{ content1|default:'&lt;h1&gt;hello&lt;/h1&gt;' }}
</body>
</html>
```
效果如下

![](http://tp.jikedaohang.com/20191212202946_GuuHpz_Screenshot.jpeg)