### 分组

字段分组，字段相同的数据会被放到一个组中。

```
select 列1,列2,聚合... from 表名 group by 列1,列2,列3...
```

根据名字分组 统计名字的个数

```
select name,count(*) as name_count from users group by name;
```

![](https://tva1.sinaimg.cn/large/00831rSTly1gd34fu59nxj31yo0hq0um.jpg)



### having过滤分组

where在数据分组前进行过滤，having在数据分组后进行过滤。

```
select name,count(*) as name_count from users group by name having name_count >= 2 ;
```

![](https://tva1.sinaimg.cn/large/00831rSTly1gd34jirbkrj31xy0buq48.jpg)

### select子句顺序

| 子句     | 说明     |
| -------- | -------- |
| Select   | 返回的列 |
| From     | 检索的表 |
| where    | 行级过滤 |
| group by | 分组     |
| having   | 组级过滤 |
| Order by | 排序     |
| Limit    | 限制查询 |

