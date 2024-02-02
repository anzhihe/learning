import os
# 保存图片的目录
file_path = "/Users/edz/Desktop/pic"
# 需要批量重命名的扩展名
old_ext = ".jpg"
# 取得指定文件夹下的文件列表
old_names = os.listdir(file_path)
# 新文件名称从1开始
new_name = 1

# 取得所有的文件名
for old_name in old_names:

    # 根据扩展名，判断文件是否需要改名
    if old_name.endswith(old_ext):

        # 完整的文件路径
        old_path = os.path.join(file_path, old_name)

        # 新的文件名
        new_path = os.path.join(file_path, str(new_name)+".txt")
       
        # 重命名
        os.rename(old_path, new_path)

        # 文件名数字加1
        new_name = int(new_name)+1

# 显示改名后的结果
print(os.listdir(file_path))

#  ['3.txt', '2.txt', '1.txt', 'xyz.bmp']