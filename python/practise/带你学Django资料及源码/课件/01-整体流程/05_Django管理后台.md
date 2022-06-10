

# 后台管理

网站的数据每天都会产生变化，既然产生了变化，就一定会有数据增删改查。那如何实现对数据增删改查呢？那就需要用到网站的后台管理。

**使用Django的管理模块，需要按照如下步骤操作：**
- 1. 管理界面本地化
- 2. 创建管理员
- 3. 注册模型类
- 4. 自定义管理页面

## 1. 管理界面本地化
本地化是将显示的语言、时间等使用本地的习惯，这里的本地化就是进行中国化，中国大陆地区使用简体中文，时区使用``亚洲/上海时区``，注意这里不使用北京时区表示。

- 打开wangzhe/settings.py文件，找到语言编码、时区的设置项，将内容改为如下：

```python 
LANGUAGE_CODE = 'zh-hans' #使用中国语言
TIME_ZONE = 'Asia/Shanghai' #使用中国上海时间
```

## 2. 创建管理员
- 创建管理员的命令如下，按提示输入用户名、邮箱、密码。
```python
python manage.py createsuperuser
```

![](http://tp.jikedaohang.com/20191114205150_b85kn2_Screenshot.jpeg)

- 接下来启动服务器

```python
python manage.py runserver
```

- 打开浏览器，在地址栏中输入如下地址后回车。
```python
http://127.0.0.1:8000/admin/
```

![image-20191114205259921](/Users/xiaoyuan/Library/Application Support/typora-user-images/image-20191114205259921.png)

登录成功后界面如下，接下来进行第三步操作。

![](http://tp.jikedaohang.com/20191114205532_CodvxL_Screenshot.jpeg)


## 3. 注册模型类
**登录后台管理后，默认没有我们创建的应用中定义的模型类，需要在自己应用中的admin.py文件中注册，才可以在后台管理中看到，并进行增删改查操作。**

- 打开game/admin.py文件，编写如下代码：
```python
from .models import *

admin.site.register(Hero)
admin.site.register(Skill)
```
- 到浏览器中刷新页面，可以看到模型类BookInfo和HeroInfo的管理了。

![](http://tp.jikedaohang.com/20191114205507_eqvawm_Screenshot.jpeg)

- 接下来，我们就可以对数据实现增删改查了。

