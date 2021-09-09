def is_power_of_2(num):
    temp = 1
    while temp <= num:
        if temp == num:
            return True
        temp = temp * 2
    return False


def is_power_of_2_v2(num):
    temp = 1
    while temp <= num:
        if temp == num:
            return True
        temp = temp << 1
    return False


def is_power_of_2_v3(num):
    return (num & num-1) == 0


print(is_power_of_2_v3(19))
print(is_power_of_2_v3(32))
