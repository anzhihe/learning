import sqlite3
import pathlib

class OptSqlite(object):
    def __init__(self, dbname = "new.db"):
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

    def new_table(self, table_name):
        """
        新建联系人表
        """

        sql = f'''CREATE TABLE {table_name}(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone INT NOT NULL
            )'''

        try:
            self.cur.execute(sql)
            print("创建表成功")
        except Exception as e:
            print("创建表失败")
            print(f"失败原因是：{e}")


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

    def get_all_contents(self):
        """
        取得所有的联系人
        """
        try:
            self.result = self.cur.execute("SELECT * FROM address_book")
            return self.result.fetchall()
        except Exception as e:
            print(f"失败原因是：{e}")

    def set_one_phone(self, name, phone):
        """
        增加或修改一个联系人的电话
        """
        if self.get_one_phone(name):
            self.set_user_phone_sql = '''UPDATE address_book 
            SET phone= ? WHERE name=?'''
            self.v =  (int(phone), str(name))
        else:
            self.set_user_phone_sql = '''INSERT INTO address_book
            VALUES (?, ?, ?)'''
            self.v =  (None, str(name), int(phone))
        try:
            self.cur.execute(self.set_user_phone_sql, self.v)
            self.conn.commit()
        except Exception as e:
            print(f"失败原因是：{e}")


    def delete_one_content(self, name):
        """
        删除一个联系人的电话
        """
        self.delete_user_sql = f'''DELETE FROM address_book 
                WHERE name="{name}"'''

        try:
            self.cur.execute(self.delete_user_sql)
            self.conn.commit()
        except Exception as e:
            print(f"删除失败原因是：{e}")

if __name__ == "__main__":

    # 实例化
    my_query = OptSqlite("contents.db")

    # 创建一张表
    # my_query.new_table("address_book")
    
    # 增加或修改一个联系人的电话
    my_query.set_one_phone("Jerry","12344445556")
    
    # 查询一个联系人的电话
    phone = my_query.get_one_phone("Jerry")    
    print(phone)
    
    # 查询所有人的电话
    contents = my_query.get_all_contents()
    print(contents)

    # 删除一个联系人
    my_query.delete_one_content("Jerry")


    contents = my_query.get_all_contents()
    print(contents)   

    # 关闭连接
    my_query.close()
