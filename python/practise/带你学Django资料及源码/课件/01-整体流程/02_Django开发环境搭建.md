# 虚拟环境

在开发过程中，当需要使用python的包时可以联网安装:
```python
sudo pip3 install 包名称
```
使用如上命令，会将包安装到/usr/local/lib/python3.5/dist-packages下。

## 1. 问题
如果在一台机器上，想开发多个不同的项目，需要用到同一个包的不同版本，如果还使用上面的命令，在同一个目录下安装或者更新，其它的项目必须就无法运行了，怎么办呢？

> 解决方案: 虚拟环境

那么为什么是虚拟环境呢?

这里给大家举一个简单的例子，桌面上有一个word文件，我们打开修改这个文件，修改了一会之后发现还是原来的文件比较好，这个时候我想找回原来的文件就比较困难了。那么怎么办呢？就有这样一种解决方案，在修改文件之前，先复制一份，然后在副本文件里进行修改，这样即使发现修改有错，也不会影响原始文件。

> 虚拟环境其实就是对真实pyhton环境的复制，这样我们在复制的python环境中安装包就不会影响到真实的python环境。通过建立多个虚拟环境，在不同的虚拟环境中开发项目就实现了项目之间的隔离。


## 2. 创建
首先安装虚拟环境，命令如下:
```python
sudo pip3 install virtualenv #安装虚拟环境
```
接下来还要安装虚拟环境扩展包，命令如下：
```python
sudo pip3 install virtualenvwrapper
```
安装虚拟环境包装器的目的是使用更加简单的命令来管理虚拟环境。

修改用户家目录下的配置文件.bashrc,添加如下内容：
```python
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
```

使用source .bashrc命令使配置文件生效。

创建python3虚拟环境的命令如下：
```python
mkvirtualenv  虚拟环境名称 # mkvirtualenv -p python3 虚拟环境名字
例：
mkvirtualenv  django_1
```
如果虚拟环境没有创建成功可以升级一下pip包管理工具后重新一下虚拟环境:
```python
sudo pip3 --default-timeout=10000 install --upgrade pip
```

![虚拟环境01](![](http://tp.jikedaohang.com/20191112224407_nwd4tz_Screenshot.jpeg)

**总结**
- 创建成功后，会自动工作在这个虚拟环境上。
- 创建虚拟环境需要联网。
- 工作在虚拟环境上，提示符最前面会出现"(虚拟环境名称)"。
- 所有的虚拟环境，都位于/home/wengwenyu/下的隐藏目录.virtualenvs下。


> 特别提示:
如果在使用pip包管理工具安装包的时候出现超时有以下两种方案可以解决!

```python
# 利用清华http源安装:

pip install -i https://pypi.douban.com/simple/ 包名  

pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple +包名

#设置超时时间安装:

pip --default-timeout=100 install  包名
```

## 2. 退出
退出虚拟环境的命令如下：
```python
deactivate
```

![image-20191112224500144](/Users/xiaoyuan/Library/Application Support/typora-user-images/image-20191112224500144.png)

## 3. 查看与使用

**查看所有虚拟环境的命令如下：**

> 提示:workon后面有个空格,再按两次tab键

![image-20191112224652083](/Users/xiaoyuan/Library/Application Support/typora-user-images/image-20191112224652083.png)

**使用虚拟环境的命令如下:**
> 写出名称的前部分后,可以使用tab键补齐

```python
workon 虚拟环境名称
例:
workon django_1
```

## 4. 删除
删除虚拟环境命令如下:
```python
rmvirtualenv 虚拟环境名称
例:
先退出: deactivate 
再删除: rmvirtualenv django_1
```

## 5. 包管理
在虚拟环境中可以使用pip命令操作python包,安装命令如下:
```python
pip install 包名称
```

> 注意: 在虚拟环境中可以使用pip命令操作python包,安装命令如下:
```python
pip list
pip freeze   # 查看安装了哪些包
```
这两个命令都可以查看当前工作的虚拟环境中安装了哪些包,只是显示格式稍有不同

## 6. 安装Django包
```python
mkvirtualenv django_1
```

然后安装django的包,命令如下:
```python
pip install django
```

![image-20191112224835467](/Users/xiaoyuan/Library/Application Support/typora-user-images/image-20191112224835467.png)



> 先检查一下pip是否是虚拟环境下的pip


