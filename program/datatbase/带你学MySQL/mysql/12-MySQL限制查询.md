### 限制查询

我们通过limit可以限制返回结果的行数

```
select * from 表名 limit count;
```



```
select * from users limit 3;
```

![](https://tva1.sinaimg.cn/large/00831rSTly1gco0a2p8c4j31y208udha.jpg)

### 指定从第几行起，返回多少行

```
select * from 表名 limit start,count;
```

```
select * from users limit 2,3;
相等
select * from users limit 3 offset 2;
```

![](https://tva1.sinaimg.cn/large/00831rSTly1gco0ar4al1j31yg08ota5.jpg)

### 取最大值

```
select * from users order by age desc limit 1;
```

![](https://tva1.sinaimg.cn/large/00831rSTly1gco0cr9d7rj31wy07qgmp.jpg)

### 取最小值

```
select * from users order by age asc limit 1;
```

### 分页

```
select * from users  limit (page-1)*pageSize,pageSize;
```

![](https://tva1.sinaimg.cn/large/00831rSTly1gco0fwo1kyj31yo0estb1.jpg)