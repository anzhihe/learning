#!/usr/bin/env python

import os
from random import randrange as rrange
from sqlalchemy import *
from ushuffle_db import NAMES, randName

FIELDS = ('login', 'uid', 'prid')
DBNAME = 'test'
COLSIZ = 10

class MySQLAlchemy(object):
    def __init__(self, db, dbName):
        import MySQLdb
        import _mysql_exceptions
        MySQLdb = pool.manage(MySQLdb)
        url = 'mysql://db=%s' % DBNAME
        eng = create_engine(url)
        try:
            cxn = eng.connection()
        except _mysql_exceptions.OperationalError, e:
            eng1 = create_engine('mysql://user=root')
            try:
                eng1.execute('DROP DATABASE %s' % DBNAME)
            except _mysql_exceptions.OperationalError, e:
                pass
            eng1.execute('CREATE DATABASE %s' % DBNAME)
            eng1.execute(
                "GRANT ALL ON %s.* TO ''@'localhost'" % DBNAME)
            eng1.commit()
            cxn = eng.connection()

        try:
            users = Table('users', eng, autoload=True)
        except exceptions.SQLError, e:
            users = Table('users', eng,
                Column('login', String(8)),
                Column('uid', Integer),
                Column('prid', Integer),
                redefine=True)

        self.eng = eng
        self.cxn = cxn
        self.users = users

    def create(self):
        users = self.users
        try:
            users.drop()
        except exceptions.SQLError, e:
            pass
        users.create()

    def insert(self):
        d = [dict(zip(FIELDS,
            [who, uid, rrange(1,5)])) for who, uid in randName()]
        return self.users.insert().execute(*d).rowcount

    def update(self):
        users = self.users
        fr = rrange(1,5)
        to = rrange(1,5)
        return fr, to, \
            users.update(users.c.prid==fr).execute(prid=to).rowcount

    def delete(self):
        users = self.users
        rm = rrange(1,5)
        return rm, \
            users.delete(users.c.prid==rm).execute().rowcount

    def dbDump(self):
        res = self.users.select().execute()
        print '\n%s%s%s' % ('LOGIN'.ljust(COLSIZ),
            'USERID'.ljust(COLSIZ), 'PROJ#'.ljust(COLSIZ))
        for data in res.fetchall():
            print '%s%s%s' % tuple([str(s).title().ljust(COLSIZ) for s in data])

    def __getattr__(self, attr):
        return getattr(self.users, attr)

    def finish(self):
        self.cxn.commit()
        self.eng.commit()

def main():
    print '*** Connecting to %r database' % DBNAME
    orm = MySQLAlchemy('mysql', DBNAME)

    print '\n*** Creating users table'
    orm.create()

    print '\n*** Inserting names into table'
    orm.insert()
    orm.dbDump()

    print '\n*** Randomly moving folks',
    fr, to, num = orm.update()
    print 'from one group (%d) to another (%d)' % (fr, to)
    print '\t(%d users moved)' % num
    orm.dbDump()

    print '\n*** Randomly choosing group',
    rm, num = orm.delete()
    print '(%d) to delete' % rm
    print '\t(%d users removed)' % num
    orm.dbDump()

    print '\n*** Dropping users table'
    orm.drop()
    orm.finish()

if __name__ == '__main__':
    main()
