#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    third_party_module.py
 @Function:    python使用第三方库中的模块
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/18
"""


"""使用第三方库中的模块"""

"""
除了官方提供的标准库之外，还有非常非常多的第三方库可供我们使用，用以完成各种不同的任务。

如果想要使用第三方库中的模块，必须先使用工具（例如：pip3) 下载安装第三方库，然后通过import语句进行导入。

1、PyPI简介

    PyPI的全程是：Python Package Index，它是Python官方的、基于 Web 的、集中管理的、第三方的软件仓库
    所有人都可以从PyPI下载安装第三方库，或将自己开发的库上传发布到PyPI。
    PyPI的网址：https://pypi.org

2、从PyPI下载安装第三方库

    通常使用工具pip3从PyPI下载安装第三方库。pip的全称是：Package Installer for Python。

    安装最新版本的 Python3 之后，pip3 也被安装上了（在 Windwos 上安装 Python3 时，确保已经勾选了 pip）。
    可以通过命令验证是否已经安装了 pip3: $pip3 或$python3 -m pip

    可以通过命令查看 pip3 的安装路径
    在 Mac0S 或 Ubuntu 操作系统上，输入命令：$ which pip3
    在 Windows 操作系统上, 输入命令: > where pip3
"""

"""
3、pip3使用

    搜索要下载安装的第三方库的 package name，假设为 xxx，则对应的安装命令为： 
    pip3 install xxx 或：python3 -m pip install xxx 
    例如：pip3 install tortoise-orm

    第三方库的安装路径：
    Mac0S操作系统：
    Library/Frameworks/Python.framework/Versions/3.6/Lib/python3.6/site-packages
    Windows操作系统：
    <Python的安装路径》\Lib\site-packages

    第三方库中模块的源代码也是极好的Python学习资料。

    pip3 的相关命令：

    (1) 查看 pip3 的帮助信息：pip3
    (2) 列出已安装的所有第三方库：pip3 list
    (3) 模糊搜索某个第三方库：pip3 search xxx
    (4) 安装指定的第三方库（及其版本号）：pip3 install xxx (pip3 install xxx==y.y) 
    (5) 升级指定的第三方库：pip3 install --upgrade xxx
    (6) 卸載指定的第三方库（及其版本号）：pip3 uninstall xxx (pip3 uninstall xxx==y.y) 
    (7) 查看 pip3 之后某个命令的帮助信息:pip3 <命令> --help
"""

"""
4、导入第三库中的模块
    导入第三方库中的模块的方式与导入标准库中模块的方式是完全相同的
"""

import tortoise.fields
print(tortoise.fields.DateField)

"""
5、将自己开发的库发布到PyPI或共享给别人
    1. 创建配置文件setup.py
    在配置文件setup.py中调用模块setuptools中的函数setup，并且传递各种关键字参数。
    通过配置各种关键字参数，该位置文件会告诉系统如何打包自己开发的库。

    关于setup.py文件的配置，可以参考以下文档：
    (1) setuptools的官方文档
        https://setuptools.readthedocs.io/en/latest/index.html
    (2) Python的官方文档
        https://packaging.python.org/tutorials/packaging-projects/
    (3) Github上的sample project
        https://github.com/pypa/sampleproject

    2. 创建其它文件
        参考以上文档
        
    3. 打包自己开发的库
        将setup.py、其它文件和自己开发的库放在同一个目录中，在命令行中切换到该目录，
        然后执行命令：python3 setup.py sdist，在dist目录中生成一个source distribution(sdist)压缩文件，
        该压缩文件中包含了模块的源代码；此外，还生成了一个名为<package name>.egg-info的文件夹。

    4. 将打包的库发布到PyPI或共享给别人
        关于如何将自己开发的库发布到PyPI，可以参考Python的官方文档:
        https://packaging.python.org/tutorials/packaging-projects

        当把打包的库共享给别人后，别人就可以直接安装了。
        切换到dist目录，然后执行命令：pip3 install <dist目录中生成的压缩文件>
"""

import my_module
my_module.f()   # f被调用

