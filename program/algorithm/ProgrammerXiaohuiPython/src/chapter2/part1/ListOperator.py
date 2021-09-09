

def operate_list():
    # 初始化列表
    my_list = [3, 1, 2, 5, 4, 9, 7, 2]

    # 读取元素
    print(my_list[2])

    # 更新元素
    my_list[3] = 10
    print(my_list[3])

    # 尾部插入元素
    my_list.append(6)
    print(my_list)

    # 中间插入元素
    my_list.insert(5, 11)
    print(my_list)

    # 删除元素
    my_list.remove(6)
    print(my_list)


operate_list()
