
from setuptools import setup, find_packages

setup(
    # 发布到PyPI后的package name
    name='my_python_lib',
    # 版本号
    version='0.1',
    # 描述
    description='My Python Lib',
    # 如果要发布的项目包含包，既可以手动指定要包含的包，也可以调用函数find_packages，例如：
    # packages=find_packages()
    # 如果要发布的项目只包含模块，那就指定py_modules这个关键字参数
    py_modules=['my_module']
)