### 表命令

- 查看所有表

```
show tables;
```

![](https://tva1.sinaimg.cn/large/0082zybply1gc31azo9uwj31ys04gjru.jpg)

- 创建表

```
CREATE TABLE table_name (
    column1_name data_type constraints,
    column2_name data_type constraints,
    ....
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

创建一个用户表

```
CREATE TABLE users (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    birth_date DATE,
    phone VARCHAR(11) NOT NULL UNIQUE
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

![](https://tva1.sinaimg.cn/large/0082zybply1gc33sxl0lpj31ye0gudhx.jpg)

上面的语句创建了一个名为users的表，其中包含5个字段`id`、`name`、`birth_date`和`phone`。注意，每个字段后面都有一个数据类型声明，表示该字段将存储何种类型的数据，例如：整数、字符串、日期等。

### MySQL支持的常用数据类型

- 数字型

| 数据类型     | 字节                                     | 范围（无符号）unsigned                                       | 范围（有符号）<br> signed(默认)                              | **描述**                                                     |
| ------------ | :--------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| tinyint      | 1                                        | (0，255)                                                     | (-128，127)                                                  | 小整数值                                                     |
| decimal      | 2                                        | (0，65535)                                                   | (-32768，32767)                                              | 大整数值                                                     |
| mediumint    | 3                                        | (0，16 777 215)                                              | (-8 388 608，8 388 607)                                      | 大整数值                                                     |
| int          | 4                                        | (0，4 294 967 295)                                           | (-2 147 483 648，2 147 483 647)                              | 大整数值                                                     |
| bigint       | 8                                        | (0，18 446 744 073 709 551 615)                              | (-9,223,372,036,854,775,808，9 223 372 036 854 775 807)      | 极大整数值                                                   |
| FLOAT(M,D)   | 4                                        | 0，(1.175 494 351 E-38，3.402 823 466 E+38)                  | (-3.402 823 466 E+38，-1.175 494 351 E-38)，0，(1.175 494 351 E-38，3.402 823 466 351 E+38) | 单精度<br/>浮点数值<br>M是数字总个数，D是小数点后个数        |
| double(M,D)  | 8                                        | 0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308) | (-1.797 693 134 862 315 7 E+308，-2.225 073 858 507 201 4 E-308)，0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308) | 双精度<br/>浮点数值<br/>M是数字总个数，D是小数点后个数       |
| decimal(M,D) | 对DECIMAL(M,D) ，如果M>D，为M+2否则为D+2 | 依赖于M和D的值                                               | 依赖于M和D的值                                               | `M是表示有效数字数的精度。 `M`范围为`1〜65`。 `D`是表示小数点后的位数。 `D`的范围是`0`~`30`。MySQL要求`D`小于或等于(`<=`)M`。 |

> 单精度和双精度不同
>
> 1、在内存中占有的字节数不同
>
> 2、有效数字位数不同
>
> 3、所能表示数的范围不同

- 字符串

| 类型    | 字节         | 说明       |
| ------- | ------------ | ---------- |
| char    | 0-255字节    | 定长字符串 |
| varchar | 0-65535 字节 | 变长字符串 |
| text    | 0-65 535字节 | 长文本数据 |

- 日期

| 类型     | 大小 | 范围                                    | 格式                | 说明     |
| -------- | ---- | --------------------------------------- | ------------------- | -------- |
| date     | 3    | 1000-01-01/9999-12-31                   | YYYY-MM-DD          | 日期     |
| time     | 3    | '-838:59:59'/'838:59:59'                | HH:MM:SS            | 时间     |
| datetime | 8    | 1000-01-01 00:00:00/9999-12-31 23:59:59 | YYYY-MM-DD HH:MM:SS | 日期时间 |
| year     | 1    | 1901/2155                               | YYYY                | 年份类型 |



### MySQL支持的常用约束

| 修饰符      | 描述 |
| ----------- | ---- |
| primary key | 主键 |
| not null    | 非空 |
| unique      | 唯一 |
| default     | 默认 |
| foreign key | 外键 |

### 存储引擎

MySQL中的数据用各种不同的技术存储在文件（或者内存）中。这些技术中的每一种技术都使用不同的存储机制、索引技巧、锁定水平并且最终提供广泛的不同的功能和能力。通过选择不同的技术，你能够获得额外的速度或者功能，从而改善你的应用的整体功能。

![](https://tva1.sinaimg.cn/large/00831rSTly1gcqeui5sugj30i809kdgl.jpg)

```
show engines;
```





- 查看表结构

```
desc 表名;
```

- 查看表的创建语句

```
show create table '表名';
```

- 更改表名称

```
rename table 原表名 to 新表名;
```

- 修改表

```
alter table 表名 add|change|drop 列名 类型;

alter table users add age int default 1;
```

```
alter table users add user_desc varchar(50) default '哈哈';
alter table users change user_desc userdesc varchar(50);
```

```
alter table users drop userdesc
```

- 删除表

```
drop table 表名;
```



### 更新约束

先创建一个表,除了主键，不加其他约束。

```
CREATE TABLE users1 (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    birth_date DATE,
    phone VARCHAR(11)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

给手机号添加唯一约束

```
ALTER TABLE users1 ADD UNIQUE (phone);
```

删除唯一约束

```
ALTER TABLE users1 DROP INDEX phone;
```

给名字添加非空约束

```
ALTER TABLE users1 modify name VARCHAR(50) not null;
```

删除非空约束

```
ALTER TABLE users1 
CHANGE COLUMN `name` `name` VARCHAR(50) NULL ;
```

给生日添加默认约束

```
ALTER TABLE users1 ALTER birth_date SET DEFAULT '1992-05-11';
```

删除默认约束

```
ALTER TABLE users1 ALTER birth_date DROP DEFAULT;
```

