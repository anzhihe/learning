import xlrd
from pathlib import Path, PurePath
from collections import defaultdict
from collections import Counter

# 订单路径
download_path = '/Users/edz/Desktop/效率专栏/新年特辑/订单'

# 取得该目录下所有的xlsx格式文件
p = Path(download_path)
files = [x for x in p.iterdir() if PurePath(x).match('*.xlsx')]

# 定义字典用于结果统计
total = defaultdict(int)

# 中文做字典的key会有问题,做两个简单的翻译函数
tran_dict =  {
    "dragon_fruit":"火龙果",
    "coconut":"椰子",
    "watermelon":"西瓜"
}
# 中文翻译成英文
def dict_trans_chi2eng(value):
    return [k for k,v in tran_dict.items() if v == value]

# 英文翻译成中文
def dict_name_eng2chi(key):
    return tran_dict[key]



# 遍历文件 
for file in files:
    sheet = xlrd.open_workbook(file)

    # 遍历表格
    for table in  sheet.sheets():
        # 从第二行遍历内容
        for line in range(1,table.nrows):
            fruit = table.row_values(rowx=line, start_colx=0, end_colx=None)

            # 统计每种水果的销售额           
            fruit_name = dict_trans_chi2eng(fruit[0])[0]
            total[fruit_name] = total[fruit_name] + fruit[-2]

    # 每张表格是一个月份,进行一次月份统计之后,将临时统计清零
    # 用每个excel的文件名区分月份
    print(f"月份为: {file.stem} 本月水果销量 Top3为:")

    # 排序并取出Top3
    # 通过sort函数排序取出Top3也可以实现
    #  这里我直接使用Counter函数
    sorted_total = Counter(total)

    # 清空本月统计数据
    total = defaultdict(int)

    print(sorted_total.most_common(3))
