### DELETE删除

通过`DELETE`可以删除表中的一条记录或者多条记录

```
DELETE FROM 表名 WHERE 条件;
```

![](https://tva1.sinaimg.cn/large/00831rSTly1gco1bxye64j31z40oeq75.jpg)

### 删除所有数据

```
DELETE FROM 表名;
```



### TRUNCATE删除

```
TRUNCATE TABLE 表名;
```

### DELETE和TRUNCATE区别

- DELETE支持条件，TRUNCATE不支持条件
- DELETE支持事务回滚，TRUNCATE不支持回滚
- DELETE清理速度比TRUNCATE要慢
- TRUNCATE自增值会初始化

