# 模板

**如何向请求者返回一个漂亮的页面呢？**

肯定需要用到html、css，如果想要更炫的效果还要加入js，问题来了，这么一堆字段串全都写到视图中，作为HttpResponse()的参数吗？这样定义就太麻烦了吧，因为定义字符串是不会出任何效果和错误的，如果有一个专门定义前端页面的地方就好了。

解决问题的技术来了：**模板。**

在Django中，将前端的内容定义在模板中，然后再把模板交给视图调用，各种漂亮、炫酷的效果就出现了。

## 1. 创建模板
- 为应用wangzhe下的视图index创建模板index.html，目录结构如下图：

![](http://tp.jikedaohang.com/20191114220702_e0JERo_Screenshot.jpeg)

- 设置查找模板的路径：打开wangzhe/settings.py文件，设置TEMPLATES的DIRS值

```python 
'DIRS': [os.path.join(BASE_DIR, 'templates')],
```

![](http://tp.jikedaohang.com/20191114220730_QKltwd_Screenshot.jpeg)

## 3. 视图函数

```python
from django.shortcuts import render
from django.http import HttpResponse

from .models import Hero


# Create your views here.
def index(request):
    heros = Hero.objects.all()
    ctx = {
        'heros': heros
    }
    return render(request, 'index.html', ctx)

```



## 3. 定义模板



打开templates/index.html文件，定义代码如下：
```html 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<ul>
    {% for hero in heros %}
        <li>{{ hero.name }}</li>
    {% endfor %}
</ul>

</body>
</html>
```

在模板中输出变量语法如下，变量可能是从视图中传递过来的，也可能是在模板中定义的。
```python
{{变量名}}
```
在模板中编写代码段语法如下：
```python
{%代码段%}
```

## 
![](http://tp.jikedaohang.com/20191114221015_bPLweJ_Screenshot.jpeg)

