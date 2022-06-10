# HttpRequest对象

当客户端像服务器发起一个请求后，会创建一个名为HttpRequest对象。视图中的第一个参数必须是HttpRequest对象。

## 属性

- path：一个字符串，表示请求的页面的完整路径，不包含域名和参数部分。
- method：一个字符串，表示请求使用的HTTP方法，常用值包括：'GET'、'POST'。
    - 在浏览器中给出地址发出请求采用get方式，如超链接。
    - 在浏览器中点击表单的提交按钮发起请求，如果表单的method设置为post则为post请求。
- encoding：一个字符串，表示提交的数据的编码方式。
    - 如果为None则表示使用浏览器的默认设置，一般为utf-8。
    - 这个属性是可写的，可以通过修改它来修改访问表单数据使用的编码，接下来对属性的任何访问将使用新的encoding值。
- GET：QueryDict类型对象，类似于字典，包含get请求方式的所有参数。
- POST：QueryDict类型对象，类似于字典，包含post请求方式的所有参数。
- FILES：一个类似于字典的对象，包含所有的上传文件。
- COOKIES：一个标准的Python字典，包含所有的cookie，键和值都为字符串。
- session：一个既可读又可写的类似于字典的对象，表示当前的会话，只有当Django 启用会话的支持时才可用，详细内容见"状态保持"。
- 运行服务器，在浏览器中浏览首页，可以在浏览器“开发者工具”中看到请求信息如下图：

![](http://tp.jikedaohang.com/20191203220558_w8TPrO_Screenshot.jpeg)

- 编辑views.py文件，代码如下：


```python 
def index(request):
    content='%s,%s'%(request.path,request.encoding)
    return render(request, 'index.html', {'content':content})
```

- 在templates下创建index.html文件，代码如下：

```html
<html>
<head>
    <title>首页</title>
</head>
<body>
{{ content }}
<br/>
</body>
</html>
```
## 方法

#### GET

- 编写视图


```python
def index(request):
    return render(request, 'index.html')
```

-  模板代码如下

```html
<form action="/register" method="get">
    输入手机号：<input type="text" name="phone" ><br>
    输入密码：<input type="password" name="password"><br>
    确认密码：<input type="password" name="password1"><br>
    性别：男<input type="radio" value="1" name="gender">
    女<input type="radio" value="0" name="gender"><br>
    爱好
    抽烟：<input type="checkbox" value="抽烟" name="hobby">
    喝酒 <input type="checkbox" value="喝酒" name="hobby">
    喝酒 <input type="checkbox" value="烫头" name="hobby">


    <input type="submit" value="注册">

</form>
```


- 编写注册视图

```python
def register(request):
    phone = request.GET.get('phone')
    hobby = request.GET.getlist('hobby')
    return HttpResponse('接到参数了')
```



#### POST

- 模板代码如下

```python
<form action="/register" method="get">
    输入手机号：<input type="text" name="phone" ><br>
    输入密码：<input type="password" name="password"><br>
    确认密码：<input type="password" name="password1"><br>
    性别：男<input type="radio" value="1" name="gender">
    女<input type="radio" value="0" name="gender"><br>
    爱好
    抽烟：<input type="checkbox" value="抽烟" name="hobby">
    喝酒 <input type="checkbox" value="喝酒" name="hobby">
    喝酒 <input type="checkbox" value="烫头" name="hobby">


    <input type="submit" value="注册">

</form>
```

- 视图代码

```python
def register(request):
    phone = request.POST.get('phone')
    hobby = request.POST.getlist('hobby')
    return HttpResponse('接到参数了')
```

















