### Windows安装

```
https://dev.mysql.com/downloads/mysql/
```

![](https://tva1.sinaimg.cn/large/0082zybply1gc2zpraxfgj31st0u0thy.jpg)

![](https://tva1.sinaimg.cn/large/0082zybply1gc2zq7oahsj31sx0u044w.jpg)

### windows安装

- 下载

  ```
  https://cdn.mysql.com//Downloads/MySQL-5.7/mysql-5.7.30-winx64.zip
  ```

  

- 环境变量

  ![](https://tva1.sinaimg.cn/large/007S8ZIlly1genronqt3rj30af089dgr.jpg)

  ![](https://tva1.sinaimg.cn/large/007S8ZIlly1genrp3p23tj30k40gedgy.jpg)

  ![](https://tva1.sinaimg.cn/large/007S8ZIlly1genrpe5eqlj30ue0hj408.jpg)

  > 注意：一定要是自己的mysql路径

![](https://tva1.sinaimg.cn/large/007S8ZIlly1genrt5sjxqj30qd0i8q4f.jpg)



- 打开CMD

![](https://tva1.sinaimg.cn/large/007S8ZIlly1genrsehuscj30ah0h3glp.jpg)



> 注意：最好右键以管理员方式打开



-  进入bin目录

![](https://tva1.sinaimg.cn/large/007S8ZIlly1genrtqntxjj30rq03adfs.jpg)

> 注意：一定要是自己的mysql路径

- 生成data文件夹

```
mysqld --initialize-insecure --user=mysql 
```

![](https://tva1.sinaimg.cn/large/007S8ZIlly1genruj9cqkj311d01cmx0.jpg)

- 安装mysql

```
mysqld -install
```

![](https://tva1.sinaimg.cn/large/007S8ZIlly1genrvhlzlbj30t501umx0.jpg)

- 启动服务

```
net start MySQL
```

![](https://tva1.sinaimg.cn/large/007S8ZIlly1genrvumjh5j30yj01zjr9.jpg)

- 登录mysql

```
mysql -uroot -p
```

> 注意：直接回车即可，不需要输入密码

![](https://tva1.sinaimg.cn/large/007S8ZIlly1genrx8htquj30t206ujrk.jpg)



- 更新密码

```
select host,user,authentication_string from mysql.user;
```

```
use mysql; 
```

```
update mysql.user set authentication_string=password("123456") where user="root";
```

```
flush privileges; 
```

![](https://tva1.sinaimg.cn/large/007S8ZIlly1genrxkd9rwj30qr08m0sy.jpg)

- 退出

```
quit或者ctrl+c
```

- 以后就用密码登录了

![](https://tva1.sinaimg.cn/large/007S8ZIlly1gens0hcg8bj30jw072mxa.jpg)

### Linux安装

- 安装

```
sudo apt-get install mysql-server mysql-client
```

> 注意：安装的过程会让你输入密码

- 启动

```
service mysql start
```

- 关闭

```
service mysql stop
```

- 重启

```
service mysql restart
```

### Mac安装

- 下载

```
https://dev.mysql.com/downloads/mysql/
```

- 安装

![](https://tva1.sinaimg.cn/large/007S8ZIlly1genshrlk6vj316k0oaab6.jpg)

> 注意：可能出现安全验证，打开苹果设置，安全与隐私，选择仍要打开就行

![](https://tva1.sinaimg.cn/large/007S8ZIlly1geocjlfqd4j30ya0o4goo.jpg)

![](https://tva1.sinaimg.cn/large/007S8ZIlly1gensjoxdunj30ww0mqguy.jpg)

- 打开终端

  ```
  vim ~/.bash_profile
  ```

  在bash_profile文件中加入下面配置

  ```
  PATH=$PATH:/usr/local/mysql/bin
  ```

  保存并退出（多按 几下Esc键，然后输入  :wq  之后按回车）,退出后，在执行下面命令

  ```
  source ~/.bash_profile 
  ```



- 登录

  ```
  mysql -uroot -p
  ```

  ![](https://tva1.sinaimg.cn/large/007S8ZIlly1gensn2q07fj30vg0e2wg9.jpg)

  > 注意：输入上面复制的初识密码

  

- 修改密码

登录成功后直接输入下面命令

```
SET PASSWORD FOR 'root'@'localhost' = PASSWORD('123456');
```

```
flush privileges; 
```

退出quit，以后就可以用新密码登录了。



### 忘记密码

- 查看服务

```
net start
```

![](https://tva1.sinaimg.cn/large/007S8ZIlly1gent4tqbsej30mf0fgt95.jpg)

- 停止服务

```
net stop MySQL
```

![](https://tva1.sinaimg.cn/large/007S8ZIlly1gent5h2cdcj30ki02f3yc.jpg)

- 输入下面命令

```
mysqld --skip-grant-tables
```

![](https://tva1.sinaimg.cn/large/007S8ZIlly1gent6mni1nj30jv01wt8i.jpg)

会出现等待状态，然后重新开个终端

- 修改密码

  新打开一个终端

![](https://tva1.sinaimg.cn/large/007S8ZIlly1gent7re48oj31cy0awjtq.jpg)

```
use mysql; 
```

```
update mysql.user set authentication_string=password("1234567") where user="root";
```

```
flush privileges; 
```

![](https://tva1.sinaimg.cn/large/007S8ZIlly1gent8538ejj30qr04bq2w.jpg)



- 重启服务

![](https://tva1.sinaimg.cn/large/007S8ZIlly1geocioouj9j30q802a3yc.jpg)

### Mac

- 关闭服务

```
sudo /usr/local/mysql/support-files/mysql.server stop   # 或者可以系统偏好设置里面点击关闭也可以
```

- 进入目录

```
cd /usr/local/mysql/bin
```

- 获取权限

```
sudo su
```

- 重启服务器

```
./mysqld_safe --skip-grant-tables &
```

- 退出编辑

```
control + D
```

- 配置短命令

```
alias mysql=/usr/local/mysql/bin/mysql
```

- 进入命令模式

```
mysql
```

- 使用数据库

```
use mysql
```

- 获取更改权限

```
flush privileges;
```

- 重置密码

```
set password for 'root'@'localhost'=password('123456');
```

