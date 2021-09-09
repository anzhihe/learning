class Bucket:
    def __init__(self):
        self.min = None
        self.max = None


def get_max_sorted_distance(array=[]):
    # 1.得到数列的最大值和最小值
    max_value = array[0]
    min_value = array[0]
    for i in range(1, len(array)):
        if array[i] > max_value:
            max_value = array[i]
        if array[i] < min_value:
            min_value = array[i]
    d = max_value - min_value
    # 如果max和min相等，说明数组所有元素都相等，返回0
    if d == 0:
        return 0
    # 2.初始化桶
    bucket_num = len(array)
    buckets = []
    for i in range(0, bucket_num):
        buckets.append(Bucket())
    # 3.遍历原始数组，确定每个桶的最大最小值
    for i in range(0, len(array)):
        # 确定数组元素所归属的桶下标
        index = int((array[i] - min_value) * (bucket_num-1) / d)
        if buckets[index].min is None or buckets[index].min > array[i]:
            buckets[index].min = array[i]
        if buckets[index].max is None or buckets[index].max < array[i]:
            buckets[index].max = array[i]
    # 4.遍历桶，找到最大差值
    left_max = buckets[0].max
    max_distance = 0
    for i in range(1, len(buckets)):
        if buckets[i].min is None:
            continue
        if buckets[i].min - left_max > max_distance:
            max_distance = buckets[i].min - left_max
        left_max = buckets[i].max
    return max_distance


my_array = list([2, 6, 3, 4, 5, 10, 9])
print(get_max_sorted_distance(my_array))
