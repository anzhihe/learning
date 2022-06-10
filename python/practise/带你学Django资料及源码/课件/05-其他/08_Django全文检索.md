### 全文检索

全文检索不同于特定字段的模糊查询，使用全文检索的效率更高，并且能够对于中文进行分词处理'

### 安装

whoosh：纯Python编写的全文搜索引擎。

jieba：一款免费的中文分词包，当然也有收费的。

haystack：全文检索的框架，支持whoosh、solr、Xapian、Elasticsearc四种全文检索引擎。

```
pip install django-haystack whoosh jieba
```



### 配置

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app.apps.AppConfig',
    'haystack'
]
```

```python
# 全文检索框架的配置
HAYSTACK_CONNECTIONS = {
    'default': {
        # 配置搜索引擎
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        # 配置索引文件目录
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}
# 指定每页显示的结果数量
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10

#当添加、修改、删除数据时，自动生成索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

```

### 模型类

```python
class Goods():
    name = models.CharField(verbose_name='名字', max_length=200)
    content = models.CharField(verbose_name='内容', max_length=200)

```

### 创建索引文件

在应用下创建名字为search_indexes.py的文件

```python
# 导入全文检索框架索引类
from haystack import indexes
from app.models import Goods
class GoodsSearchIndex(indexes.SearchIndex, indexes.Indexable):
    # 设置需要检索的主要字段内容 use_template表示字段内容在模板中
    text = indexes.CharField(document=True, use_template=True)
    # 获取检索对应对的模型
    def get_model(self):
        return Goods
    # 设置检索需要使用的查询集
    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

```



在模板下创建如下文件夹和文件，格式为：templates/search/indexes/应用名/模型名小写_text.txt

文件内容如下：

```
{{object.name}} #object就代表get_model()方法返回的对象
{{object.content}}
```

![](http://tp.jikedaohang.com/20191217212130_cW5dCZ_Screenshot.jpeg)

### 配置路由

```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', include('haystack.urls')),
    path('', include(('app.urls', 'app'), namespace='app')),
]
```

### 生成索引文件

```
python manage.py rebuild_index
```

### 创建搜索表单

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<form action="/search/" method="get">
    <input type="text" name="q" value="" placeholder="请输入搜索内容"/>
    <input type="submit" value="提交"/>
</form>


</body>
</html>
```

### 创建结果显示页面

在search文件夹下面创建search.html文件

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
{% if query %}
    <ul class="list-pro" style="margin-top: 20px">
        {% for result in page %}
            <li>
                <a href="{% url 'app:detail' result.object.pk %}"></a>
                <div class="shop-list-mid" style="width: 65%;">
                    <div class="tit">
                        <a href="{% url 'app:detail' result.object.pk %}">
                            {{ result.object.name }}
                        </a>
                    </div>
                </div>
            </li>
        {% empty %}
            <li>没有找到您搜索的内容</li>
        {% endfor %}
    </ul>
{% endif %}


</body>
</html>
```

![](http://tp.jikedaohang.com/20191217212615_8EE3TQ_Screenshot.jpeg)

效果如下：

![](http://tp.jikedaohang.com/20191217213409_XLpRFB_Screenshot.jpeg)

### 支持中文

在路径site-packages/haystack/backends/下创建ChineseAnalyzer.py

![](http://tp.jikedaohang.com/20191217213549_w1uqLo_Screenshot.jpeg)

文件内容是

```python
import jieba
from whoosh.analysis import Tokenizer, Token

class ChineseTokenizer(Tokenizer):
    def __call__(self, value, positions=False, chars=False,
                 keeporiginal=False, removestops=True,
                 start_pos=0, start_char=0, mode='', **kwargs):
        t = Token(positions, chars, removestops=removestops, mode=mode,
                  **kwargs)
        seglist = jieba.cut(value, cut_all=True)
        for w in seglist:
            t.original = t.text = w
            t.boost = 1.0
            if positions:
                t.pos = start_pos + value.find(w)
            if chars:
                t.startchar = start_char + value.find(w)
                t.endchar = start_char + value.find(w) + len(w)
            yield t

def ChineseAnalyzer():
    return ChineseTokenizer()
```

复制 whoosh_backend.py 改名为 whoosh_cn_backend.py

### 更改词语分析类

```
from .ChineseAnalyzer import ChineseAnalyzer
查找
analyzer=StemmingAnalyzer()
改为
analyzer=ChineseAnalyzer()
```

### 更改设置

```python
# 全文检索框架的配置
HAYSTACK_CONNECTIONS = {
    'default': {
        # 配置搜索引擎
        # 'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        # 中文分词 使用jieba的whoosh引擎
        'ENGINE': 'haystack.backends.whoosh_cn_backend.WhooshEngine',
        # 配置索引文件目录
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}

```

### 重新生成索引

```
python manage.py rebuild_index
```



### 关键词高亮与分页

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

</head>
<style>
    span.highlighted {
        color: red;
    }
</style>
<body>


{% if query %}
    {% load highlight %}

    <ul class="list-pro" style="margin-top: 20px">
        {% for result in page %}
            <li>
                <a href="{% url 'app:detail' result.object.pk %}"></a>
                <div class="shop-list-mid" style="width: 65%;">
                    <div class="tit">
                        <a href="{% url 'app:detail' result.object.pk %}">
                            {#                            {{ result.object.name }}#}
                            {% highlight result.object.name with query %}
                            {% highlight result.object.content with query %}
                        </a>
                    </div>
                </div>
            </li>
        {% empty %}
            <li>没有找到您搜索的内容</li>
        {% endfor %}

    </ul>


    {% if page.has_previous or page.has_next %}
        <div>
            {% if page.has_previous %}
                <a href="?q={{ query }}&amp;page={{ page.previous_page_number }}">{% endif %}&laquo; 上一页
            {% if page.has_previous %}</a>{% endif %}
            |
            {% if page.has_next %}<a href="?q={{ query }}&amp;page={{ page.next_page_number }}">{% endif %}下一页 &raquo;
            {% if page.has_next %}</a>{% endif %}
        </div>
    {% endif %}
{% else %}
{% endif %}


</body>
</html>
```