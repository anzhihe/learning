### 数据排序

当数据查询出来以后，我们可以对数据进行排序处理。在末尾使用order by语句。

```
select * from 表名 order by 列1 asc|desc,列2 asc|desc,...
```

> 注：
>
> asc即为升序，也是默认值。
>
> desc即为降序
>
> 排序首先先按照列1进行排序，如果出现结果相同的，在进行列2排序



```
select * from users
where age > 10 order by id desc;
```

![](https://tva1.sinaimg.cn/large/00831rSTly1gco074wdphj31yw0awmz5.jpg)

```
select * from users
where age > 10 order by id asc;
```

![](https://tva1.sinaimg.cn/large/00831rSTly1gco07zci0uj31yq0bwjtd.jpg)