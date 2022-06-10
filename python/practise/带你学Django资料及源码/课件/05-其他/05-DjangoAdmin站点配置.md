### 注册模型管理

```
class ArticleAdmin(admin.ModelAdmin):
    pass
```

参数注册
```python
admin.site.register(AreaInfo,AreaAdmin)
```

装饰器注册

```python
@admin.register(AreaInfo)
class AreaAdmin(admin.ModelAdmin):
    pass
```

### 页大小

```python
list_per_page=100
```

### 动作栏

```
actions_on_top=True
```



### 显示字段

```python
list_display=[模型字段1,模型字段2,...]
```



**将方法作为列**

列可以是模型字段，还可以是模型方法，要求方法有返回值。

```python
class Article(models.Model):
    def show_title(self):
        return self.title
```

```python
list_display = ['id','show_title','title']
```



指定方法字段排序的依据

```
admin_order_field=模型类字段
```

```python
class Article(models.Model):
    def show_title(self):
        return self.title
    show_title.admin_order_field='vnum'
```

### **列标题**

```
short_description='列标题'
```

### 搜索框

```python
search_fields=[]
```



### 编辑页

属性如下：

```
fields=[]
```

### 分组显示

```
fieldsets=(
    ('标题1',{'fields':('字段1','字段2')}),
    ('标题2',{'fields':('字段3','字段4')}),
)
```

> 注意：fields与fieldsets只能用一个。

### 关联对象

```python
class CategoryStackedInline(admin.StackedInline): # TabularInline
    model = Article
    extra = 2
```

```python
class CategoryAdmin(admin.ModelAdmin):
    ...
    inlines = [AreaStackedInline]
```


