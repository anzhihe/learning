### 聚合

聚合就是对一组数据进行统计

#### count

查询总数

```
select count(*) from users;
```

![](https://tva1.sinaimg.cn/large/00831rSTly1gd33iwlne8j31y00cigmq.jpg)

#### max

查询最大值

```
select max(age) from users;
```

![](https://tva1.sinaimg.cn/large/00831rSTly1gd33jpkwp1j31y60cgt9v.jpg)



#### min

查询最小值

```
select min(age) from users;
```

![](https://tva1.sinaimg.cn/large/00831rSTly1gd33m5tonpj31z20ccjsj.jpg)



#### sum

求和

```
select sum(age) from users;
```

![](https://tva1.sinaimg.cn/large/00831rSTly1gd33mrbl1oj31z20cqdh1.jpg)

#### avg

平均数

```
select avg(age) from users;
```

![](https://tva1.sinaimg.cn/large/00831rSTly1gd3474ddm5j31z20cqdh1.jpg)