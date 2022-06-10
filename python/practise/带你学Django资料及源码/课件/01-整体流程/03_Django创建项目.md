# 创建王者荣耀项目
我用我们经常玩的王者游戏做案例，王者这里面应该会有很多模块，比如用户中心、英雄、符文等等

在一个项目中，应该会包含多个模块，每个模块对应网站上的一个功能。

## 1. 示例
创建项目的名称为wangzhe，完成"英雄-英雄类型"之间的关系，应用名称为game。

## 2. 创建项目
> 在当前用户的某个目录下创建项目，这样不会发生权限问题。

此处在/home/wengwenyu/django_project目录下创建项目

```python
cd /Users/xiaoyuan/Desktop
mkdir django_project
cd django_project
```

创建项目的命令如下：

```python
django-admin startproject 项目名称
例：
django-admin startproject wangzhe
```



## 3. 项目默认目录说明

目录结构如下：

- manage.py是项目管理文件，通过它管理项目。
- 与项目同名的目录，此处为wangzhe。
- ``_init_.py``是一个空文件，作用是这个目录wangzhe可以被当作包使用。
- settings.py是项目的整体配置文件。
- urls.py是项目的URL配置文件。
- wsgi.py是项目与WSGI兼容的Web服务器入口，详细内容会在布署中讲到。

## 4. 创建应用
使用一个应用开发一个业务模块，此处创建应用名称为game

创建应用的命令如下:
```python
python manage.py startapp game
```

- ``_init.py_``是一个空文件，表示当前目录booktest可以当作一个python包使用。
- tests.py文件用于开发测试用例，在实际开发中会有专门的测试人员，这个事情不需要我们来做。
- models.py文件跟数据库操作相关。
- views.py文件跟接收浏览器请求，进行处理，返回页面相关。
- admin.py文件跟网站的后台管理相关。
- migrations用来装迁移文件

##5. 配置应用

应用创建成功后，需要安装才可以使用，也就是建立应用和项目之间的关联，在test1/settings.py中INSTALLED_APPS下添加应用的名称就可以完成安装。

在INSTALLED_APPS加入应用的名字如下图：

![](http://tp.jikedaohang.com/20191112230521_GSOzfx_Screenshot.jpeg)

## 6. 运行服务器
在开发阶段，为了能够快速预览到开发的效果，django提供了一个纯python编写的轻量级web服务器，仅在开发阶段使用。

运行服务器命令如下：

```python
python manage.py runserver ip:端口
例：
python manage.py runserver
```
**可以不写IP和端口，默认IP是127.0.0.1，默认端口为8000。**

服务器成功启动后如下图：

![](http://tp.jikedaohang.com/20191112230647_vXt1aO_Screenshot.jpeg)

紧接着在浏览器中输入网址“127.0.0.1:8000”，或者按着ctrl键点击上图中标示出来的地址，可以查看当前站点开发效果。

> 如果增加、修改、删除文件，服务器会自动重启;
按ctrl+c停止服务器。

![](http://tp.jikedaohang.com/20191112230737_al6zHC_Screenshot.jpeg)

