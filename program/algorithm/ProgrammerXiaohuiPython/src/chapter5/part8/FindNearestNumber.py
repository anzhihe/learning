def find_nearest_number(numbers=[]):
    # 1.从后向前查看逆序区域，找到逆序区域的前一位，也就是数字置换的边界
    index = find_transfer_point(numbers)
    # 如果数字置换边界是0，说明整个数组已经逆序，无法得到更大的相同数字组成的整数，返回null
    if index == 0:
        return None
    # 2.把逆序区域的前一位和逆序区域中刚刚大于它的数字交换位置
    # 拷贝入参，避免直接修改入参
    numbers_copy = numbers.copy()
    exchange_head(index, numbers_copy)
    # 3.把原来的逆序区域转为顺序
    reverse(index, numbers_copy)
    return numbers_copy


def find_transfer_point(numbers=[]):
    for i in range(len(numbers)-1, 0, -1):
        if numbers[i] > numbers[i-1]:
            return i
    return 0


def exchange_head(index, numbers=[]):
    head = numbers[index-1]
    for i in range(len(numbers)-1, 0, -1):
        if head < numbers[i]:
            numbers[index-1] = numbers[i]
            numbers[i] = head
            break
    return numbers


def reverse(index, numbers=[]):
    i = index
    j = len(numbers)-1
    while i < j:
        temp = numbers[i]
        numbers[i] = numbers[j]
        numbers[j] = temp
        i += 1
        j -= 1
    return numbers


def output_numbers(numbers=[]):
    for i in numbers:
        print(i, end='')
    print()


my_numbers = list([1, 2, 3, 4, 5])
# 打印12345之后的10个全排列整数
for k in range(0, 10):
    my_numbers = find_nearest_number(my_numbers)
    output_numbers(my_numbers)


