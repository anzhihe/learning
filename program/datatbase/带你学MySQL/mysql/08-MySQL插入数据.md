### 插入数据

```
insert into 表名 (列1,...) values(值1,...)
```

![](https://tva1.sinaimg.cn/large/0082zybply1gc33vioq7dj31yq0bidhc.jpg)

- 缺省插入

```
INSERT INTO users (name, birth_date, phone,age)
VALUES ('老王', '1990-01-01', '13813145211',30);
```

![](https://tva1.sinaimg.cn/large/0082zybply1gc33vuhhvvj31yu038wf3.jpg)

- 全列插入

```
INSERT INTO users VALUES (0,'老宋', '1990-01-01', '13823145212',30);# 全列插入 不需要写字段
```

![](https://tva1.sinaimg.cn/large/0082zybply1gc33zz51n1j31yu02emxl.jpg)

- 不同

主键列是自动增长，但是在全列插入时需要占位，通常使用0，插入成功后以实际数据为准

### 查询数据

```
select * from 表名
```

![](https://tva1.sinaimg.cn/large/0082zybply1gc47rdiqndj31ys08aq3v.jpg)