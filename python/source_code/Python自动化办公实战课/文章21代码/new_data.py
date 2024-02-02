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
sql1 = '''INSERT INTO address_book
          VALUES (?, ?, ?)'''
v =  (1, "Tom", 12377778888)

# 执行SQL
try:
    cur.execute(sql1, v)
    conn.commit()

except Exception as e:
    print(f"失败原因是：{e}")

finally:
    # 关闭游标
    cur.close()
    # 关闭连接
    conn.close()
