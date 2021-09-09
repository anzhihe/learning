def get_greatest_common_divisor(a, b):
    big = max(a, b)
    small = min(a, b)
    if big % small == 0:
        return small
    for i in range(small//2, 1, -1):
        if small % i == 0 and big % i == 0:
            return i
    return 1


def get_greatest_common_divisor_v2(a, b):
    big = max(a, b)
    small = min(a, b)
    if big % small == 0:
        return small
    return get_greatest_common_divisor_v2(big % small, small)


def get_greatest_common_divisor_v3(a, b):
    if a == b:
        return a
    big = max(a, b)
    small = min(a, b)
    return get_greatest_common_divisor_v2(big-small, small)


def get_greatest_common_divisor_v4(a, b):
    if a == b:
        return a
    if (a & 1) == 0 and (b & 1) == 0:
        return get_greatest_common_divisor_v4(a >> 1, b >> 1) << 1
    elif (a & 1) == 0 and (b & 1) != 0:
        return get_greatest_common_divisor_v4(a >> 1, b)
    elif (a & 1) != 0 and (b & 1) == 0:
        return get_greatest_common_divisor_v4(a, b >> 1)
    else:
        big = max(a, b)
        small = min(a, b)
        return get_greatest_common_divisor_v4(big - small, small)


print(get_greatest_common_divisor(25, 5))
print(get_greatest_common_divisor_v2(100, 75))
print(get_greatest_common_divisor_v3(99, 55))
print(get_greatest_common_divisor_v4(100, 80))
