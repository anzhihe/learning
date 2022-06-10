

## 定义属性

Django根据属性的类型确定以下信息：

- 当前选择的数据库支持字段的类型
- 渲染管理表单时使用的默认html控件
- 在管理站点最低限度的验证
django会为表创建自动增长的主键列，每个模型只能有一个主键列，如果使用选项设置某属性为主键列后django不会再创建自动增长的主键列。

默认创建的主键列属性为id，可以使用pk代替，pk全拼为primary key。

> 注意：pk是主键的别名，若主键名为id2，那么pk是id2的别名。

属性命名限制：

- 不能是python的保留关键字。
- 不允许使用连续的下划线，这是由django的查询方式决定的，在后面会详细讲解查询。
- 定义属性时需要指定字段类型，通过字段类型的参数指定选项，语法如下：
```python
属性=models.字段类型(选项)
```

## 字段类型

使用时需要引入django.db.models包，字段类型如下：

- AutoField：自动增长的IntegerField，通常不用指定，不指定时Django会自动创建属性名为id的自动增长属性。(必须填入参数primary_key=True)
```python
from django.db import models

    class UserInfo(models.Model):
        # 自动创建一个列名为id的且为自增的整数列
        username = models.CharField(max_length=32)

    class Group(models.Model):
        # 自定义自增列
        nid = models.AutoField(primary_key=True)
        name = models.CharField(max_length=32)
```

- BooleanField：布尔字段，值为True或False。
- NullBooleanField：支持Null、True、False三种值。
- CharField(max_length=字符长度)：字符串。
    - 参数max_length表示最大字符个数。
- TextField：大文本字段，一般超过4000个字符时使用。
- IntegerField：整数。
- DecimalField(max_digits=None, decimal_places=None)：十进制浮点数。
    - 参数max_digits表示总位数。
    - 参数decimal_places表示小数位数。
- FloatField：浮点数。
- DateField[auto_now=False, auto_now_add=False])：日期。
    - 参数auto_now表示每次保存对象时，自动设置该字段为当前时间，用于"最后一次修改"的时间戳，它总是使用当前日期，默认为false。
    - 参数auto_now_add表示当对象第一次被创建时自动设置当前时间，用于创建的时间戳，它总是使用当前日期，默认为false。
    - 参数auto_now_add和auto_now是相互排斥的，组合将会发生错误。
- TimeField：时间，参数同DateField。
- DateTimeField：日期时间，参数同DateField。
- FileField：上传文件字段。

| 参数 | 说明 |
|:------|:------:|
|upload_to = ""| 上传文件的保存路径如：upload_to = "uploads/%Y/%m/%d/“ |
- ImageField：继承于FileField，对上传的内容进行校验，确保是有效的图片。



| 参数              |                           说明                            |
| :---------------- | :-------------------------------------------------------: |
| upload_to = ""    |                    上传文件的保存路径                     |
| storage = None    | 存储组件，默认django.core.files.storage.FileSystemStorage |
| width_field=None  |        上传图片的高度保存的数据库字段名（字符串）         |
| height_field=None |        上传图片的宽度保存的数据库字段名（字符串）         |


## 选项

通过选项实现对字段的约束，选项如下：

- null：如果为True，表示允许为空，默认值是False。
- blank：如果为True，则该字段允许为空白，默认值是False。
- **对比：null是数据库范畴的概念，blank是表单验证范畴的。**
- db_column：字段的名称，如果未指定，则使用属性的名称。
- db_index：若值为True, 则在表中会为此字段创建索引，默认值是False。
- default：默认值。
- primary_key：若为True，则该字段会成为模型的主键字段，默认值是False，一般作为AutoField的选项使用。
- unique：如果为True, 这个字段在表中必须有唯一值，默认值是False。

## 关联数据 on_delete

-  CASCADE:这就是默认的选项，级联删除。
- PROTECT: 保护模式，如果采用该选项，删除的时候，会抛出`ProtectedError`错误。
- SET_NUL`: 置空模式，删除的时候，外键字段被设置为空，前提就是`blank=True, null=True`,定义该字段的时候，允许为空。
- SET_DEFAULT: 置默认值，删除的时候，外键字段设置为默认值，所以定义外键的时候注意加上一个默认值。
- SET(): 自定义一个值，该值当然只能是对应的实体了

```python
**官方案例**
def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class MyModel(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
    )
```



## 综合演练
修改booktest/models.py中的模型类，代码如下：
```python
from django.db import models

# 分类表
class Category(models.Model):
    title = models.CharField(max_length=20)

    position = models.IntegerField(default=1)  # 用来排序

    isshow = models.BooleanField(default=True)  # 用于是否展示

    isdelete = models.BooleanField(default=False)  # 用于是否删除

    create_time = models.DateTimeField(auto_now_add=True)  # 用于表示创建时间

    update_time = models.DateTimeField(auto_now=True)  # 用于表示更新时间

    def __str__(self):
        return self.title 
# 文章表
class Article(models.Model):
    title = models.CharField(max_length=100)

    content = models.TextField(max_length=5000)

    Category = models.ForeignKey(to=Category)  # 一对多 必须写在多的里面

    user = models.ForeignKey(to=User)  # 一对多
	
  	def __str__(self):
        return self.title

# 用户表
class User(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
```
然后生成迁移文件并执行迁移命令，最后查看db_1903数据库中的内容。