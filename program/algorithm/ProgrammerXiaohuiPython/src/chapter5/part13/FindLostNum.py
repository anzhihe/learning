def find_lost_num(array=[]):
    # 用于存储两个出现奇数次的整数
    result = [0, 0]
    # 第一次整体异或
    xor_result = 0
    for i in range(0, len(array)):
        xor_result ^= array[i]
    # 如果异或结果为0，说明输入数组不符合题目
    if xor_result == 0:
        raise ValueError
    # 确定两个整数的不同位，以此来做分组
    separator = 1
    while 0 == (xor_result & separator):
        separator <<= 1
    # 第二次分组异或
    for i in range(0, len(array)):
        if 0 == (array[i] & separator):
            result[0] ^= array[i]
        else:
            result[1] ^= array[i]
    return result


my_array = list([4, 1, 2, 2, 5, 1, 4, 3])
print(find_lost_num(my_array))

