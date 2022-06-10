
# 模型设计

我们之前操作数据库是通过写sql语句，那么能不能不写sql语句就可以操作数据库呢？ 可以，就是通过接下来要给大家讲的ORM框架。

# ORM框架
O是object，也就**类对象**的意思，R是relation，翻译成中文是关系，也就是关系数据库中数据表的意思，M是mapping，是**映射**的意思。在ORM框架中，它帮我们把类和数据表进行了一个映射，可以让我们**通过类和类对象就能操作它所对应的表格中的数据**。ORM框架还有一个功能，它可以**根据我们设计的类自动帮我们生成数据库中的表格**，省去了我们自己建表的过程。

django中内嵌了ORM框架，不需要直接面向数据库编程，而是定义模型类，通过模型类和对象完成数据表的增删改查操作。

使用django进行数据库开发的步骤如下：

1. 在models.py中定义模型类
2. 迁移
3. 通过类和对象完成数据增删改查操作

下面我们以保存图书信息为例来给大家介绍Django中进行数据库开发的整个流程。

## 1. 定义模型类
模型类定义在models.py文件中，继承自models.Model类。

> 说明: 不需要定义主键列，在生成时会自动添加，并且值为自动增长。

### 1.1 设计英雄类
英雄类:
- 类名:Hero
- 英雄名字:name
- 英雄性别:gender
- 英雄职位:job

### 1.2 模型类的设计
根据设计，在models.py中定义模型类如下：

```python
from django.db import models


# Create your models here.
class Hero(models.Model):
    name = models.CharField(verbose_name='英雄名字', max_length=10)
    gender = models.IntegerField('英雄性别', default=0)
    job = models.CharField('英雄职位', max_length=10)
```

## 2. 迁移
迁移前目录结构如下图：

![](http://tp.jikedaohang.com/20191114111815_hsVBqb_Screenshot.jpeg)

迁移由两步完成:
- 1. 生成迁移文件：根据模型类生成创建表的迁移文件。
- 2. 执行迁移：根据第一步生成的迁移文件在数据库中创建表。

生成迁移文件命令如下:
```python
python manage.py makemigrations
```

![image-20191114111757541](/Users/xiaoyuan/Library/Application Support/typora-user-images/image-20191114111757541.png)

执行生成迁移文件命令后，会在应用booktest目录下的migrations目录中生成迁移文件。

Django框架根据我们设计的模型类生成了迁移文件，在迁移文件中我们可以看到fields列表中每一个元素跟BookInfo类属性名以及属性的类型是一致的。同时我们发现多了一个id项，这一项是Django框架帮我们自动生成的，在创建表的时候id就会作为对应表的主键列，并且主键列自动增长。

执行迁移命令如下：
```python
python manage.py migrate
```

![](http://tp.jikedaohang.com/20191114111916_QGG3un_Screenshot.jpeg)

当执行迁移命令后，Django框架会读取迁移文件自动帮我们在数据库中生成对应的表格。



按照下图的步骤找到要打开的数据库文件。

![](http://tp.jikedaohang.com/20191114112024_hBkAsb_Screenshot.jpeg)



### 2.1 默认生成的表名称
细心的同学会发现我们上面生成的表的名字叫做booktest_bookinfo，booktest是应用的名字，bookinfo是模型类的名字。

数据表的默认名称为：
```python
<app_name>_<model_name>
```

![](http://tp.jikedaohang.com/20191114112127_2f3EF2_Screenshot.jpeg)

## 3. 设计技能类

技能类：
- 类名：Kill
- 技能名字：name
- 冷却时间：time
- 技能是哪个英雄：hero
- 英雄与技能关系为一对多
```python
class Skill(models.Model):
    name = models.CharField(verbose_name='技能名字', max_length=20)
    time = models.IntegerField(verbose_name='冷却时间', default=3)
    hero = models.ForeignKey(to=Hero, on_delete=models.CASCADE)
```
这里要说明的是，Hero类和Skill类之间具有一对多的关系，这个一对多的关系应该定义在多的那个类，也就是Skill类中。

> ```
> hero = models.ForeignKey(to=Hero, on_delete=models.CASCADE) //一对多关系
> ```

**在我们之后迁移生成表的时候，Django框架就会自动帮我们在英雄和技能之间建立一个外键关系。**

生成迁移文件：
```python
python manage.py makemigrations
```

结果如下图:

![](http://tp.jikedaohang.com/20191114112718_491Pi9_Screenshot.jpeg)




执行迁移的命令：
```python
python manage.py migrate
```

![](http://tp.jikedaohang.com/20191114112812_b7Sine_Screenshot.jpeg)

最后我们可以看到数据库中生成的英雄表如下图：

![](http://tp.jikedaohang.com/20191114113023_4WUuA0_Screenshot.jpeg)

### 3.1 数据操作

完成数据表的迁移之后，下面就可以通过进入项目的shell，进行简单的API操作。如果需要退出项目，可以使用ctrl+d快捷键或输入quit()。

进入项目shell的命令：
```python
python manage.py shell
```

![选区_205](https://i.loli.net/2018/08/05/5b65ec4b744ca.png)

首先引入game/models中的类：
```python
from game.models import *
```
查询所有英雄信息：
```python
Hero.objects.all()
```
因为当前并没有数据，所以返回空列表

新建图书对象：
```python
hero = Hero()
hero.name = '鲁班'
hero.gender = 1
hero.job = '射手'
hero.save()
```
再次查询所有图书信息：
```python
BookInfo.objects.all()
```
![](http://tp.jikedaohang.com/20191114113414_jlrK7p_Screenshot.jpeg)

查找英雄信息并查看值：

```python
hero = Hero.objects.get(id=1)
hero.name
```
![](http://tp.jikedaohang.com/20191114113515_HuDMXk_Screenshot.jpeg)

修改英雄信息：

```python
hero.gender = 0
hero.save()
```
删除英雄信息：
```python
hero.delete()
```
### 3.2 对象的关联操作

创建一个BookInfo对象
```python
b=BookInfo()
b.btitle='abc'
b.bpub_date=date(2017,1,1)
b.save()
```
创建一个Kill对象
```python
skill = Skill()
skill.name = '太空扫射'
skill.time = 3
skill.hero = hero
skill.save()
```
英雄与技能是一对多的关系，django中提供了关联的操作方式。

获得关联集合：返回当前英雄对象的所有的技能。
```python
hero.skill_set.all()
```

![](http://tp.jikedaohang.com/20191114113901_qM3OIm_Screenshot.jpeg)

