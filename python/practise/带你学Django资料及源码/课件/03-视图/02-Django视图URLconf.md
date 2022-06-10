# URLconf 

用户通过在浏览器的地址栏中输入网址请求网站，对于Django开发的网站，由哪一个视图进行处理请求，是由url匹配找到的。

## 获取URL参数

### Django默认path转换器

- str：匹配任何非空字符串，但不含斜杠`/`，如果你没有专门指定转换器，那么这个是默认使用的；

- int：匹配0和正整数，返回一个int类型

- slug：可理解为注释、后缀、附属等概念，是url拖在最后的一部分解释性字符。该转换器匹配任何ASCII字符以及连接符和下划线，比如’ building-your-1st-django-site‘；

- uuid：匹配一个uuid格式的对象。为了防止冲突，规定必须使用破折号，所有字母必须小写，例如’075194d3-6885-417e-a8a8-6c931e272f00‘ 。返回一个UUID对象；

- path：匹配任何非空字符串，重点是可以包含路径分隔符’/‘。这个转换器可以帮助你匹配整个url而不是一段一段的url字符串

  ​	

  ```
  path('article/<int:id>/', views.index),
  
  path('article/<str:id>/', views.index),
  
  ```



### 自定义转换器

新建一个converters.py文件，与urlconf同目录

- 类属性regex：一个字符串形式的正则表达式属性；
- to_python(self, value) 方法：一个用来将匹配到的字符串转换为你想要的那个数据类型，并传递给视图函数。如果转换失败，它必须弹出ValueError异常；
- to_url(self, value)方法：将Python数据类型转换为一段url的方法，上面方法的反向操作。

```
class FourDigitYearConverter():
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value): # 用来反向解析
        return '%04d'%value
```


```python
from django.urls import path, register_converter
from . import views, converters
register_converter(converters.FourDigitYearConverter, 'yyyy')
urlpatterns = [
    path('article/<yyyy:id>/', views.index),
]
```
### 使用正则表达式

```
from django.urls import re_path
urlpatterns = [
    re_path('article/(\d+)/', views.index),
]
```



### 关键字参数
```python
from django.contrib import admin
from django.urls import path, register_converter
from . import views, converters
from django.urls import re_path

register_converter(converters.FourDigitYearConverter, 'yyyy')
urlpatterns = [
    re_path('article/(?P<id1>[0-9]{4})/', views.index),
]

```
> 注意：视图index此时必须要有一个参数名为id1，否则报错。
```python
def index(request, id1):
    return HttpResponse('哈哈')
```
## 错误视图
Django内置处理HTTP错误的视图，主要错误及视图包括：

- 404错误
- 500错误

> 注意：需要重启


需要修改setting.py文件的DEBUG项。
```python
DEBUG = False
ALLOWED_HOSTS = ['*', ]
```

### 自定义404页面

![](http://tp.jikedaohang.com/20191202230801_tO93l1_Screenshot.jpeg)

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<span>找不到了，开心吗</span>

</body>
</html>
```



![](http://tp.jikedaohang.com/20191202230825_ieVEaV_Screenshot.jpeg)

**500错误及视图**

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<span>服务器报错了，开心吗</span>
</body>
</html>
```

![](http://tp.jikedaohang.com/20191202230953_PCi5je_Screenshot.jpeg)