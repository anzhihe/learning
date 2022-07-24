### 外键

两个表之间一定是通过某种介质联系，这个介质就是外键。所以外键是建立表之间的联系的必须的前提。外键也是一种约束。我们目前知道的约束有

![](https://tva1.sinaimg.cn/large/00831rSTly1gdb3j4rogyj31as0hm40c.jpg)

创建外键有两种方式。



- 创建表的时候

```sql
create table tbl_students (
	
	id int not null primary key auto_increment,

	name varchar(50) not null,

	gender varchar(1) not null,

	age int(11) not null,
  
  cls_id int(11),
  
	constraint stu_cls foreign key(cls_id) references tbl_classes(id)
	
)engine = innodb default charset=utf8;
```

- 更新成外键

```
alter table tbl_students add constraint stu_cls foreign key(cls_id) references tbl_classes(id);
```

![](https://tva1.sinaimg.cn/large/00831rSTly1gdb3nc94y6j30vk04ygmw.jpg)

因为这里面有两个没有班级的数据，因为连接不到数据，所以不让创建外键。也就是外键的值一定能在某个表中查到数据。

```
delete from tbl_students where id > 5;
```

![](https://tva1.sinaimg.cn/large/00831rSTly1gdb3p1sxqmj30vc072gmr.jpg)

### 注意事项

因为我们现在的表已经有关系了，所以当我们删除一条数据的时候，如果这个表跟其他表有关系，删除的时候就会报错。

- restrict（限制）：默认值，抛异常
- cascade：从主表中删除或更新对应的行，同时自动的删除或更新从表中匹配的行
- set null：从主表中删除或更新对应的行，同时将从表中的外键列设为空
- no action：拒绝删除或者更新父表

```sql
create table tbl_students (
	
	id int not null primary key auto_increment,

	name varchar(50) not null,

	gender varchar(1) not null,

	age int(11) not null,
  
  cls_id int(11),

	constraint stu_cls foreign key(cls_id) references tbl_classes(id) on delete cascade
	
)engine = innodb default charset=utf8;

```

或者

前提是没有外键，如果有请先删除

```sql
alter table tbl_students add constraint stu_cls foreign key(cls_id) references tbl_classes(id) on delete cascade;
```

> alter table tbl_students drop foreign key stu_cls;   #删除外键

如果是默认，我删除一个班级。

![](https://tva1.sinaimg.cn/large/00831rSTly1gdb3s5nns9j30vm04ywfj.jpg)

如果是cascade

![](https://tva1.sinaimg.cn/large/00831rSTly1gdb423ju9sj30vk04uwfa.jpg)

![](https://tva1.sinaimg.cn/large/00831rSTly1gdb42zgdjoj30uu0cigmv.jpg)

