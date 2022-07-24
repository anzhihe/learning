### 字段去重

在数据表中，可能会有重复的数据，我们可以通过`distinct`去掉重复的行。

```
SELECT DISTINCT name from users;
```

![](https://tva1.sinaimg.cn/large/00831rSTly1gco0itbaicj31yo0lgq5p.jpg)

### 作用于多列

```
SELECT DISTINCT name,id from users;
```

