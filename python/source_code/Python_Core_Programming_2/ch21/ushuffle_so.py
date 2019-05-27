#!/usr/bin/env python

import os
from random import randrange as rrange
from sqlobject import *
from ushuffle_db import NAMES, randName

DBNAME = 'test'
COLSIZ = 10
FIELDS = ('login', 'uid', 'prid')

class MySQLObject(object):
    def __init__(self, db, dbName):
        import MySQLdb
        import _mysql_exceptions
        url = 'mysql://localhost/%s' % DBNAME

        while True:
            cxn = connectionForURI(url)
            sqlhub.processConnection = cxn
            #cxn.debug = True
            try:
                class Users(SQLObject):
                    class sqlmeta:
                        fromDatabase = True
                    login = StringCol(length=8)
                    uid = IntCol()
                    prid = IntCol()
                break
            except _mysql_exceptions.ProgrammingError, e:
                class Users(SQLObject):
                    login = StringCol(length=8)
                    uid = IntCol()
                    prid = IntCol()
                break
            except _mysql_exceptions.OperationalError, e:
                cxn1 = sqlhub.processConnection=connectionForURI('mysql://root@localhost')
                cxn1.query("CREATE DATABASE %s" % DBNAME)
                cxn1.query("GRANT ALL ON %s.* TO ''@'localhost'" % DBNAME)
                cxn1.close()
        self.users = Users
        self.cxn = cxn

    def create(self):
        Users = self.users
        Users.dropTable(True)
        Users.createTable()

    def insert(self):
        for who, uid in randName():
            self.users(**dict(zip(FIELDS,
                [who, uid, rrange(1,5)])))

    def update(self):
        fr = rrange(1,5)
        to = rrange(1,5)
        users = self.users.selectBy(prid=fr)
        for i, user in enumerate(users):
            user.prid = to
        return fr, to, i+1

    def delete(self):
        rm = rrange(1,5)
        users = self.users.selectBy(prid=rm)
        for i, user in enumerate(users):
            user.destroySelf()
        return rm, i+1

    def dbDump(self):
        print '\n%s%s%s' % ('LOGIN'.ljust(COLSIZ),
            'USERID'.ljust(COLSIZ), 'PROJ#'.ljust(COLSIZ))
        for usr in self.users.select():
            print '%s%s%s' % (tuple([str(getattr(usr,
                field)).title().ljust(COLSIZ) \
                for field in FIELDS]))

    drop = lambda self: self.users.dropTable()
    finish = lambda self: self.cxn.close()

def main():
    print '*** Connecting to %r database' % DBNAME
    orm = MySQLObject('mysql', DBNAME)

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
