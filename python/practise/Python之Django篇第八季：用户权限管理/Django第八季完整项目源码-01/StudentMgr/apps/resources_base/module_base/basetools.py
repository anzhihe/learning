"""
本模块实现一些常见的功能：加密
"""
# ===== 导入加密模块=====
import hashlib
# ==== 导入settings ===
from django.conf import settings


def md5(str):
    """实现字符串的加密"""
    # 实例化一个hashlib对象
    hash_object = hashlib.md5(settings.SECRET_KEY.encode("utf-8"))
    # 使用hashlid对象加密字符串
    hash_object.update(str.encode("utf-8"))
    # 返回密文
    return hash_object.hexdigest()