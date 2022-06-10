### 缓存

对于一些网站首页，例如企业官网，页面在一段时间，都不会有变化。那么我们就可以把它缓存起来，以减少服务器压力。

### 配置

- 利用Redis数据库缓存

```
pip install django-redis-cache
```

```

CACHES = {
    "default": {
        "BACKEND": "redis_cache.cache.RedisCache",
        "LOCATION": "127.0.0.1:6379",
        'TIMEOUT': 60,
    },
}

```

- 利用文件缓存

```
# 缓存
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache' 
    }
}
```

- 利用内存缓存

```
CACHES={
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'TIMEOUT': 60,
    }
}
```



### 视图缓存

```
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.http import HttpResponse

# Create your views here.
@cache_page(60 * 15)
def index(request):
    return HttpResponse('您好')
    # return HttpResponse('大家好')

```



### 模板缓存

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

{% load cache %}

{% cache 900 content %}
    <span>大家好</span>
    <span>我们好</span>
{% endcache %}


</body>
</html>
```

