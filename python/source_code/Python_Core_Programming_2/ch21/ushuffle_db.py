#!/usr/bin/env python

import os
from random import randrange as rrange

COLSIZ = 10
RDBMSs = {'s': 'sqlite', 'm': 'mysql', 'g': 'gadfly'}
DB_EXC = None

def setup():
    return RDBMSs[raw_input('''
Choose a database system:

(M)ySQL
(G)adfly
(S)QLite

Enter choice: ''').strip().lower()[0]]

def connect(db, dbName):
    global DB_EXC
    dbDir = '%s_%s' % (db, dbName)

    if db == 'sqlite':
        try:
            import sqlite3
        except ImportError, e:
            try:
                from pysqlite2 import dbapi2 as sqlite3
            except ImportError, e:
                return None

        DB_EXC = sqlite3
        if not os.path.isdir(dbDir):
            os.mkdir(dbDir)
        cxn = sqlite3.connect(os.path.join(dbDir, dbName))

    elif db == 'mysql':
        try:
            import MySQLdb
            import _mysql_exceptions as DB_EXC 
        except ImportError, e:
            return None

        try:
            cxn = MySQLdb.connect(db=dbName)
        except DB_EXC.OperationalError, e:
            cxn = MySQLdb.connect(user='root')
            try:
                cxn.query('DROP DATABASE %s' % dbName)
            except DB_EXC.OperationalError, e:
                pass
            cxn.query('CREATE DATABASE %s' % dbName)
            cxn.query("GRANT ALL ON %s.* to ''@'localhost'" % dbName)
            cxn.commit()
            cxn.close()
            cxn = MySQLdb.connect(db=dbName)

    elif db == 'gadfly':
        try:
            from gadfly import gadfly
            DB_EXC = gadfly
        except ImportError, e:
            return None

        try:
            cxn = gadfly(dbName, dbDir)
        except IOError, e:
            cxn = gadfly()
            if not os.path.isdir(dbDir):
                os.mkdir(dbDir)
            cxn.startup(dbName, dbDir)
    else:
        return None
    return cxn

def create(cur):
    try:
        cur.execute('''
            CREATE TABLE users (
                login VARCHAR(8),
                uid INTEGER,
                prid INTEGER)
        ''')
    except DB_EXC.OperationalError, e:
        drop(cur)
        create(cur)

drop = lambda cur: cur.execute('DROP TABLE users')

NAMES = (
    ('aaron', 8312), ('angela', 7603), ('dave', 7306),
    ('davina',7902), ('elliot', 7911), ('ernie', 7410),
    ('jess', 7912), ('jim', 7512), ('larry', 7311),
    ('leslie', 7808), ('melissa', 8602), ('pat', 7711),
    ('serena', 7003), ('stan', 7607), ('faye', 6812),
    ('amy', 7209),
)

def randName():
    pick = list(NAMES)
    while len(pick) > 0:
        yield pick.pop(rrange(len(pick)))

def insert(cur, db):
    if db == 'sqlite':
        cur.executemany("INSERT INTO users VALUES(?, ?, ?)",
        [(who, uid, rrange(1,5)) for who, uid in randName()])
    elif db == 'gadfly':
        for who, uid in randName():
            cur.execute("INSERT INTO users VALUES(?, ?, ?)",
            (who, uid, rrange(1,5)))
    elif db == 'mysql':
        cur.executemany("INSERT INTO users VALUES(%s, %s, %s)",
        [(who, uid, rrange(1,5)) for who, uid in randName()])

getRC = lambda cur: cur.rowcount if hasattr(cur, 'rowcount') else -1

def update(cur):
    fr = rrange(1,5)
    to = rrange(1,5)
    cur.execute(
        "UPDATE users SET prid=%d WHERE prid=%d" % (to, fr))
    return fr, to, getRC(cur)

def delete(cur):
    rm = rrange(1,5)
    cur.execute('DELETE FROM users WHERE prid=%d' % rm)
    return rm, getRC(cur)

def dbDump(cur):
    cur.execute('SELECT * FROM users')
    print '\n%s%s%s' % ('LOGIN'.ljust(COLSIZ),
        'USERID'.ljust(COLSIZ), 'PROJ#'.ljust(COLSIZ))
    for data in cur.fetchall():
        print '%s%s%s' % tuple([str(s).title().ljust(COLSIZ) \
            for s in data])

def main():
    db = setup()
    print '*** Connecting to %r database' % db
    cxn = connect(db, 'test')
    if not cxn:
        print '\nERROR: %r not supported, exiting' % db
        return
    cur = cxn.cursor()

    print '\n*** Creating users table'
    create(cur)

    print '\n*** Inserting names into table'
    insert(cur, db)
    dbDump(cur)

    print '\n*** Randomly moving folks',
    fr, to, num = update(cur)
    print 'from one group (%d) to another (%d)' % (fr, to)
    print '\t(%d users moved)' % num
    dbDump(cur)

    print '\n*** Randomly choosing group',
    rm, num = delete(cur)
    print '(%d) to delete' % rm
    print '\t(%d users removed)' % num
    dbDump(cur)

    print '\n*** Dropping users table'
    drop(cur)
    cur.close()
    cxn.commit()
    cxn.close()

if __name__ == '__main__':
    main()
