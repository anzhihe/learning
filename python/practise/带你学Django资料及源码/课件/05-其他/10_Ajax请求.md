### Ajax

现在前后端分离项目越来越流行了，前端只关注页面，后端只关注数据，前端只要通过Ajax发起请求把数据请求回来填充到页面就可以了。



### 准备模型

```
from django.db import models


# Create your models here.

class Area(models.Model):
    name = models.CharField(verbose_name='地区名字', max_length=20)
    parent = models.ForeignKey(to='self', blank=True, null=True, on_delete=models.Model)

```

### 导入area.sql文件



### 编写视图

```python
from django.shortcuts import render
from .models import *

from django.http import HttpResponse, JsonResponse


# Create your views here.


def index(request):
    return render(request, 'app01/index.html')


def get_parent(request):
    areas = Area.objects.filter(parent__isnull=True).all()
    l = []
    for item in areas:
        l.append({"id": item.id, 'name': item.name})
    return JsonResponse({'data': l})


def get_son(request,id):
    areas = Area.objects.filter(parent_id=id).all()
    l = []
    for item in areas:
        l.append({"id": item.id, 'name': item.name})
    return JsonResponse({'data': l})

```

### 编写模板

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>


<html>
<head>
    <title>省市区列表</title>
    <script type="text/javascript" src="http://code.jquery.com/jquery-2.1.4.min.js"></script>
    <script type="text/javascript">
        $(function () {
            //页面加载完成后获取省信息，并添加到省select
            $.get('/app01/get_parent', function (res) {
                pro = $('#pro')
                $.each(res.data, function (index, item) {
                    pro.append('<option value=' + item.id + '>' + item.name + '</option>');
                })
            });
            //为省select绑定change事件，获取市信息，并添加到市select
            $('#pro').change(function () {
                $.get('/app01/get_son/' + $(this).val() + '/', function (dic) {
                    city = $('#city');
                    city.empty().append('<option value="">请选择市</option>');
                    dis = $('#dis');
                    dis.empty().append('<option value="">请选择区县</option>');
                    $.each(dic.data, function (index, item) {
                        city.append('<option value=' + item.id + '>' + item.name + '</option>');
                    })
                });
            });
            //为市select绑定change事件，获取区县信息，并添加到区县select
            $('#city').change(function () {
                $.get('/app01/get_son/' + $(this).val() + '/', function (dic) {
                    dis = $('#dis');
                    dis.empty().append('<option value="">请选择区县</option>');
                    $.each(dic.data, function (index, item) {
                        dis.append('<option value=' + item.id + '>' + item.name + '</option>');
                    })
                })
            });

        });
    </script>
</head>
<body>
<select id="pro">
    <option value="">请选择省</option>
</select>
<select id="city">
    <option value="">请选择市</option>
</select>
<select id="dis">
    <option value="">请选择区县</option>
</select>
</body>
</html>

</body>
</html>
```

