#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    python_practice2.py
 @Function:    python practice
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/6
"""


"""一、百钱买百鸡"""

"""
【问题描述】
    用100文钱买100只鸡，其中公鸡5文钱1只，母鸡3文钱1只，小鸡1文钱3只
    求各买了几只公鸡、母鸡和小鸡
    
【设计思路】
    设计思路一：
    设公鸡、母鸡和小鸡的只数分别为x、y和z，根据问题描述可以得到如下方程组：
    x + y + z = 100
    5x + 3y + z/3 = 100
    
    如果100文钱全买公鸡，最多可买100 / 5 = 20只，所以x的取值范围是：[0, 20]
    如果100文钱全买母鸡，最多可买100 / 3 = 33只，所以y的取值范围是：[0, 33]
    如果100文钱全买小鸡，最多可买100 * 3 = 300只
    因为总共买了100只鸡，且1文钱3只，所以z的取值范围是：[0, 100],并且z能被3整除
    
    通过三重循环穷举x、y和z的值
    在穷举的过程中，只要x、y和z满足上面的方程组，则得到一组符合条件的解
"""

# 通过三重循环穷举x、y和z的值
# 如果100文钱全买公鸡，最多可买100 / 5 = 20只，所以x的取值范围是：[0, 20]
for x in range(21):
    # 如果100文钱全买母鸡，最多可买100 / 3 = 33只，所以y的取值范围是：[0, 33]
    for y in range(34):
        # 如果100文钱全买小鸡，最多可买100 * 3 = 300只
        # 因为总共买了100只鸡，且1文钱3只，所以z的取值范围是：[0, 100], 并且z能被3整除
        for z in range(0, 101, 3):
            if x + y + z == 100 and 5 * x + 3 * y + z / 3 == 100:
                print('公鸡的只数：%d，母鸡的只数：%d，小鸡的只数：%d' % (x, y, z))

"""
    设计思路二：
    通过二重循环穷举x和y的值
    在穷举的过程中，求出z = 100 - x - y
    只要z满足：z >= 0 且 z能被3整除 且 5x + 3y + z/3 = 100,则得到一组符合条件的解
"""

for x in range(21):
    for y in range(34):
        z = 100 - x - y
        if z >= 0 and z % 3 == 0 and 5 * x + 3 * y + z / 3 == 100:
            print('公鸡的只数：{}，母鸡的只数：{}，小鸡的只数：{}'.format(x, y, z))


"""二、谁家孩子跑得最慢"""

"""
【问题描述】
    张家、王家和李家各有三个孩子
    一天，三家的九个孩子在一起比赛跑步，规定：
    跑第一名得9分，跑第二名得8分，跑第三名得7分，...，跑第九名得1分
    
    比赛结果如下：
    (1) 各家三个孩子的总分相同
    (2) 第一名是李家的孩子，第二名是王家的孩子
    (3) 所有孩子的名次没有并列的
    (4) 各家三个孩子的名次都没有相连的
    求最后一名是谁家的孩子
    
【设计思路】
    由1可知：
    各家三个孩子的总分都是：(1+2+3+4+5+6+7+8+9)/3=15
    
    由2可知：
    因为第1名是李家的孩子，所以可设李家孩子的分数分别为：9、x、15-(9+x)，即：9、x、6-x，其中，x的取值范围是[1, 5]
    因为第2名是王家的孩子，所以可设王家孩子的分数分别为：8、y、15-(8+y)，即：8、y、7-y，其中，y的取值范围是[1, 6]
    
    由3和4可知：
    x-(6-x)>1，y-(7-y)>1
    
    通过循环穷举李家三个孩子的分数和王家三个孩子的分数
    在穷举的过程中，定义一个列表存放所有名次对应的分数
    每穷举一次李家三个孩子的分数，就把李家三个孩子的分数从列表中删除
    每穷举一次王家三个孩子的分数，就把王家三个孩子的分数从列表中删除
    列表中剩余的元素即为张家三个孩子的分数，从大到小分别为zhang[2]、zhang[1]、zhang[0]
    因为张家三个孩子的名次没有相连的
    所以zhang[2] - zhang[1] > 1，并且zhang[1] - zhang[0] > 1 
"""

def slowest_child():
    for li in [[9, x, 6 - x] for x in range(1, 6) if x - (6 - x) > 1]:
        # 在穷举的过程中，定义一个列表存放所有名次对应的分数
        scores = list(range(1, 10))
        # 每穷举一次李家三个孩子的分数，就把李家三个孩子的分数从列表中删除
        for score in li:
            scores.remove(score)

        for wang in [[8, y, 7 -y] for y in scores if 7 -y in scores and y - (7 - y) > 1]:
            for score in wang:
                scores.remove(score)

        # 列表中剩余的元素即为张家三个孩子的分数，从大到小分别为zhang[2]、zhang[1]、zhang[0]
        zhang = scores
        # 因为张家三个孩子的名次没有相连的
        # 所以zhang[2] - zhang[1] > 1，并且zhang[1] - zhang[0] > 1
        if zhang[2] - zhang[1] > 1 and zhang[1] - zhang[0] > 1:
            print('李家三个孩子的分数：', li)
            print('王家三个孩子的分数：', wang)
            print('张家三个孩子的分数：', zhang)

slowest_child()


"""三、杨辉三角"""

"""
【问题描述】
    打印下图所示的杨辉三角：
             １
　　　　　　　１　１
　　　　　　１　２　１
　　　　　１　３　３　１
　　　　１　４　６　４　１
　　　１　５　10　10　５　１
　　１　６　15　20　15　６　１
　１　７　21　35　35　21　７　１
１　８　28　56　70　56　28　８　１
......
【设计思路】
    杨辉三角的特点：
    (1) 第i行有i个数
    (2) 每行的第一个数和最后一个数都是1
    (3) 每行除了第一个数和最后一个数，其余各数都是其两肩上的数之和

如果将所有的数存在一个二维列表L中，则有：
[[1],
 [1, 1]
 [1, 2, 1]
 [1, 3, 3, 1]
 [1, 4, 6, 4, 1]
 [1, 5, 10, 10, 5, 1]
 [1, 6, 15, 20, 15, 6, 1]
 [1, 7, 21, 35, 35, 21, 7, 1]
 [1, 8, 28, 56, 70, 56, 28, 8, 1]]
 
假设要打印n行，对于特点2，则有：
L[i][0] = L[i][i] = 1(i =  0，1，2，...，n-1)
对于特点3，则有：
当j != 0 且 j != i时，L[i][j] = L[i-1][j-1] + L[i-1][j]

首先，初始化一个所有元素都为1的n行二维列表，第i行有i个数
然后，根据上述特点3的条件和公式更新二维列表，对杨辉三角中不为1的位置进行更新
最后，根据杨辉三角的格式打印二维列表
    打印每行的内容前，先打印一定数量的水平制表符，第i行打印n-i个
    打印每行的内容时，除最后一个数之外，每打印一个数之后打印两个水平制表符
    对于每行的最后一个数，打印之后换行，准备打印下一行
"""

# 首先，初始化一个所有元素都为1的n行二维列表，第i行有i个数
L = [[1 for j in range(i + 1)] for i in range(9)]

# 然后，对杨辉三角中不为1的位置进行更新
for i in range(2, 9):
    for j in range(i + 1):
        # 每行除了第一个数和最后一个数，其余各数都是其两肩上的数之和
        if j != 0 and j != i:
            L[i][j] = L[i - 1][j - 1] + L[i - 1][j]

# 最后，根据杨辉三角的格式打印二维列表
for i in range(9):
    # 打印每行的内容前，先打印一定数量的水平制表符，第i行打印n-i个
    print('\t' * (8 - i), end = '')

    # 打印每行的内容时
    for j in range(i + 1):
        # 除最后一个数之外
        if j != i:
            # 每打印一个数之后打印两个水平制表符
            print('%d\t\t' % L[i][j], end = '')
        # 对于每行的最后一个数
        else:
            # 打印之后换行，准备打印下一行
            print('%d' % L[i][j])