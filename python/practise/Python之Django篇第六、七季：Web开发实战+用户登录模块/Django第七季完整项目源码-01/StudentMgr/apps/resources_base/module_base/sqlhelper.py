"""
# 本模块用来和数据库的交互的标准化操作模块
功能包含：查询，添加、修改、删除、批量添加等功能
如何使用 ：
 ==================

使用范例：
========================
"""
# =========== 第一部分： 所需引入的模块 ==============
import pymysql
from django.conf import settings


# ========== 第二部分：定义全局变量 ====================


# ========== 第三部分：用户自定义的函数或者类 ================
def conn_db():
    # 定义一个返回值的结构体
    res = {}
    # 使用异常处理连接
    try:
        # 实例化一个连接对象
        conn = pymysql.connect(host=settings.DATABASES['default']['HOST'], user=settings.DATABASES['default']['USER'],
                               password=settings.DATABASES['default']['PASSWORD'],db=settings.DATABASES['default']['NAME'])

        # 添加连接的状态值
        res['status'] = True
        # 添加连接的对象
        res['conn'] = conn

    except Exception as e:
        # 添加连接的状态值
        res['status'] = False
        # 添加连接错误的信息
        res['error'] = '连接数据库出现异常！具体原因：' + str(e)

    # 返回
    return res   #


def get_db_data(sql: str):
    """
    根据提供的SQL语句，连接数据库查询，返回查询后的结果
    :param sql: 提供的SQL语句
    :return: 返回的数据
    """
    # 获取一个数据库的连接
    rec = conn_db()
    # 判断是否连接成功
    if not rec['status']:
        return rec
    # 获取一个操作数据库的指针
    cursor = rec['conn'].cursor()
    # 使用异常处理执行语句
    try:
        # 执行获取的传递的SQL语句
        cursor.execute(sql)
        # 获取返回的结果
        rec['data'] = cursor.fetchall()
        # 添加一个错误key
        rec['error'] = ""
    except Exception as e:
        # 修改执行的状态
        rec['status'] = False
        # 添加错误信息
        rec['error'] = '获取数据库数据出现异常！具体原因：' + str(e)
    # 返回
    return rec


def update_db(sql: str):
    """
    实现对数据库的修改：修改（Update、Insert、Delete）
    :param sql: 提供SQL语句
    :return: 返回执行的结果
    """
    # 获取连接数据库的对象
    rec = conn_db()
    # 判断是否连接成功
    if not rec['status']:
        return rec
    # 获取一个操作数据库的指针
    cursor = rec['conn'].cursor()
    # 使用异常处理执行SQL语句并提交到数据库
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 把修改提交到数据库
        rec['conn'].commit()
        # 添加一个错误key
        rec['error'] = ""
    except Exception as e:
        # 修改执行的状态
        rec['status'] = False
        # 回滚操作
        rec['conn'].rollback()
        # 修改数据库的错误信息题库
        rec['error'] = "修改数据库出现异常！具体原因：" + str(e)
    # 返回
    return rec


def bluk_insert(sql:str, data: list):
    """
    批量插入数据
    :param sql: SQL语句的模板
    :param data: 提供的数据集合
    :return: 返回结果
    """
 # 获取连接数据库的对象
    rec = conn_db()
    # 判断是否连接成功
    if not rec['status']:
        return rec
    # 获取一个操作数据库的指针
    cursor = rec['conn'].cursor()
    # 使用异常处理执行SQL语句并提交到数据库
    try:
        # 执行SQL语句
        cursor.executemany(sql, data)
        # 把修改提交到数据库
        rec['conn'].commit()
        # 添加一个错误key
        rec['error'] = ""
    except Exception as e:
        # 修改执行的状态
        rec['status'] = False
        # 回滚操作
        rec['conn'].rollback()
        # 修改数据库的错误信息题库
        rec['error'] = "修改数据库出现异常！具体原因：" + str(e)
    # 返回
    return rec


def get_db_data_dict(sql, keys: list):
    """
    获取数据，并转为Dict的格式
    :param sql: 提供的SQL语句
    :param keys: dict的key
    :return: 返回数据的格式 -- [{}，{}，{}，{}，{}，]
    """
    # 调用数据库获取数据
    response = get_db_data(sql)
    # 判断是否成功
    if not response['status']:
        return response
    # 拼接成字典
    data = []
    # 循环
    for index, value in enumerate(response['data']):
        # 定义一个dict
        temp_dict = {}
        # 遍历
        for i, v in enumerate(value):
            temp_dict[keys[i]] = v
        # 附加到集合
        data.append(temp_dict)
    # 修改携带的数据
    response['data'] = data
    # 返回
    return response


