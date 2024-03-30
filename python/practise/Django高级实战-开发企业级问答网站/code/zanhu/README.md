> 注意命令的执行用户，[root@zanhu ~]#表示root用户，[zanhu@zanhu ~]$表示zanhu用户

## 一、ECS+RDS初始化配置

### 1.1 云服务器ECS配置

先准备好服务器，内存至少2G，在阿里云购买`抢占式实例`，2vCPU 2G不到一毛钱一小时。

![](https://liaogx-public-img.oss-cn-shanghai.aliyuncs.com/imooc/zanhu_ecs.png)

### 1.2 云数据库RDS MySQL版配置

将ECS的内网IP加入白名单

![](https://liaogx-public-img.oss-cn-shanghai.aliyuncs.com/imooc/zanhu_rds_settings01.png)

ECS和RDS要在**同一个地区**，通过内网地址连接

![](https://liaogx-public-img.oss-cn-shanghai.aliyuncs.com/imooc/zanhu_rds_settings02.png)

创建数据库`zanhu`

![](https://liaogx-public-img.oss-cn-shanghai.aliyuncs.com/imooc/zanhu_mysql.png)

创建**普通账号**`zanhu`，赋予`zanhu`数据库**读写权限**

![](https://liaogx-public-img.oss-cn-shanghai.aliyuncs.com/imooc/zanhu_mysql_user.png)

后面生成数据表之后，可以登录数据库看看，连接地址为<u>内网地址</u>：

`zanhu-MySQL - rm-8vbol04k8sn31e7zy43490.mysql.zhangbei.rds.aliyuncs.com:3306`

跳转到该页面会帮你自动填写好的，DMS是阿里云的另外一个产品。

![](https://liaogx-public-img.oss-cn-shanghai.aliyuncs.com/imooc/zanhu_dms.png)

## 二、CentOS 7初始化配置

### 2.1 创建组和用户

```shell
[root@zanhu ~]# groupadd zanhu
[root@zanhu ~]# useradd -m zanhu -g zanhu
[root@zanhu ~]# passwd zanhu
```

zanhu家目录赋予执行权限，非常重要！！！

```shell
[zanhu@zanhu ~]$ chmod +x /home/zanhu/
```

### 2.2 安装系统依赖

有Python, MySQL的依赖，Elasticsearch对Java依赖，django-compressor的压缩需要的bizp2-devel等

```shell
[root@zanhu ~]# yum -y update
[root@zanhu ~]# yum -y install python-devel zlib-devel mysql-devel libffi-devel bzip2-devel openssl-devel java wget gcc
```

### 2.3 安装git/redis/nginx/supervisor

后面要用的一次装好

```shell
[root@zanhu ~]# yum -y  install git redis nginx supervisor
```

### 2.3 设置开机启动

保证实例重启后服务依然运行

```shell
[root@zanhu ~]# systemctl enable redis nginx supervisord
Created symlink from /etc/systemd/system/multi-user.target.wants/redis.service to /usr/lib/systemd/system/redis.service.
Created symlink from /etc/systemd/system/multi-user.target.wants/nginx.service to /usr/lib/systemd/system/nginx.service.
Created symlink from /etc/systemd/system/multi-user.target.wants/supervisord.service to /usr/lib/systemd/system/supervisord.service.
[root@zanhu ~]#
```

## 三、安装Python3

### 3.1 六条命令一梭哈

一条条来不容易出问题，阿里云的服务器下载`Python-3.7.2.tar.xz`很慢，可以先浏览器下载了再传到服务器上，后面下载`elasticsearch-2.4.6.tar.gz`也是一样。

```shell
[root@zanhu ~]# wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tar.xz
[root@zanhu ~]# tar -xvf Python-3.7.2.tar.xz
[root@zanhu ~]# cd Python-3.7.2
[root@zanhu ~]# ./configure --prefix=/usr/local/python3 --enable-optimizations
[root@zanhu ~]# make
[root@zanhu ~]# make install
```

* 注：加上`--enable-optimizations`后make的过程巨慢，但系统在执行Python代码时会有10%-20%的性能提升，参考 [what does --enable-optimizations do while compiling python?](https://stackoverflow.com/questions/41405728/what-does-enable-optimizations-do-while-compiling-python)

### 3.2 创建软链接

```shell
[root@zanhu ~]# ln -s /usr/local/python3/bin/python3 /usr/bin/python3
[root@zanhu ~]# ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
```

### 3.3 验证安装结果

```shell
[root@zanhu ~]# python3 -V
Python 3.7.2
[root@zanhu ~]# pip3 -V
pip 18.1 from /usr/local/python3/lib/python3.7/site-packages/pip (python 3.7)
[root@zanhu ~]# whereis python3
python3: /usr/bin/python3 /usr/local/python3
[root@zanhu ~]# whereis pip3
pip3: /usr/bin/pip3
[root@zanhu ~]#
```

## 四、安装Elasticsearch

切换到zanhu用户，elasticsearch服务不能使用root用户运行

```shell
[zanhu@zanhu ~]$ wget https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/2.4.6/elasticsearch-2.4.6.tar.gz
[zanhu@zanhu ~]$ tar -xvf elasticsearch-2.4.6.tar.gz
```

## 五、项目发布

### 5.1 上传代码

从慕课的仓库`clone`过来，大家可以上传自己的代码

```shell
[zanhu@zanhu ~]$ git clone https://git.imooc.com/coding-333/zanhu.git  # 是zanhu用户
```

创建logs文件夹，用于存放`uwsgi`, `daphne`等服务生成的日志

```shell
[zanhu@zanhu ~]$ cd zanhu
[zanhu@zanhu zanhu]$ mkdir logs
```

### 5.2 安装项目需要的包

部署到生产环境的时候，因为就一个项目在服务器上，就使用真实的Python3环境，**不需要pipenv了**

使用`root`安装，其它用户权限不够，`requirements.txt`文件如下，生产环境需要的包

```shell
python-slugify==3.0.1
redis==3.2.1
celery==4.3.0rc3
django-celery-email==2.0.1
daphne==2.2.5
django==2.1.7
django-redis==4.10.0
django-allauth==0.39.1
django-environ==0.4.5
django-crispy-forms==1.7.2
django-compressor==2.2
mysqlclient==1.4.2.post1
django-contrib-comments==1.9.1
django-markdownx==2.0.28
channels==2.1.7
sorl-thumbnail==12.5.0
django-taggit==1.1.0
channels-redis==2.3.3
awesome-slugify==1.6.5
argon2-cffi==19.1.0
pillow==5.4.1
python3-openid==3.1.0
requests-oauthlib==1.2.0
requests==2.21.0
django-haystack==2.8.1
elasticsearch==2.4.1
uwsgi==2.0.18
```

安装，root用户的pip源会自动使用阿里云，飞快

```shell
[root@zanhu ~]# pip3 install -r /home/zanhu/zanhu/requirements.txt
[root@zanhu ~]# pip3 install --upgrade pip  # 总有个版本提示很让人纠结，更新一下
```

### 5.3 生成数据表

回到`zanhu`用户，migrate一下

```shell
[zanhu@zanhu zanhu]$ pwd
/home/zanhu/zanhu
[zanhu@zanhu zanhu]$ python3 manage.py makemigrations
[zanhu@zanhu zanhu]$ python3 manage.py migrate
......
```

### 5.4 collect静态文件

```shell
[zanhu@zanhu zanhu]$ python3 manage.py collectstatic

99 static files copied to '/home/zanhu/zanhu/zanhu/static'.
[zanhu@zanhu zanhu]$
```

### 5.5 压缩静态文件

```shell
[zanhu@zanhu zanhu]$ python3 manage.py compress --force  # 其实不用手动执行，会随着客户端请求响应自动生成到STATIC/CACHE目录下
......
Compressing... done
Compressed 13 block(s) from 60 template(s) for 1 context(s).
[zanhu@zanhu zanhu]$
```

### 5.6 添加GitHub的client_id和secret

这步别忘了，不然网站无法使用GitHub注册。先插入`socialaccount_socialapp`，点击`SQL操作数据`，`新建`

![](https://liaogx-public-img.oss-cn-shanghai.aliyuncs.com/imooc/socialaccount_socialapp.png)

`socialaccount_socialapp_sites`表也是一样，填好数据之后`提交修改`

![](https://liaogx-public-img.oss-cn-shanghai.aliyuncs.com/imooc/socialaccount_socialapp_sites.png)

对应的，这是我GitHub上`OAuth Apps`认证的设置

![img](https://liaogx-public-img.oss-cn-shanghai.aliyuncs.com/imooc/zanhu_oauth_github_explanation.png)

## 六、nginx+uwsgi+daphne+supervisor配置

### 6.1 nginx配置

下面是nginx的配置，`/etc/nginx/nginx.conf`

```shell
# For more information on configuration, see:
#   * Official English Documentation: http://nginx.org/en/docs/
#   * Official Russian Documentation: http://nginx.org/ru/docs/

user nginx;
worker_processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;

# Load dynamic modules. See /usr/share/nginx/README.dynamic.
include /usr/share/nginx/modules/*.conf;

events {
    worker_connections 1024;
}

http {
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile            on;
    tcp_nopush          on;
    tcp_nodelay         on;
    keepalive_timeout   65;
    types_hash_max_size 2048;

    include             /etc/nginx/mime.types;
    default_type        application/octet-stream;

    # Load modular configuration files from the /etc/nginx/conf.d directory.
    # See http://nginx.org/en/docs/ngx_core_module.html#include
    # for more information.
    include /etc/nginx/conf.d/*.conf;

    upstream uwsgi_backend {  # http请求转发配置
        server localhost:8888;
    }

    upstream channels-backend {  # websocket请求转发配置
        server localhost:8000;
    }

    server {
        listen       80 default_server;
        listen       [::]:80 default_server;
        server_name  _;
        root         /usr/share/nginx/html;

        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

        location / {
            proxy_http_version 1.1;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

            uwsgi_pass  uwsgi_backend;
            include uwsgi_params;
        }

        location /static/ {
            root  /home/zanhu/zanhu/zanhu;  # static文件所在的目录路径
        }

        location /media/ {
            root   /home/zanhu/zanhu/zanhu;  # media文件所在的目录路径
        }

        location /ws/ {  # /ws/用于区分http请求和websocket
            proxy_pass http://channels-backend;

            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            proxy_redirect off;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Host $server_name;
        }

        error_page 404 /404.html;
            location = /40x.html {
        }

        error_page 500 502 503 504 /50x.html;
            location = /50x.html {
        }
    }
}
```

### 6.2 uwsgi配置

下面是uwsgi的配置，放在`/etc/uwsgi.ini`

```shell
[uwsgi]
# Django manage.py 所在文件夹路径
chdir = /home/zanhu/zanhu
module = config.wsgi:application
# 启用master进程管理
master = true
# 绑定的 UNIX socket
socket = 127.0.0.1:8888
# uwsgi的进程数
processes = 1
# 最大请求处理数，之后重新生成进程
max-requests = 5000
# 退出时清理环境
vacuum = true
# python的安裝路径
home = /usr/local/python3/
```

### 6.3 supervisor管理uwsgi进程

`zanhu_uwsgi.ini`文件，放在`/etc/supervisord.d/`目录下，使用supervisor管理uwsgi进程

```shell
[program:uwsgi]
# 执行用户
user = zanhu
# 在该目录下执行下面command命令
directory = /home/zanhu/zanhu
# 执行的命令
command = /usr/local/python3/bin/uwsgi --ini /etc/uwsgi.ini
# 日志文件配置
loglevel = info
stdout_logfile = /home/zanhu/zanhu/logs/uwsgi.log
stderr_logfile = /home/zanhu/zanhu/logs/uwsgi_error.log
stdout_logfile_maxbytes = 100MB
stdout_logfile_backups = 3
# 给每个进程命名，便于管理
process_name = uwsgi_worker%(process_num)s
# 启动的进程数，设置成云服务器的vCPU数
numprocs_start = 1
numprocs = 1
max-requests = 5000
# 设置自启和重启
autostart = true
autorestart = true
redirect_stderr = True
```

### 6.4 supervisor管理daphne进程

daphne的配置，supervisor通过读取`zanhu_daphne.ini`的配置，管理daphne进程

```shell
[program:daphne]
# 执行用户
user = zanhu
# 在该目录下执行下面command命令
directory = /home/zanhu/zanhu
# 执行的命令
command = /usr/local/python3/bin/daphne -p 8000 config.asgi:application
# 日志文件配置
loglevel = info
stdout_logfile = /home/zanhu/zanhu/logs/daphne.log
stderr_logfile = /home/zanhu/zanhu/logs/daphne_error.log
stdout_logfile_maxbytes = 100MB
stdout_logfile_backups = 3
# 给每个进程命名，便于管理
process_name = daphne_worker%(process_num)s
# 启动的进程数，设置成云服务器的vCPU数
numprocs_start = 1
numprocs = 1
max-requests = 5000
# 设置自启和重启
autostart = true
autorestart = true
redirect_stderr = True
```

### 6.5 supervisor管理celery进程

`zanhu_celery.ini`文件，放在`/etc/supervisord.d/`目录下，使用supervisor管理celery进程

```shell
[program:celery]
# 执行用户
user = zanhu
# 执行的命令
command = /usr/local/python3/bin/celery --workdir=/home/zanhu/zanhu -A zanhu.taskapp worker -l info
# 日志文件配置
loglevel = info
stdout_logfile = /home/zanhu/zanhu/logs/celery.log
stderr_logfile = /home/zanhu/zanhu/logs/celery_error.log
stdout_logfile_maxbytes = 100MB
stdout_logfile_backups = 3
# 给每个进程命名，便于管理
process_name = celery_worker%(process_num)s
# 启动的进程数，设置成云服务器的vCPU数
numprocs_start = 1
numprocs = 1
# 设置自启和重启
autostart = true
autorestart = true
redirect_stderr = True
```

### 6.6 supervisor管理elasticsearch进程

`zanhu_elasticsearch.ini`文件，放在`/etc/supervisord.d/`目录下，使用supervisor管理elasticsearch进程

```shell
[program:elasticsearch]
# 执行用户
user = zanhu
# 在该目录下执行下面command命令
directory = /home/zanhu/elasticsearch-2.4.6/bin/
# 执行的命令
command = /home/zanhu/elasticsearch-2.4.6/bin/elasticsearch -d
# 日志文件配置
loglevel = info
stdout_logfile = /home/zanhu/zanhu/logs/elasticsearch.log
stderr_logfile = /home/zanhu/zanhu/logs/elasticsearch_error.log
stdout_logfile_maxbytes = 100MB
stdout_logfile_backups = 3
# 给每个进程命名，便于管理
process_name = elasticsearch_worker%(process_num)s
# 启动的进程数，设置成云服务器的vCPU数
numprocs_start = 1
numprocs = 1
# 设置自启和重启
autostart = true
autorestart = true
redirect_stderr = True
```

## 七、启动服务并检查日志

### 7.1 启动nginx和redis

```shell
[root@zanhu ~]# cd /home/zanhu/zanhu/deploy/nginx+uwsgi+daphne+supervisor
[root@zanhu nginx+uwsgi+daphne+supervisor]# cp nginx.conf /etc/nginx/nginx.conf
[root@zanhu ~]# systemctl start nginx
[root@zanhu ~]# systemctl start redis
```

### 7.2 启动supervisord

也就是启动了uwsgi, daphe, celery, elasticsearch服务

```shell
[root@zanhu ~]# cd /home/zanhu/zanhu/deploy/nginx+uwsgi+daphne+supervisor
[root@zanhu nginx+uwsgi+daphne+supervisor]# cp uwsgi.service /etc/systemd/system/
[root@zanhu nginx+uwsgi+daphne+supervisor]# cp zanhu_* /etc/supervisord.d/  # y确定
[root@zanhu nginx+uwsgi+daphne+supervisor]# systemctl start supervisord
[root@zanhu nginx+uwsgi+daphne+supervisor]# supervisorctl update
[root@zanhu nginx+uwsgi+daphne+supervisor]# supervisorctl reload
```

查看所有的python3进程，可以看到uwsgi, daphe, celery进程都有了

```shell
[zanhu@zanhu ~]$ ps -ef | grep python3
zanhu    10324 10047  2 16:51 ?        00:00:01 /usr/local/python3/bin/python3.7 /usr/local/python3/bin/celery --workdir=/home/zanhu/zanhu -A zanhu.taskapp worker -l info
zanhu    10325 10047  2 16:51 ?        00:00:01 /usr/local/python3/bin/python3.7 /usr/local/python3/bin/daphne -p 8000 config.asgi:application
zanhu    10327 10047  1 16:51 ?        00:00:00 /usr/local/python3/bin/uwsgi --ini /etc/uwsgi.ini
zanhu    10364 10327  0 16:51 ?        00:00:00 /usr/local/python3/bin/uwsgi --ini /etc/uwsgi.ini
zanhu    10365 10324  0 16:51 ?        00:00:00 /usr/local/python3/bin/python3.7 /usr/local/python3/bin/celery --workdir=/home/zanhu/zanhu -A zanhu.taskapp worker -l info
zanhu    10366 10324  0 16:51 ?        00:00:00 /usr/local/python3/bin/python3.7 /usr/local/python3/bin/celery --workdir=/home/zanhu/zanhu -A zanhu.taskapp worker -l info
zanhu    10367 10324  0 16:51 ?        00:00:00 /usr/local/python3/bin/python3.7 /usr/local/python3/bin/celery --workdir=/home/zanhu/zanhu -A zanhu.taskapp worker -l info
zanhu    10368 10324  0 16:51 ?        00:00:00 /usr/local/python3/bin/python3.7 /usr/local/python3/bin/celery --workdir=/home/zanhu/zanhu -A zanhu.taskapp worker -l info
zanhu    10712  3625  0 16:52 pts/1    00:00:00 grep --color=auto python3
[zanhu@zanhu ~]$
```

验证`elasticsearch`服务启动结果

```shell
[zanhu@zanhu ~]$ curl http://localhost:9200
{
  "name" : "Chase Stein",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "UtXbk8tSSeakhjLEOMwP9A",
  "version" : {
    "number" : "2.4.6",
    "build_hash" : "5376dca9f70f3abef96a77f4bb22720ace8240fd",
    "build_timestamp" : "2017-07-18T12:17:44Z",
    "build_snapshot" : false,
    "lucene_version" : "5.5.4"
  },
  "tagline" : "You Know, for Search"
}
[zanhu@zanhu ~]$
```

### 7.3 检查日志

- 分别检查`uwsgi.log  elasticsearch.log  celery.log  daphne.log`是否启动成功，有没有报错

```sh
[zanhu@zanhu ~]$ tail -5  zanhu/logs/daphne.log
127.0.0.1:42906 - - [07/Apr/2019:00:31:28] "WSDISCONNECT /ws/notifications/" - -
127.0.0.1:42912 - - [07/Apr/2019:00:31:39] "WSCONNECTING /ws/notifications/" - -
127.0.0.1:42912 - - [07/Apr/2019:00:31:39] "WSREJECT /ws/notifications/" - -
127.0.0.1:42912 - - [07/Apr/2019:00:31:39] "WSDISCONNECT /ws/notifications/" - -
127.0.0.1:42918 - - [07/Apr/2019:00:31:50] "WSCONNECTING /ws/notifications/" - -
[root@zanhu ~]# tail -5  zanhu/logs/elasticsearch.log
[root@zanhu ~]# tail -5  zanhu/logs/celery.log
[root@zanhu ~]# tail -5  zanhu/logs/uwsgi.log
```

- `nginx access.log`，root用户才有权限查看，下同。

```shell
[root@zanhu ~]# tail -5 /var/log/nginx/access.log
180.164.101.207 - - [07/Apr/2019:00:41:32 +0800] "GET /static/CACHE/css/bootstrap.min.css.map HTTP/1.1" 404 3043 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36" "-"
180.164.101.207 - - [07/Apr/2019:00:41:32 +0800] "GET /static/fonts/font-awesome-4.7.0/fonts/fontawesome-webfont.woff2?v=4.7.0&b3114982de95 HTTP/1.1" 200 77160 "http://39.98.252.127/static/CACHE/css/7be88d97718d.css" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36" "-"
180.164.101.207 - - [07/Apr/2019:00:41:32 +0800] "GET /static/CACHE/js/8b4fbd1ef7c0.js HTTP/1.1" 200 423351 "http://39.98.252.127/messages/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36" "-"
180.164.101.207 - - [07/Apr/2019:00:41:33 +0800] "GET /notifications/latest-notifications/?_=1554568893315 HTTP/1.1" 200 94 "http://39.98.252.127/messages/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36" "-"
180.164.101.207 - - [07/Apr/2019:00:41:33 +0800] "GET /static/img/favicon.png HTTP/1.1" 200 17052 "http://39.98.252.127/messages/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36" "-"
[root@zanhu ~]#

```

- `nginx error.log`，没有报错，爽！

```shell
[root@zanhu ~]# tail -5 /var/log/nginx/error.log
```

- `supervisor.log`，root用户才有权限查看

```shell
[root@zanhu ~]# tail -10 /var/log/supervisor/supervisord.log
2019-04-06 23:24:18,396 INFO success: asgi_worker0 entered RUNNING state, process has stayed up for > than 1 seconds (startsecs)
2019-04-06 23:24:29,561 INFO waiting for asgi_worker0 to die
2019-04-06 23:24:29,725 INFO stopped: asgi_worker0 (exit status 0)
2019-04-06 23:24:29,729 CRIT Supervisor running as root (no user in config file)
2019-04-06 23:24:29,729 WARN Included extra file "/etc/supervisord.d/zanhu_daphne.ini" during parsing
2019-04-06 23:24:29,730 INFO RPC interface 'supervisor' initialized
2019-04-06 23:24:29,730 CRIT Server 'unix_http_server' running without any HTTP authentication checking
2019-04-06 23:24:29,730 INFO supervisord started with pid 30359
2019-04-06 23:24:30,732 INFO spawned: 'asgi_worker0' with pid 30365
2019-04-06 23:24:32,371 INFO success: asgi_worker0 entered RUNNING state, process has stayed up for > than 1 seconds (startsecs)
[root@zanhu ~]#
```

有提示`CRIT Server 'unix_http_server' running without any HTTP authentication checking`，可以在`/etc/supervisord.conf`中给`unix_http_server`设置用户名和密码，就这样也没事。

## 八、赢取白富美，出任CTO...

走上人生巅峰之前，有个小坑要注意一下，我用Google云的VM实例的时候，发现部署完了一直是静态文件403，文件夹和文件都有权限，而且用阿里云没有问题

```shell
[zanhu@zanhu ~]$ sudo setenforce 0  # Google云实例上关闭SElinux
```

完。
