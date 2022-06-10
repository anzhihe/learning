### SQL注入

通过非法的SQL命令，达到欺骗服务器的目录。查到的数据就会出现一些意想不到的效果。一些网站被爆一般都是通过非法的SQL命令获取。

### 编写视图

```
from django.db import connection
def get_data(request):
    id = request.GET.get('id')
    cursor = connection.cursor()
    sql = "select id,name from app04_user where id=%s" % id
    print(sql)
    cursor.execute(sql)
    rows = cursor.fetchall()
    ctx = {
        'rows': rows
    }
    return render(request, 'app04/show.html', ctx)
```

### 编写模板

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<ul>
    {% for row in rows %}
        <li>{{ row.1 }}</li>
    {% endfor %}

</ul>

</body>
</html>
```

这样表面上看起来没有问题。但是如果用户传的user_id是等于1 or 1=1，那么以上拼接后的sql语句为：

```
select id,username from front_user where id=1 or 1=1

select id,username from front_user where 'username=xiao' or '1=1'
```

- 永远要进行前端参数校验
- 永远不要拼接SQL
- 永远加密一下重要信息
- 永远不要给出具体的错误类型
- 永远不要用root去管理数据库

### 如何防御sql注入

- 使用ORM去查询数据
- 使用参数形式查询数据