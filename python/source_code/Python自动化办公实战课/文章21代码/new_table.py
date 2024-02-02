import sqlite3
import pathlib

# 数据库文件的路径和文件名称
dir = pathlib.PurePath(__file__).parent
db = pathlib.PurePath(dir, "contents.db")

# 创建连接
conn = sqlite3.connect(db)

# 创建游标
cur = conn.cursor()

# 定义要执行的SQL语句
sql = '''CREATE TABLE address_book(
        id INT PRIMARY KEY NOT NULL,
        name TEXT NOT NULL,
        phone INT NOT NULL
       )'''

# 执行SQL
try:
    cur.execute(sql)
    print("创建成功")
except Exception as e:
    print("创建失败")
    print(f"失败原因是：{e}")
finally:
    # 关闭游标
    cur.close()
    # 关闭连接
    conn.close()
