
def bubble_sort_v1(array=[]):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp


def bubble_sort_v2(array=[]):
    for i in range(len(array)-1):
        # 有序标记，每一轮的初始是true
        is_sorted = True
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                # 有元素交换，所以不是有序，标记变为false
                is_sorted = False
        if is_sorted:
            break


def bubble_sort_v3(array=[]):
    # 记录最后一次交换的位置
    last_exchange_index = 0
    # 无序数列的边界，每次比较只需要比到这里为止
    sort_border = len(array)-1
    for i in range(len(array)-1):
        # 有序标记，每一轮的初始是true
        is_sorted = True
        for j in range(sort_border):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                # 有元素交换，所以不是有序，标记变为false
                is_sorted = False
                # 把无序数列的边界更新为最后一次交换元素的位置
                last_exchange_index = j
        sort_border = last_exchange_index
        if is_sorted:
            break


my_array = list([3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11])
bubble_sort_v3(my_array)
print(my_array)

