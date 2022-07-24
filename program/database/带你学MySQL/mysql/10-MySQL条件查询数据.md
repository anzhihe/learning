### 条件查询

利用where语句可以对数据进行筛选

```
select * from 表名 where 条件;
```

### 比较运算符

| 运算符 | 描述     | 例子                 |
| ------ | -------- | -------------------- |
| =      | 等于     | where id = 1         |
| \>     | 大于     | where age > 10       |
| <      | 小于     | where age < 10       |
| >=     | 大于等于 | where age >= 10      |
| <=     | 小于等于 | where age <= 10      |
| !=     | 不等于   | where name != '老王' |

```
select * from users where id = 1;
```

![](https://tva1.sinaimg.cn/large/00831rSTly1gcmw82514yj31yw0c475n.jpg)

### 逻辑运算符

| 运算符 | 描述 | 例子                      |
| ------ | ---- | ------------------------- |
| and    | 并且 | where id = 1 and age > 10 |
| or     | 或者 | where id = 1 or age > 10  |
| not    | 取反 | where not id = 1          |

```sql
select * from users where id = 1 and age = 30;
```

![](https://tva1.sinaimg.cn/large/00831rSTly1gcmw8ny6rej31yg0j4tb5.jpg)



```sql
select * from users where not id = 1;
```

![](https://tva1.sinaimg.cn/large/00831rSTly1gcmw99wglrj31z20deabs.jpg)

### 范围查询

| 运算符              | 描述                 | 例子                      |
| ------------------- | -------------------- | ------------------------- |
| in                  | 在指定的非连续范围内 | where id in(1,3,5);       |
| between ... and ... | 在指定的连续范围内   | where id between 1 and 5; |

```
select * from users where id in (1,3,4);
```

![](https://tva1.sinaimg.cn/large/00831rSTly1gcmwbd14pxj31y40csjt3.jpg)

```
select * from users where id between 1 and 5;
```

![](https://tva1.sinaimg.cn/large/00831rSTly1gcmwcfwf7kj31ys0daq4x.jpg)

### 空判断

| 运算符      | 描述           | 例子                   |
| ----------- | -------------- | ---------------------- |
| is null     | 判断是否为空   | where name is null     |
| is not null | 判断是否不为空 | where name is not null |

> 注：null与''是不一样的

```
INSERT INTO users (name, birth_date, phone,age) VALUES ('', '1990-01-01', '13813145213',30);
```

```
INSERT INTO users (name, birth_date, phone,age) VALUES (null, '1990-01-01', '13813145213',30);
```



![](https://tva1.sinaimg.cn/large/00831rSTly1gcmwpxwkh0j31z20po78z.jpg)

```
 INSERT INTO users (name, birth_date, phone,age) VALUES ('老张', null, '17813145213',30);
```

![](https://tva1.sinaimg.cn/large/00831rSTly1gcmwz4gsqcj31y60lkwi7.jpg)



```
select * from users  where brith_date is null;
```

![](https://tva1.sinaimg.cn/large/00831rSTly1gcmx0jheymj31yq0aymyj.jpg)

### 模糊查询

| 运算符 | 描述                         | 例子                   |
| ------ | ---------------------------- | ---------------------- |
| like   | 简单的模式匹配               | where name like '老王' |
|        | where name like '老王%'      | 以老王开头             |
|        | where name like '%老王'      | 以老王结尾             |
|        | where name like '%老王%'     | 任意地方包含老王       |
|        | where name not like '%老王%' | 任意地方都不包含老王   |

```
select * from users  where name like '王%';
select * from users  where name like '%王';
```

![](https://tva1.sinaimg.cn/large/00831rSTly1gcmx1ucfdoj31yq0heq5f.jpg)

### 优先级

- 小括号，not，比较运算符，逻辑运算符
- and比or先运算，如果同时出现并希望先算or，需要结合()使用

