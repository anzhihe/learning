
def heap_sort(array=[]):
    # 1.把无序数组构建成最大堆
    for i in range((len(array)-2)//2, -1, -1):
        down_adjust(i, len(array), array)
    # 2.循环交换集合尾部元素到堆顶，并调节堆产生新的堆顶
    for i in range(len(array)-1, 0, -1):
        # 最后一个元素和第一元素进行交换
        temp = array[i]
        array[i] = array[0]
        array[0] = temp
        # 下沉调整最大堆
        down_adjust(0, i, array)


def down_adjust(parent_index, length, array=[]):
    # temp保存父节点值，用于最后的赋值
    temp = array[parent_index]
    child_index = 2 * parent_index + 1
    while child_index < length:
        # 如果有右孩子，且右孩子大于左孩子的值，则定位到右孩子
        if child_index+1 < length and array[child_index+1] > array[child_index]:
            child_index += 1
        # 如果父节点大于等于任何一个孩子的值，直接跳出
        if temp >= array[child_index]:
            break
        # 无需真正交换，单向赋值即可
        array[parent_index] = array[child_index]
        parent_index = child_index
        child_index = 2 * child_index + 1
    array[parent_index] = temp


my_array = list([3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11])
heap_sort(my_array)
print(my_array)

