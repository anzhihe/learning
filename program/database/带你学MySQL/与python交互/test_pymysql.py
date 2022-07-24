import pymysql

# 连接操作
db = pymysql.connect(host='localhost', user='root',
                     password='123456', port=3306, db='db_test')

# 获取游标

cur = db.cursor()


def insert(sql, args):
    '''
    插入
    :param sql:
    :param args:
    :return:
    '''
    try:
        # cur.execute(sql, args)  # 执行

        cur.executemany(sql, args)

        # 提交
        db.commit()

    except Exception as e:
        print(e)

        # 回滚
        db.rollback()
    finally:
        db.close()


sql = "insert into tbl_stu(id,name) values (%s,%s)"


# insert(sql, (0, '老王'))

# insert(sql, ((0, '老赵'), (0, '老宋')))


def select(sql, args=None):
    try:
        cur.execute(sql, args)

        # result = cur.fetchall()

        result1 = cur.fetchone()

        print(result1)

        # for res in result:
        #     id = res[0]
        #     name = res[1]
        #     print(id, name)


    except Exception as e:
        print(e)

    finally:
        db.close()


# sql = 'select * from tbl_stu'
# select(sql)

sql = 'select * from tbl_stu where id= %s'


# select(sql, args=(1,))


def update(sql, args):
    try:
        cur.execute(sql, args)
        db.commit()

    except Exception as e:
        print(e)
        db.rollback()

    finally:
        db.close()


sql = 'update tbl_stu set name=%s where id = %s '


# update(sql, ('小红', 1))


def delete(sql, args):
    try:
        cur.execute(sql, args)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    finally:
        db.close()


sql = 'delete from  test_index where id = %s'

delete(sql, (9999,))
