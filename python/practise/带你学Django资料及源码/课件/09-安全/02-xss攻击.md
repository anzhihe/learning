### XSS攻击

XSS( Cross-site scripting，跨站脚本攻击)是把输入的数据变成可执行的程序语句.

### 编写视图

```python
from django.shortcuts import render
msg = []
def comment(request):
        if request.method == "GET":
        return render(request,'comment.html')
    else:
        v = request.POST.get('content')
        if "script" in v:
            return render(request,'comment.html',{'error': '标签违法'})
        else:
            msg.append(v)
            return render(request,'comment.html')

def index(request):
    return render(request,'index.html',{'msg':msg})

def test(request):
    from django.utils.safestring import mark_safe
    temp = "<script>alert('哈哈')</script>"
    newtemp = mark_safe(temp)
    return render(request,'test.html',{'temp':newtemp}

```

### 编写视图

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <form method="POST" action="/comment/">
        <h4>评论</h4>
        <input type="text" name="content"/>
        <input type="submit" value="提交" />{{ error }}
    </form>
</body>
</html>
```



```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <h1>评论内容</h1>
    {% for item in msg %}
        <div>{{ item|safe }}</div>
    {% endfor %}
</body>
</html>

```

### bleach库

bleach库是用来清理包含html格式字符串的库。他可以指定哪些标签需要保留，哪些标签是需要过滤掉的。

```
pip install bleach
```

```
import bleach
from bleach.sanitizer import ALLOWED_TAGS,ALLOWED_ATTRIBUTES
from django.views.decorators.http import require_http_methods
 
@require_http_methods(['POST'])
def message(request):
    # 从客户端中获取提交的数据
    content = request.POST.get('content')
 
    # 在默认的允许标签中添加img标签
    tags = ALLOWED_TAGS + ['img']
    # 在默认的允许属性中添加src属性
    attributes = {**ALLOWED_ATTRIBUTES,'img':['src']}
 
    # 对提交的数据进行过滤
	content = bleach.clean(content, tags, attributes)
```

