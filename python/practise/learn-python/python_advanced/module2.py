#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    module2.py
 @Function:    python模块使用
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/18
"""


"""一、使用当前项目中的模块"""

"""
如果想要使用当前项目中的模块，必须通过import语句进行导入。有三种导入方式：
1. 直接导入
2. 绝对导入
3. 相对导入
"""

"""
1. 直接导入
    直接导入当前目录中的模块名
    
2. 绝对导入
    导入模块名的绝对路径
    
3. 相对导入
    导入模块名的相对路径。其中，一个.表示当前目录，两个..表示当前目录的父目录
    当直接运行某个模块时，该模块就变成了主模块。主模块位于最顶层，与同目录下的其它模块无法构成相对关系
    因此，当直接运行某个模块时，该模块不能使用相对导入
"""


"""二、导入的不同模块中存在相同的属性"""

"""
当导入的不同模块中存在相同的属性时，比如：当导入的两个模块moda和modb中存在同名的变量v时，

1、错误的导入方式：
    from modb import v
    from moda import v
    后面的导入的属性会把前面导入的属性覆盖掉
    
2、两种正确的导入方式：
    (1) 给导入的属性起一个别名
        from moda import v as va
        from modb import v as vb
    (2) 导入整个模块
        import moda
        import modb
"""


"""三、import语句的执行流程"""

"""
    当使用import语句导入模块时，解释器会根据sys模块的modules属性来查找模块是否已经被导入了
"""

import pprint, sys
pprint.pprint(sys.modules)

"""
1. 如果模块已经被导入了，解释器什么也不做
2. 如果模块没有被导入
    (1) 解释器按照某种路径搜索模块
    (2) 将搜索到的模块编译为pyc字节码文件(可选)
    (3) 执行编译生成的字节码文件从而运行模块
"""


"""四、解释器搜索模块的路径"""

"""
当使用import语句导入模块时，如果模块还没有被导入，首先，解释器会按照某种路径搜索模块
1、解释器搜索模块的示例
"""

# import my_module
# my_module.f()   # f被调用

"""
2、解释器搜索模块的路径
    解释器搜索模块的路径存放在模块sys的变量path中
    
    在交互式命令行中执行：
    >>> import sys
    >>> sys.path
    ['', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python36.zip',  
    '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6',
    '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynLoad',  
    '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages']
    
    搜索路径主要由三部分组成：
    (1) 当前目录
    (2) 标准库的目录
    (3) 第三方库的安装目录
"""

"""
3、修改解释器搜索模块的路径
    第一种方式：直接修改sys.path
        根据上述打印结果可知：sys.path是一个列表
        可以在代码运行时直接修改sys.path以修改搜索路径，但是在代码运行后修改会失效
"""

import sys
sys.path.insert(0, '/Users/zhangrongchao/Downloads')

"""
    把my_module.py拷贝到目录/Users/zhangrongchao/Downloads，并做如下修改：
    def f():
        print('f被调用(Downloads目录)')
"""

import my_module
my_module.f()   # f被调用(Downloads目录)

"""
    在交互式命令行中执行：
    >>> import sys
    >>> sys.path 
    搜索路径不变
"""

"""
    第二种方式：设置环境变量PYTHONPATH以修改sys.path
        环境变量PYTHONPATH对应的路径会被自动添加到sys.path中
        修改后的搜索路径在代码运行后仍然有效
"""