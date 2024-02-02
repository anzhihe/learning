import pathlib 
import re

keyword = "apple"

# 获取索引文件路径
current_path = pathlib.PurePath(__file__).parent
dbfile = current_path.joinpath("search.db")

# 在索引文件中搜索关键字
with open(dbfile, encoding='utf-8') as f:
    for line in f.readlines():
        if re.search(keyword, line):
            print(line.rstrip())
