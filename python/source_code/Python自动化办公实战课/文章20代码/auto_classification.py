import os
import shutil
from queue import Queue

# 建立新的目录
def make_new_dir(dir, type_dir):
    for td in type_dir:
        new_td = os.path.join(dir, td)
        if not os.path.isdir(new_td):
            os.makedirs(new_td)

# 遍历目录并存入队列
def write_to_q(path_to_write, q: Queue):
    for full_path, dirs, files in os.walk(path_to_write):
        # 如果目录下没有文件，就跳过该目录
        if not files:
            continue
        else:
            q.put(f"{full_path}::{files}")

# 移动文件到新的目录
def move_to_newdir(filename_withext, file_in_path, type_to_newpath):
    # 取得文件的扩展名
    filename_withext = filename_withext.strip(" \'")
    ext = filename_withext.split(".")[1]

    for new_path in type_to_newpath:
        if ext in type_to_newpath[new_path]:
            oldfile = os.path.join(file_in_path, filename_withext)
            newfile = os.path.join(source_dir, new_path, filename_withext)
            shutil.move(oldfile, newfile)

# 将队列的文件名分类并写入新的文件夹
def classify_from_q(q: Queue, type_to_classify):
    while not q.empty():
        item = q.get()

        # 将路径和文件分开
        filepath, files = item.split("::")

        files = files.strip("[]").split(",")
        # 对每个文件进行处理
        for filename in files:
            # 将文件移动到新的目录
            move_to_newdir(filename, filepath, type_to_classify)


if __name__ == "__main__":
    # 定义要对哪个目录进行文件扩展名分类
    source_dir = "/Users/edz/Desktop/files"

    # 定义文件类型和它的扩展名
    file_type = {
        "music": ("mp3", "wav"),
        "movie": ("mp4", "rmvb", "rm", "avi"),
        "execute": ("exe", "bat")
    }

    # 建立新的文件夹
    make_new_dir(source_dir, file_type)

    # 定义一个用于记录扩展名放在指定目录的队列
    filename_q = Queue()

    # 遍历目录并存入队列
    write_to_q(source_dir, filename_q)

    # 将队列的文件名分类并写入新的文件夹
    classify_from_q(filename_q, file_type)
