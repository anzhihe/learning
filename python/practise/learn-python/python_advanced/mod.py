
v = 56

print('模块的特殊属性__name__的值：', __name__)

"""
以下是测试代码
"""
def add_num(num1, num2):
    return num1 + num2

# 根据__name__的值判断是否执行模块中的测试代码
if __name__ == '__main__':
    print('1 + 2 =', add_num(1, 2))
    print('3 + 5 =', add_num(3, 5))