### Pymsql



- 安装

```
pip install pymysql
```



```python
import pymysql

# 连接数据库
db = pymysql.connect(host="localhost", user="root",
                     password="123456", db="db_test", port=3306)

# 获取游标
cur = db.cursor()
```



### 插入

```python
def insert(sql, args):
   '''
    插入
    :param sql:
    :param args:
    :return:
    '''
    try:
        # cur.executemany(sql, args)
        cur.execute(sql, args)
        # 提交
        db.commit()
    except Exception as e:
        print(e)
        # 错误回滚
        db.rollback()
    finally:
        db.close()


sql = "insert into tbl_stu(id,name) values (%s,%s)"
insert(sql, ((0, 'A')))  # 请打开insert方法里面cur.execute(sql, args)
# insert(sql, ((0, 'A'), (0, 'B')))  # 请打开insert方法里面cur.executemany(sql, args)
```



### 查询

```python
import pymysql

# 连接数据库
db = pymysql.connect(host="localhost", user="root",
                     password="123456", db="db_test", port=3306)

# 获取游标
cur = db.cursor()

def select(sql, args=None):
    '''
    查询
    :param sql:
    :param args:
    :return:
    '''

    try:
        cur.execute(sql, args)  # 执行sql语句

        results = cur.fetchall()  # 获取查询的所有记录
        # result = cur.fetchone()  # 获取一条数据,不需要下面for循环
        for row in results:
            id = row[0]
            name = row[1]
            print(id, name)
    except Exception as e:
        raise e
    finally:
        db.close()  # 关闭连接


# sql = "select * from tbl_stu" # 查询全部

# select(sql)

sql = "select * from tbl_stu where id = %s"  # 根据条件查询

select(sql, args=(1,))  # 参数数元组或者列表

```

### 更新

```python
def update(sql, args):
   '''
    更新
    :param sql:
    :param args:
    :return:
    '''
    try:
        cur.execute(sql, args)  
        # 提交
        db.commit()
    except Exception as e:
        print(e)
        # 回滚
        db.rollback()
    finally:
        db.close()


sql = "update tbl_stu set name = %s where id = %s"
update(sql, ('小红', 4))
```

### 删除

```python
def delete(sql, args):
   '''
    删除
    :param sql:
    :param args:
    :return:
    '''
    try:
        cur.execute(sql, args)
        # 提交
        db.commit()
    except Exception as e:
        print(e)
        # 回滚
        db.rollback()
    finally:
        db.close()


sql = "delete from test_index where id = %s"
delete(sql, (9999,))
```
