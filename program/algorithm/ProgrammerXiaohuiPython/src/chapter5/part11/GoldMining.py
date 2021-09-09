def get_best_gold_mining(w, n, p=[], g=[]):
    """
    :param w: 工人数量
    :param n: 可选金矿数量
    :param p: 金矿开采所需工人数量
    :param g: 金矿储量
    :return: 最优收益
    """
    if w == 0 or n == 0:
        return 0
    if w < p[n-1]:
        return get_best_gold_mining(w, n-1, p, g)
    return max(get_best_gold_mining(w, n-1, p, g), get_best_gold_mining(w - p[n-1], n-1, p, g) + g[n-1])


def get_best_gold_mining_v2(w, p=[], g=[]):
    """
    :param w: 工人数量
    :param p: 金矿开采所需工人数量
    :param g: 金矿储量
    :return: 最优收益
    """
    result_table = [[0 for i in range(w+1)] for i in range(len(g)+1)]
    # 填充表格
    for i in range(1, len(g)+1):
        for j in range(1, w+1):
            if j < p[i-1]:
                result_table[i][j] = result_table[i-1][j]
            else:
                result_table[i][j] = max(result_table[i-1][j], result_table[i-1][j-p[i-1]]+ g[i-1])
    # 返回最后一个格子的值
    return result_table[len(g)][w]


def get_best_gold_mining_v3(w, p=[], g=[]):
    """
    :param w: 工人数量
    :param p: 金矿开采所需工人数量
    :param g: 金矿储量
    :return: 最优收益
    """
    # 创建当前结果
    results = [0]*(w+1)
    # 填充一维数组
    for i in range(1, len(g)+1):
        for j in range(w, 0, -1):
            if j >= p[i-1]:
                results[j] = max(results[j], results[j-p[i-1]] + g[i-1])
    # 返回最后一个格子的值
    return results[w]


test_w = 10
test_p = list([5, 5, 3, 4, 3])
test_g = list({400, 500, 200, 300, 350})
print("最优收益：", get_best_gold_mining_v2(test_w, test_p, test_g))

