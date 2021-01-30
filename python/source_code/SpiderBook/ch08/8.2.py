#coding:utf-8

import MySQLdb

con = MySQLdb.connect(host='localhost', user='root', passwd='', db='test', port=3306, charset='utf8')
cur = con.cursor()

cur.execute(' CREATE TABLE person (id int not null auto_increment primary key,name varchar(20),age int)')
data="'qiye',20"
cur.execute(' INSERT INTO person (name,age) VALUES (%s)'%data)

cur.execute(' INSERT INTO person (name,age) VALUES (%s,%s)',('qiye',20))

cur.executemany(' INSERT INTO person (name,age) VALUES (%s,%s)',[('marry',20),('jack',20)])

con.commit()

cur.execute('SELECT * FROM person')

cur.execute('SELECT * FROM person')
res = cur.fetchall()
for line in res:
    print line
    cur.execute('SELECT * FROM person')
    res = cur.fetchone()
    print res

cur.execute('UPDATE person SET name=%s WHERE id=%s', ('rose', 1))
cur.execute('DELETE FROM person WHERE id=%s', (0,))
con.commit()
con.close()
