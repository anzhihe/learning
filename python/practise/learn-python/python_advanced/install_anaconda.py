#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    install_anaconda.py
 @Function:    安装和配置Anaconda
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/18
"""


"""安装和配置Anaconda"""

"""
1、什么是Anaconda以及为什么要安装Anaconda？
    我们经常会用到很多Python的第三方库。
    如果使用工具pip3逐个安装，不仅费时费力，而且还要考虑兼容性。
    Anaconda是一个基于Python的数据处理和科学计算的平台，它内置了很多非常有用的第三方库。
    安装Anaconda后，相当于把大量的第三方库都自动安装好了，因此可以直接导入这些第三方库中的模块。
"""

"""
2、Anaconda的安装和配置
    官网下载地址：https://www.anaconda.com/download  
    Anaconda是跨平台的。
    
    安装程序会把Anaconda安装目录下的bin目录添加到系统环境变量PATH中，比如： 
    # added by Anaconda3 5.0.1 installer
    export PATH="/Users/zhangrongchao/anaconda3/bin:$PATH" 
    因此，安装完Anaconda后，会使用其自带的Python，从而：
    (1) 在命令行中输入的python3来自于: <Anaconda的安装目录>/bin
    (2) 使用工具pip3安装的第三方库会被安装到: <Anaconda的安装目录>/lib/python3.x/site-packages
"""

"""
3、Anaconda的第三方库管理工具conda
    Anaconda使用工具conda对第三方库进行管理，类似于工具pip3。
    
    conda的相关命令：
    (1) 查看conda的帮助信息：
        conda
    (2) 列出已安装的所有第三方库
        conda list 
    (3) 模糊搜索某个第三方库
        conda search xxx
    (4) 安装指定的第三方库（及其版本号）
        conda install xxx(conda install xxx=y.y) 
    (5) 升级指定的第三方库
        conda update xxx
    (6) 卸载指定的第三方库（及其版本号）
        conda remove xxx(conda remove xxx=y.y) 
    (7) 查看conda之后某个命令的帮助信息
        conda《命令》--help
"""

