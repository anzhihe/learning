"""
本模块提供了上传文件的模块化（图片，视频，文本，excel）
提供的参数：
1. 要写入的文件
2. 路径 （提供子目录） --- images
3. 名称的命名
   1 ---- 日期 + 时间 + 4位随机值  18位！
   2 ---- uuid

返回值：
  1. 成功
    {'status': True, 'data': 文件名 }
  2. 失败
    {'status': True, 'error': 失败的原因 }
"""
# 导入模块
from resources_base.module_base.importmodules import *


def upload_file(file, path: str, type: int):
    """
    提供文件的上传
    :param file: 要上传的文件
    :param path: 提供的路径
    :param type: 随机命名的方式  1-- 时间日期随机值  2-- uuid
    :return:
    """
    # 定义返回的数据结构
    res = {'status': True}
    # 定义新文件名称
    new_name = ""
    # 获取新文件的名称
    if type == 1:
        new_name = get_file_name_random_date()
    elif type == 2:
        new_name = uuid.uuid4().hex
    # 拼接路径
    file_name = settings.MEDIA_ROOT + os.path.sep + path + os.path.sep + new_name + os.path.splitext(file.name)[1]
    # 开始写入
    try:
        # === 1. 写入文件 ====
        f = open(file_name, 'wb')
        # 分多次写入
        for i in file.chunks():
            f.write(i)
        # 关闭
        f.close()

        # 提供写入的文件名
        res['data'] = new_name + os.path.splitext(file.name)[1]
    except Exception as e:
        res['status'] = False
        res['error'] = "文件写入磁盘出现异常，具体原因" + str(e)

    return res


def get_file_name_random_date():
    """根据日期获取随机值"""
    filename = datetime.now().strftime("%Y-%m-%d").replace("-", "")
    filename += str(random.randint(1000, 9999))
    return filename
