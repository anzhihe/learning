import pathlib 

file_name = "e.txt"

# 取得脚本所在目录
current_path = pathlib.PurePath(__file__).parent

# 和脚本同目录下的文件绝对路径
file = current_path.joinpath(file_name)

with open(file, encoding='utf8') as f:

    content = f.read()
    words = content.rstrip()
    number = len(words)
    print(number)
    # 15
    