### 视图

视图负责接受Web请求HttpRequest，进行逻辑处理，返回Web响应HttpResponse给请求者。

- 在应用下创建一个名字为urls.py的文件

```python
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
]

```



- 在项目的urls.py包含应用urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
]

```

在应用/views.py中定义视图函数index：

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse('哈哈')

```



## 启动服务器

启动服务器，并通过浏览器访问 http://127.0.0.1:8000

![](http://tp.jikedaohang.com/20191202214457_wjI9Mh_Screenshot.jpeg)

## 类视图

    from django.views.generic import View    
    class DefineClassview(View):
        """演示类视图的定义和使用"""
    def get(self, request):
        """处理GET请求业务逻辑"""
        return HttpResponse('GET请求业务逻辑')
    
    def post(self, request):
        """处理POST请求业务逻辑"""
        return HttpResponse('POST请求业务逻辑')
    
    def put(self, request):
        pass
> - **代码可读性好**
> - **类视图相对于函数视图有更高的复用性,如果其他地方需要使用到某个类的某个特定方法,直接继承该类的视图就可以了**

配置路由

```

urlpatterns = [
    # 视图函数：注册
    path('register$', views.RegisterView.as_view(), name='register'),
]
```

