### 模板

Django提供了模板，用于编写HTML文件

模板包含：
- 静态部分：包含html、css、js。
- 动态部分：模板语言。

Django处理模板分为两个阶段：

- 加载：根据给定的路径找到模板文件，编译后放在内存中。
- 渲染：使用上下文数据对模板插值并返回生成的字符串。

### 模板语言
- 变量
- 标签
- 过滤器
- 注释

## 变量
模板变量的作用是计算并输出，变量名必须由字母、数字、下划线（不能以下划线开头）和点组成。

```
{{变量}}
```
当模版引擎遇到点dog.name，会按照下列顺序解析：
```
1.字典dog['name']
2.先属性后方法，将dog当作对象，查找属性name，如果没有再查找方法name()
3.如果是格式为dog.1则解析为列表dog[1]
```
> 注意：在模板中调用方法时不能传递参数。
>

**编写模型**

```python
from django.db import models


# Create your models here.

class Dog(models.Model):
    name = models.CharField(max_length=128)
    age = models.IntegerField(default=1)

    def show(self):
        return "名字是" + self.name + "年龄是" + str(self.age)

```

**编写视图**

```python
def index(request):
    dog = Dog.objects.all().first()

    ctx = {
        'age': {"count": 12},
        'dog': dog,
        'name': ["laowang", "laosong"],
        'comments': ["我想上一楼", "留给二楼", "四楼想要"],
        'time': datetime.now(),
        'content': 'daskdhaksdhaskjhdkjahskjdhaskjhdjkashkjdhaskh',
        'count': 21,
        'desc': "老王啊"
    }
    return render(request, 'index.html', ctx)
```
**编写路由**

```python
from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index)
   
]
```
**编写模板**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>变量</h1>
年龄放按典解析：{{ age.count }}<br>
狗的名字按属性解析:{{ dog.name }}<br>
狗的介绍按方法解析:{{ dog.show }}<br>
名字按列表解析:{{ name.1 }}


</body>

</html>
```


![](http://tp.jikedaohang.com/20191205211426_d1HRi6_Screenshot.jpeg)

## 标签


语法如下：

```
{%代码段%}
```

for标签语法如下：

```html
{%for item in 列表%}

循环逻辑
{{forloop.counter}}表示当前是第几次循环，从1开始
{%empty%}
列表为空或不存在时执行此逻辑
{%endfor%}
```

if标签语法如下：
```html
{%if ...%}
逻辑1
{%elif ...%}
逻辑2
{%else%}
逻辑3
{%endif%}
```
比较运算符如下：

> 注意：运算符左右两侧不能紧挨变量或常量，必须有空格。
```python
==
!=
<
>
<=
>=
```
布尔运算符如下：
```python
and
or
not
```
依然是上面的案例

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>


<h1>标签</h1>

<ul>

    {% for comment in commets %}
        {% if forloop.counter == 1 %}
            <li style="background-color: red">{{ comment }}----#{{ forloop.counter }}楼</li>
        {% elif forloop.counter == 2 %}
            <li style="background-color: green">{{ comment }}----#{{ forloop.counter }}楼</li>
        {% else %}
            <li style="background-color: yellow">{{ comment }}----#{{ forloop.counter }}楼</li>
        {% endif %}
    {% empty %}
        还没有人留言
    {% endfor %}
</ul>

</body>

</html>
```


![](http://tp.jikedaohang.com/20191205212937_2geEqK_Screenshot.jpeg)

## 过滤器
- 使用管道符号|来应用过滤器，用于进行计算、转换操作，可以使用在变量、标签中。
- 如果过滤器需要参数，则使用冒号:传递参数。

```
变量|过滤器:参数
```

长度length，返回字符串包含字符的个数，或列表、元组、字典的元素个数。

默认值default，如果变量不存在时则返回默认值。
```
data|default:'默认值'
```
日期date，用于对日期类型的值进行字符串格式化，常用的格式化字符如下：

- Y表示年，格式为4位，y表示两位的年。
- m表示月，格式为01,02,12等。
- d表示日, 格式为01,02等。
- j表示日，格式为1,2等。
- H表示时，24进制，h表示12进制的时。
- i表示分，为0-59。
- s表示秒，为0-59。
```
value|date:"Y年m月j日  H时i分s秒"
```
依然是上面的案例

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<h1>过滤器</h1>

长度过滤器：{{ commets|length }}<br>
默认过滤器：{{ laowang|default:'没有老王这个字段' }}<br>
不加时间过滤器：{{ time }}<br>
时间过滤器：{{ time|date:'Y年m月j日  H时i分s秒' }}<br>
时间过滤器：{{ time|date:'Y年m月d日' }}<br>
截取过滤器：{{ content|truncatechars:'10' }}
整除过滤器：
{% if count|divisibleby:3 %}
    <h1>能被整除</h1>
{% else %}
    <h1>不能被整除</h1>
{% endif %}

{% load filters %}
无参自定义过滤器：
{% if desc|equals %}
    <h1>就是老王</h1>
{% else %}
    <h1>不是老王</h1>
{% endif %}

有参自定义过滤器：
{% if desc|equals1:'2' %}
    <h1>就是老王</h1>
{% else %}
    <h1>不是老王</h1>
{% endif %}



</body>

</html
```


![](http://tp.jikedaohang.com/20191205213553_s37UMn_Screenshot.jpeg)

## 自定义过滤器
在应用下创建名字**templatetags**的包

![](http://tp.jikedaohang.com/20191205213735_NBC1hu_Screenshot.jpeg)

在文件夹下面创建filters.py文件，代码如下

```python
# 导入Library类
from django.template import Library

# 创建一个Library类对象
register = Library()

# 使用装饰器进行注册
@register.filter
# 定义求余函数mod，将value对2求余
def equals(value):
    return value == '老王'

# 使用装饰器进行注册
@register.filter
# 定义求余函数mod，将value对2求余
def equals1(value, arg):
    if value + arg == "老王1":
        return True
```

使用过滤器(必须重启服务器)

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>


<h1>过滤器</h1>

长度过滤器：{{ commets|length }}<br>
默认过滤器：{{ laowang|default:'没有老王这个字段' }}<br>
不加时间过滤器：{{ time }}<br>
时间过滤器：{{ time|date:'Y年m月j日  H时i分s秒' }}<br>
时间过滤器：{{ time|date:'Y年m月d日' }}<br>
截取过滤器：{{ content|truncatechars:'10' }}
整除过滤器：
{% if count|divisibleby:3 %}
    <h1>能被整除</h1>
{% else %}
    <h1>不能被整除</h1>
{% endif %}

{% load filters %}
无参自定义过滤器：
{% if desc|equals %}
    <h1>就是老王</h1>
{% else %}
    <h1>不是老王</h1>
{% endif %}

有参自定义过滤器：
{% if desc|equals1:'2' %}
    <h1>就是老王</h1>
{% else %}
    <h1>不是老王</h1>
{% endif %}


</body>

</html>
```

![](http://tp.jikedaohang.com/20191205220023_LweIXY_Screenshot.jpeg)




## 注释
在模板中使用如下模板注释，这段代码不会被编译，不会输出到客户端；html注释只能注释html内容，不能注释模板语言。

- 单行注释

```
{#...#}
注释可以包含任何模版代码，有效的或者无效的都可以。
```
- 多行注释

```
{%comment%}
...
{%endcomment%}
```