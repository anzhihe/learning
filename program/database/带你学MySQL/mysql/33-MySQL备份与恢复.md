### 备份

```
mysqldump -u 用户名 -p 数据库名 表1 表2 > backup.sql

不写表名则备份整个库
```

##### 备份多个库

```
mysqldump -u 用户名 -p --databases 数据库名1 数据库名2 > backup.sql
```

##### 备份所有数据库

```
mysqldump -u 用户名 -p --all-databases > backup.sql
```

##### 导入备份

```
source backup.sql
```

