def big_number_sum(big_number_a, big_number_b):
    # 把两个大整数用数组逆序存储，数组长度等于较大整数位数 + 1
    max_length = len(big_number_a) if len(big_number_a)> len(big_number_b) else len(big_number_b)
    big_number_a = big_number_a.zfill(max_length)
    big_number_b = big_number_b.zfill(max_length)
    array_a = list(big_number_a)
    array_b = list(big_number_b)
    # 2.构建result数组，数组长度等于较大整数位数 + 1
    result = [0] * (max_length + 1)
    # 3.遍历数组，按位相加
    for i in range(max_length-1, -1, -1):
        temp = result[i+1]
        temp += int(array_a[i])
        temp += int(array_b[i])
        # 判断是否进位
        if temp >= 10:
            temp = temp-10
            result[i] = 1
        result[i+1] = temp
    if result[0] == 0:
        result.pop(0)
    # 4.把result数组转成String
    result = [str(i) for i in result]
    result_str = "".join(result)
    return result_str


print(big_number_sum("426709752318", "95481253129"))

