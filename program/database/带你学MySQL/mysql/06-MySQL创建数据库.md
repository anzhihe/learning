### 数据库命令

- 查看所有数据库

```
show databases;
```

![](https://tva1.sinaimg.cn/large/0082zybply1gc310bx84nj31yw0jggnr.jpg)

> 注：所展示的数据库，会跟你不一样

- 创建数据库

```
create database 数据库名 charset=utf8;
```

![](https://tva1.sinaimg.cn/large/0082zybply1gc31a47pf7j31yq02w74l.jpg)

- 切换数据库

```
use 数据库名;
```

- 查看当前所选数据库

```
select database();
```

- 删除数据库

```
drop database 数据库名;
```

- 修改数据库

```
ALTER DATABASE [数据库名] { 
[ DEFAULT ] CHARACTER SET <字符集名> |
[ DEFAULT ] COLLATE <校对规则名>}
```

```
ALTER DATABASE db_test
DEFAULT CHARACTER SET gb2312
DEFAULT COLLATE gb2312_chinese_ci;
```

- 查看编码类型

```
show character set;
```

- 查看数据库编码

```
show  create  database db_test;
```

