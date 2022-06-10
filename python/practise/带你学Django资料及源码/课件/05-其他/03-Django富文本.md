# 富文本编辑器 

富文本编辑器，在web开发中可以说是不可缺少的。django并没有自带富文本编辑器，因此我们需要自己集成，富文本会让我的页面变的更加丰富。

## 下载

```
https://github.com/twz915/DjangoUeditor3/
```

## 安装

进入到项目文件夹，运行下面命令

```python
 python setup.py install
```

## 设置

```python
# 上传图片
MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace("\\", "/")
MEDIA_URL = '/media/'
```

## 注册应用

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app.apps.AppConfig',
    'DjangoUeditor'
]
```



## 模型类

```python 
class News(models.Model):
    title = models.CharField(verbose_name='产品标题', max_length=20)
    Content = UEditorField(width=600, height=300, toolbars="full",
                           imagePath="news/%(basename)s_%(datetime)s.%(extname)s", filePath="files/")
    vnum = models.IntegerField(verbose_name='浏览量', default=100)
    is_top = models.BooleanField(verbose_name='是否置顶', default=False)
    is_show = models.BooleanField(verbose_name='是否展示', default=True)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    class Meta:
        verbose_name = '新闻'
        verbose_name_plural = '新闻'

    def __str__(self):
        return self.title
```

- *width，height* :编辑器的宽度和高度，以像素为单位。

- imagePath* :图片上传后保存的路径,如"images/",实现上传到"{{MEDIA_ROOT}}/images"文件夹。 注意：如果imagePath值只设置文件夹，则未尾要有"/" imagePath可以按python字符串格式化：如"images/%(basename)s_%(datetime)s.%(extname)s"。这样如果上传test.png，则文件会 被保存为"{{MEDIA_ROOT}}/images/test_20140625122399.png"。 imagePath中可以使用的变量有：

 

| 字段     | 描述                         | 说明                                             |
| -------- | ---------------------------- | ------------------------------------------------ |
| time     | 上传时的时间                 | datetime.datetime.now().strftime("%H%M%S")       |
| date     | 上传时的日期                 | datetime.datetime.now().strftime("%Y%m%d")       |
| datetime | 上传时的时间和日期           | datetime.datetime.now().strftime("%Y%m%d%H%M%S") |
| year     | 年                           |                                                  |
| month    | 月                           |                                                  |
| day      | 日                           |                                                  |
| rnd      | 三位随机数                   | random.randrange(100,999)                        |
| basename | 上传的文件名称，不包括扩展名 |                                                  |
| extname  | 上传的文件扩展名             |                                                  |
| filename | 上传的文件名全称             |                                                  |



- time :上传时的时间，datetime.datetime.now().strftime("%H%M%S")
- date ：上传时的日期，datetime.datetime.now().strftime("%Y%m%d")
- datetime ：上传时的时间和日期，datetime.datetime.now().strftime("%Y%m%d%H%M%S")
- year : 年
- month : 月
- day : 日
- rnd : 三位随机数，random.randrange(100,999)
- basename ： 上传的文件名称，不包括扩展名
- extname : 上传的文件扩展名
- filename : 上传的文件名全称



## 编写路由

```python
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.views.static import serve

from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include(('app.urls', 'app'), namespace='app')),
                  path('ueditor/', include('DjangoUeditor.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## 报错解决

![](http://tp.jikedaohang.com/20191214215939_M5BmnU_Screenshot.jpeg)

![](http://tp.jikedaohang.com/20191214220025_lAJ8CY_Screenshot.jpeg)

## 在管理后台添加数据



## 编写模板

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .center {
            text-align: center;
        }

    </style>
</head>

<body>

<div class="center">
    <h1>{{ news.title }}</h1>
    {{ news.Content|safe }}

</div>

</body>
</html>
```





![](http://tp.jikedaohang.com/20191214221907_UdGsw3_Screenshot.jpeg)



