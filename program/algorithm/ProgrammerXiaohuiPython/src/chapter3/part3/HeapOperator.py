
def up_adjust(array=[]):
    """
    二叉堆的尾节点上浮操作
    :param array: 原数组
    """
    child_index = len(array) - 1
    parent_index = (child_index - 1) // 2
    # temp保存插入的叶子节点值，用于最后的赋值
    temp = array[child_index]
    while child_index > 0 and temp < array[parent_index]:
        # 无需真正交换，单向赋值即可
        array[child_index] = array[parent_index]
        child_index = parent_index
        parent_index = (parent_index - 1) // 2
    array[child_index] = temp


def down_adjust(parent_index, length, array=[]):
    """
    二叉堆的节点下沉操作
    :param parent_index: 待下沉的节点下标
    :param length: 堆的长度范围
    :param array: 原数组
    """
    # temp保存父节点值，用于最后的赋值
    temp = array[parent_index]
    child_index = 2 * parent_index + 1
    while child_index < length:
        # 如果有右孩子，且右孩子小于左孩子的值，则定位到右孩子
        if child_index + 1 < length and array[child_index + 1] < array[child_index]:
            child_index += 1
        # 如果父节点小于任何一个孩子的值，直接跳出
        if temp <= array[child_index]:
            break
        # 无需真正交换，单向赋值即可
        array[parent_index] = array[child_index]
        parent_index = child_index
        child_index = 2 * child_index + 1
    array[parent_index] = temp


def build_heap(array=[]):
    """
    二叉堆的构建操作
    :param array: 原数组
    """
    # 从最后一个非叶子节点开始，依次下沉调整
    for i in range((len(array)-2) // 2, -1, -1):
        down_adjust(i, len(array), array)


my_array = list([1, 3, 2, 6, 5, 7, 8, 9, 10, 0])
up_adjust(my_array)
print(my_array)
my_array = list([7, 1, 3, 10, 5, 2, 8, 9, 6])
build_heap(my_array)
print(my_array)
