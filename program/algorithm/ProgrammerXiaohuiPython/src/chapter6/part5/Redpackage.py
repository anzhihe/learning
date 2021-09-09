import random


def divide_red_package(total_amount, total_people_num):
    amount_list = []
    rest_amount = total_amount
    rest_people_num = total_people_num
    for i in range(0, total_people_num-1):
        # 随机范围：[1，剩余人均金额的两倍)，左闭右开
        amount = random.randint(1, int(rest_amount/rest_people_num*2)-1)
        rest_amount -= amount
        rest_people_num -= 1
        amount_list.append(amount)
    amount_list.append(rest_amount)
    return amount_list


my_amount_list = divide_red_package(1000, 10)
for my_amount in my_amount_list:
    print("抢到金额：%.2f" % (my_amount/100))
