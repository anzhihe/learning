### 什么是CSRF

跨站请求伪造（CSRF，Cross Site Request Forgery,）与跨站请求脚本正好相反。跨站请求脚本的问题在于，客户端信任服务器端发送的数据。跨站请求伪造的问题在于，服务器信任来自客户端的数据。



![](http://tp.jikedaohang.com/20191212204142_5hJ6Vy_Screenshot.jpeg)

编写视图

```python
from django.shortcuts import render
from django.http import HttpResponse


def transfer(request):
    if request.method == 'POST':
        from_ = request.POST.get('from')
        to_ = request.POST.get('to')
        money = request.POST.get('money')
        print("{}给{}转账{}".format(from_, to_, money))
        return HttpResponse("转账成功")
    return render(request, 'bank.html')
```
配置路由

```python
from django.contrib import admin
from django.urls import path
from news import views

urlpatterns = [
    path('transfer/', views.transfer),
]
```
编写模板

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>transfer</title>
</head>
<body>
<h1>银行网站</h1>
<form action="/transfer/" method="post">
    <p><input type="text" name="key" value="aaaaa" style="display: none"></p>
    <p>
        转出方账号：
        <input type="text" name='from'>
        转入方账号：
        <input type="text" name='to'>
    </p>
    <p>
        金额：
        <input type="text" name="money">
    </p>
    <p>
        <input type="submit" value="转账">
    </p>
</form>
</body>
</html>


```
效果如下![](http://tp.jikedaohang.com/20191212204334_82z9T3_Screenshot.jpeg)

## 取消CSRF保护

- 注销中间件



![](http://tp.jikedaohang.com/20191212204453_VVqv9a_Screenshot.jpeg)

- 采用装饰器

```python
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def transfer(request):
    if request.method == 'POST':
        from_ = request.POST.get('from')
        to_ = request.POST.get('to')
        money = request.POST.get('money')
        print("{}给{}转账{}".format(from_, to_, money))
        return HttpResponse("转账成功")
    return render(request, 'bank.html')
```



关闭之后，我们就可以伪装请求了。

编写钓鱼网站模板

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>transfer</title>
</head>
<body>
<h1>钓鱼网站</h1>
<form action="http://127.0.0.1:8000/transfer/" method="post">
    <p>
        转出方账号：
        <input type="text" name='from'>
        转入方账号：
        <input type="text" name=''>
        <input type="text" name='to' style="display: none;" value="kkkkk">
    </p>
    <p>
        金额：
        <input type="text" name="money">
    </p>
    <p>
        <input type="submit" value="转账">
    </p>
</form>
</body>
</html>

```



直接在本地运行，注意不用通过Django运行网站。



![](http://tp.jikedaohang.com/20191212211932_iCHjw3_Screenshot.jpeg)

![](http://tp.jikedaohang.com/20191212211944_pDRnyU_Screenshot.jpeg)

# 开启CSRF

- 打开中间件
- 利用装饰器

```
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt,csrf_project

@csrf_project
def transfer(request):
    if request.method == 'POST':
        from_ = request.POST.get('from')
        to_ = request.POST.get('to')
        money = request.POST.get('money')
        print("{}给{}转账{}".format(from_, to_, money))
        return HttpResponse("转账成功")
    return render(request, 'bank.html')
```

在form表单加上csrf_token标签


```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>transfer</title>
</head>
<body>
<h1>银行网站</h1>
<form action="/transfer/" method="post">
    {% csrf_token %}
    <p><input type="text" name="key" value="aaaaa" style="display: none"></p>
    <p>
        转出方账号：
        <input type="text" name='from'>
        转入方账号：
        <input type="text" name='to'>
    </p>
    <p>
        金额：
        <input type="text" name="money">
    </p>
    <p>
        <input type="submit" value="转账">
    </p>
</form>
</body>
</html>


```

### 类视图取消csrf

```
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.utils.decorators import method_decorator
@method_decorator(csrf_exempt,name='dispatch')
class MyView(View):
    def get(self,request):
        return HttpResponse("get")
    def post(self,request):
        return HttpResponse("post")
```



# 原理

- 加入标签,可以查看源代码,发现多了如下代码

![](http://tp.jikedaohang.com/20191212212335_jCfAPZ_Screenshot.jpeg)