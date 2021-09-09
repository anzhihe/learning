
def cock_tail__sort(array=[]):
    for i in range(len(array) // 2):
        # 有序标记，每一轮的初始是true
        is_sorted = True
        # 奇数轮，从左向右比较和交换
        for j in range(i, len(array)-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                # 有元素交换，所以不是有序，标记变为false
                is_sorted = False
        if is_sorted:
            break
        # 偶数轮之前，重新标记为true
        is_sorted = True
        # 偶数轮，从右向左比较和交换
        for j in range(len(array)-i-1, i, -1):
            if array[j] < array[j-1]:
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp
                # 有元素交换，所以不是有序，标记变为false
                is_sorted = False
        if is_sorted:
            break


my_array = list([3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11])
cock_tail__sort(my_array)
print(my_array)

