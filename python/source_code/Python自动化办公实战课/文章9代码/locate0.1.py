from pathlib import Path

base_dir = '/Users/edz/Desktop/'
keywords = '**/*BBC*'

# 遍历base_dir指向的目录下所有的文件
p = Path(base_dir)

# 当前目录下包含BBC的所有文件名称
files = p.glob(keywords)  
# files的类型是迭代器
# 通过list()函数转换为列表输出
# print(list(files))

# xlsx结尾的文件
files2 = p.rglob('*.xlsx')
print(list(files2))


# 遍历子目录和所有文件
files3 = p.glob('**/*')
print(list(files3))
