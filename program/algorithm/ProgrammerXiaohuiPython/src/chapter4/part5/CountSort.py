
def count_sort(array=[]):
    # 1.得到数列的最大值
    max_value = array[0]
    for i in range(1, len(array)):
        if array[i] > max_value:
            max_value = array[i]
    # 2.根据数列最大值确定统计数组的长度
    count_array = [0] * (max_value+1)
    # 3.遍历数列，填充统计数组
    for i in range(0, len(array)):
        count_array[array[i]] += 1
    # 4.遍历统计数组，输出结果
    sorted_array = []
    for i in range(0, len(count_array)):
        for j in range(0, count_array[i]):
            sorted_array.append(i)
    return sorted_array


def count_sort_v2(array=[]):
    # 1.得到数列的最大值最小值，并算出差值d
    max_value = array[0]
    min_value = array[0]
    for i in range(1, len(array)):
        if array[i] > max_value:
            max_value = array[i]
        if array[i] < min_value:
            min_value = array[i]
    d = max_value - min_value
    # 2.创建统计数组并统计对应元素个数
    count_array = [0] * (d+1)
    for i in range(0, len(array)):
        count_array[array[i]-min_value] += 1
    # 3.统计数组做变形，后面的元素等于前面的元素之和
    for i in range(1, len(count_array)):
        count_array[i] += count_array[i-1]
    # 4.倒序遍历原始数列，从统计数组找到正确位置，输出到结果数组
    sorted_array = [0] * len(array)
    for i in range(len(array)-1, -1, -1):
        sorted_array[count_array[array[i]-min_value]-1] = array[i]
        count_array[array[i] - min_value] -= 1
    return sorted_array


my_array = list([4, 4, 6, 5, 3, 2, 8, 1, 7, 5, 6, 0, 10])
print(count_sort(my_array))
my_array = list([95, 94, 91, 120, 90, 99, 93, 91, 92])
print(count_sort_v2(my_array))

