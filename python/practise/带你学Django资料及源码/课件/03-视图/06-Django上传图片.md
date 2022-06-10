## 上传图片

安装pillow
```
pip install Pillow
```
## 设置配置

```python
# 上传图片
MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace("\\", "/")
MEDIA_URL = '/media/'
```

## 编写模型类

```python
class Article(models.Model):
    title = models.CharField(verbose_name='文章名字', max_length=10)
    cover = models.ImageField(verbose_name='封面', upload_to='news/%y/%m/%d')
```

## 上传图片



![](http://tp.jikedaohang.com/20191214224618_VylrR0_Screenshot.jpeg)

## 编写视图

```
def show_media(request):
    article =  Article.objects.all()
    return render(request,'show_media.html',locals())
```

### 配置路由

```
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
                  path('admin/', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## 配置模板全局变量

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media'
            ],
        },
    },
]
```

## 编写模板

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
{% for article in articles %}
    <h1>{{ article.title }}</h1>
    <img src="{{ MEDIA_URL }}{{ article.cover }}" alt="">
{% endfor %}
</body>
</html>
```

## 效果如下

![](http://tp.jikedaohang.com/20191214225315_ilNyiU_Screenshot.jpeg)



## 自定义form表单中上传图片

## 编写视图

```python
def pic_upload(request):
    return render(request,'pic_upload.html')
```

## 编写路由

```
path('pic_upload/', views.pic_upload),
path('upload/', views.upload),
```

## 编写模板

```html 
<html>
<head>
    <title>上传图片</title>
</head>
<body>
<form method="post" action="/upload/" enctype="multipart/form-data">
    {% csrf_token %}
    <input type="file" name="pic"/><br>
    <input type="submit" value="上传">
</form>
</body>
</html>
```

## 编写上传视图

```python
def upload(request):
    file = request.FILES.get('pic')
    media_root = settings.MEDIA_ROOT
    path = 'news/{}/{}/{}/'.format(datetime.now().year, datetime.now().month, datetime.now().day)
    full_path = media_root + '/' + path
    print(full_path)
    if not os.path.exists(full_path):
        os.makedirs(full_path)
    with open(full_path + file.name, 'wb') as pic:
        for c in file.chunks():
            pic.write(c)
    Article.objects.create(title='ces', cover=path + file.name).save()
    return redirect('/show_media/')
```

效果如下

![](http://tp.jikedaohang.com/20191214232430_I9Z4fg_Screenshot.jpeg)




