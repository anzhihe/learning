# 1.真的需要索引吗？
MySQL索引的建立对于MySQL的高效运行是很重要的，**索引可以大大提高MySQL的检索速度**。

打个比方，如果合理的设计且使用索引的MySQL是一辆兰博基尼的话，那么没有设计和使用索引的MySQL就是一个人力三轮车。

拿汉语字典的目录页（索引）打比方，我们可以按拼音、笔画、偏旁部首等排序的目录（索引）快速查找到需要的字。

>索引分单列索引和组合索引。单列索引，即一个索引只包含单个列，一个表可以有多个单列索引，但这不是组合索引。组合索引，即一个索引包含多个列。

上面都在说使用索引的好处，但过多的使用索引将会造成滥用。因此索引也会有它的缺点：虽然索引大大提高了查询速度，同时却会降低更新表的速度，如对表进行`INSERT、UPDATE`和`DELETE`。因为更新表时，MySQL不仅要保存数据，还要保存一下索引文件。

建立索引会占用磁盘空间的索引文件。

# 2.什么是索引


    索引（在 MySQL 中也叫“键key”）是存储引擎快速找到记录的一种数据结构
    ——《高性能MySQL》
我们需要知道索引其实是一种数据结构，其功能是帮助我们快速匹配查找到需要的数据行，是数据库性能优化最常用的工具之一。其作用相当于**超市里的导购员、书本里的目录**。

# 3.测试表

本篇文章，我们将从索引基础开始，介绍什么是索引以及索引的几种类型，然后学习如何创建索引以及索引设计的基本原则。
本篇文章中用于测试索引创建的user表的结构如下：
```sql
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `gender` int(1) NOT NULL,
  `age` int(3) NOT NULL,
  `status` int(1) NOT NULL,
  `remark` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;
```

# 4.索引类型
查看索引详情

```
SHOW INDEX FROM table_name;
```
例如：

```sql
mysql> SHOW INDEX FROM user;
+-------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table | Non_unique | Key_name | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment |
+-------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| user  |          0 | PRIMARY  |            1 | id          | A         |           0 | NULL     | NULL   |      | BTREE      |         |               |
+-------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
1 row in set (0.03 sec)

```

## 4.1.主键索引
它是一种特殊的唯一索引，不允许有空值。一般是在建表的时候同时创建主键索引。主键索引就是之前的主键约束！

**Primary key**

```sql
mysql> SHOW INDEX FROM user;
+-------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table | Non_unique | Key_name | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment |
+-------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| user  |          0 | PRIMARY  |            1 | id          | A         |           0 | NULL     | NULL   |      | BTREE      |         |               |
+-------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
1 row in set (0.03 sec)

```
>注意：一个表只能有一个主键
## 4.2.唯一索引
唯一索引列的值必须唯一，但允许有空值。如果是组合索引，则列值的组合必须唯一。
**创建唯一索引:**

```
ALTER TABLE table_name ADD UNIQUE (column);
```
示例：

```sql
mysql> alter table user add unique(name);
Query OK, 0 rows affected (0.01 sec)
Records: 0  Duplicates: 0  Warnings: 0
mysql> SHOW INDEX FROM user;
+-------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table | Non_unique | Key_name | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment |
+-------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| user  |          0 | PRIMARY  |            1 | id          | A         |           0 | NULL     | NULL   |      | BTREE      |         |               |
| user  |          0 | name     |            1 | name        | A         |           0 | NULL     | NULL   |      | BTREE      |         |               |
+-------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
2 rows in set (0.03 sec)
```
**创建唯一组合索引：**

```
ALTER TABLE table_name ADD UNIQUE (column1,column2);
```
**示例：**

```sql
mysql> ALTER TABLE user ADD UNIQUE unique_name_age (name,age);
Query OK, 0 rows affected (0.01 sec)
Records: 0  Duplicates: 0  Warnings: 0
mysql> SHOW INDEX FROM user;
+-------+------------+-----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table | Non_unique | Key_name        | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment |
+-------+------------+-----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| user  |          0 | PRIMARY         |            1 | id          | A         |           0 | NULL     | NULL   |      | BTREE      |         |               |
| user  |          0 | name            |            1 | name        | A         |           0 | NULL     | NULL   |      | BTREE      |         |               |
| user  |          0 | unique_name_age |            1 | name        | A         |           0 | NULL     | NULL   |      | BTREE      |         |               |
| user  |          0 | unique_name_age |            2 | age         | A         |           0 | NULL     | NULL   |      | BTREE      |         |               |
+-------+------------+-----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
4 rows in set (0.03 sec)
```
## 4.3.普通索引
最基本的索引，它没有任何限制。

**创建普通索引：**

```
ALTER TABLE table_name ADD INDEX index_name (column);
```
**示例：**

```sql
mysql> alter table user add index index_name(name);
Query OK, 0 rows affected (0.01 sec)
Records: 0  Duplicates: 0  Warnings: 0
mysql> SHOW INDEX FROM user;
+-------+------------+-----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table | Non_unique | Key_name        | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment |
+-------+------------+-----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| user  |          0 | PRIMARY         |            1 | id          | A         |           0 | NULL     | NULL   |      | BTREE      |         |               |
| user  |          0 | name            |            1 | name        | A         |           0 | NULL     | NULL   |      | BTREE      |         |               |
| user  |          0 | unique_name_age |            1 | name        | A         |           0 | NULL     | NULL   |      | BTREE      |         |               |
| user  |          0 | unique_name_age |            2 | age         | A         |           0 | NULL     | NULL   |      | BTREE      |         |               |
| user  |          1 | index_name      |            1 | name        | A         |           0 | NULL     | NULL   |      | BTREE      |         |               |
+-------+------------+-----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
5 rows in set (0.03 sec)
```
## 4.4.组合索引
组合索引，即一个索引包含多个列。多用于避免回表查询。
**创建组合索引：**

```
ALTER TABLE table_name ADD INDEX index_name(column1, column2, column3);
```
示例：

```sql
mysql> alter table user add index index_name_age(name,age);
Query OK, 0 rows affected (0.01 sec)
Records: 0  Duplicates: 0  Warnings: 0
mysql> SHOW INDEX FROM user;
+-------+------------+-----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table | Non_unique | Key_name        | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment |
+-------+------------+-----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| user  |          0 | PRIMARY         |            1 | id          | A         |           0 | NULL     | NULL   |      | BTREE      |         |               |
| user  |          0 | name            |            1 | name        | A         |           0 | NULL     | NULL   |      | BTREE      |         |               |
| user  |          0 | unique_name_age |            1 | name        | A         |           0 | NULL     | NULL   |      | BTREE      |         |               |
| user  |          0 | unique_name_age |            2 | age         | A         |           0 | NULL     | NULL   |      | BTREE      |         |               |
| user  |          1 | index_name      |            1 | name        | A         |           0 | NULL     | NULL   |      | BTREE      |         |               |
| user  |          1 | index_name_age  |            1 | name        | A         |           0 | NULL     | NULL   |      | BTREE      |         |               |
| user  |          1 | index_name_age  |            2 | age         | A         |           0 | NULL     | NULL   |      | BTREE      |         |               |
+-------+------------+-----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
7 rows in set (0.05 sec)
```
## 4.5.全文索引
全文索引（也称全文检索）是目前搜索引擎使用的一种关键技术。
**创建全文索引**

```
ALTER TABLE table_name ADD FULLTEXT (column);
```
**示例：**

```sql
mysql> ALTER TABLE user ADD FULLTEXT (remark);
Database changed
Records: 0  Duplicates: 0  Warnings: 0
mysql> SHOW INDEX FROM user;
+-------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table | Non_unique | Key_name | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment |
+-------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| user  |          0 | PRIMARY  |            1 | id          | A         |           0 | NULL     | NULL   |      | BTREE      |         |               |
| user  |          1 | remark   |            1 | remark      | NULL      | NULL        | NULL     | NULL   | YES  | FULLTEXT   |         |               |
+-------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
2 rows in set
```
>备注:  如果是InnoDB，改为MyISAM，InnoDB不支持FULLTEXT类型的索引
# 5.删除索引
索引一经创建不能修改，如果要修改索引，只能删除重建。
删除索引：

```
DROP INDEX index_name ON table_name;
```
# 6.索引设计的原则

1.适合索引的列是出现在where子句中的列，或者连接子句中指定的列
2.基数较小的类，索引效果较差，没有必要在此列建立索引。数据库的数据量小，那么没有必要加索引！
3.使用短索引，如果对长字符串列进行索引，应该指定一个前缀长度，这样能够节省大量索引空间

    CREATE INDEX indexName ON mytable(username(length)); 
    如果是CHAR，VARCHAR类型，length可以小于字段实际长度；如果是BLOB和TEXT类型，必须指定 length。

4.不要过度索引。索引需要额外的磁盘空间，并降低写操作的性能。在修改表内容的时候，索引会进行更新甚至重构，索引列越多，这个时间就会越长。所以只保持需要的索引有利于查询即可。