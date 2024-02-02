import sqlite3
import pathlib

class OptSqlite(object):
    def __init__(self, dbname = "contacts.db"):
        """
        :param dbname  数据库名称
        """
        self.dir = pathlib.PurePath(__file__).parent
        self.db = pathlib.PurePath(self.dir, dbname)
        self.conn = sqlite3.connect(self.db)
        self.cur = self.conn.cursor()

    def close(self):
        """
        关闭连接
        """
        self.cur.close()
        self.conn.close()

    def get_one_phone(self, username):
        """
        获取一个联系人的电话
        """

        self.get_user_phone_sql = f"""
            SELECT phone FROM address_book WHERE name = "{username}" """
        try:
            self.result = self.cur.execute(self.get_user_phone_sql)
            return self.result.fetchone()
        except Exception as e:
            print(f"失败原因是：{e}")

    def set_one_phone(self, name, phone):
        """
        增加一个联系人
        """
        self.set_user_phone_sql = '''INSERT INTO address_book
          VALUES (?, ?, ?)'''
        self.v =  (2, str(name), int(phone))
        try:
            self.cur.execute(self.set_user_phone_sql, self.v)
            self.conn.commit()
        except Exception as e:
            print(f"失败原因是：{e}")


if __name__ == "__main__":

    my_query = OptSqlite("contacts.db")
    
    my_query.set_one_phone("Jerry","12344445555")
    
    phone = my_query.get_one_phone("Tom")
    phone2 = my_query.get_one_phone("Jerry")    
    
    my_query.close()

    print(phone)
    print(phone2)