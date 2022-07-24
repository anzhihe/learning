### 连接

我们现在进行多个表一起查询，也就是我们说的连接查询。连接分为以下几种。

- 内连接

```
select * from tbl_students inner join tbl_classes on tbl_students.cls_id = tbl_classes.id;
```

![](https://tva1.sinaimg.cn/large/00831rSTly1gdb2yzew85j30vm0bo767.jpg)

简写

```
select * from tbl_students as s inner join tbl_classes as c on s.cls_id = c.id
```

只显示学生的所有信息，班级只显示名字

```sql
select s.*,c.name from tbl_students as s inner join tbl_classes as c on s.cls_id = c.id;
```

![](https://tva1.sinaimg.cn/large/00831rSTly1gdb32yp1dsj30vg0bm407.jpg)

根据年龄倒序排列

```sql
select s.*,c.name from tbl_students as s inner join tbl_classes as c on s.cls_id = c.id order by s.age desc;
```

![](https://tva1.sinaimg.cn/large/00831rSTly1gdb3625szwj30vm0bmmyy.jpg)

- 左连接

```sql
select s.*,c.name from tbl_students as s left join tbl_classes as c on s.cls_id = c.id;
```

![](https://tva1.sinaimg.cn/large/00831rSTly1gdb37l516ej30vk0e6mz2.jpg)

查询没有班级的学生

```
select s.*,c.name from tbl_students as s left join tbl_classes as c on s.cls_id = c.id having c.name is null;
```

![](https://tva1.sinaimg.cn/large/00831rSTly1gdb3f9jtkuj30vg09a0ty.jpg)

- 右连接

```
insert into tbl_classes values (0,"精英10班");
insert into tbl_classes values (0,"精英11班");
insert into tbl_classes values (0,"精英12班");
```

```sql
select s.*,c.name from tbl_students as s right join tbl_classes as c on s.cls_id = c.id;
```

![](https://tva1.sinaimg.cn/large/00831rSTly1gdb3cr2qbkj30vq0ek40s.jpg)





