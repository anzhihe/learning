#!/usr/bin/env python

from distutils.log import warn as printf
from os.path import dirname
from random import randrange as rand
from sqlobject import *
from ushuffle_dbU import DBNAME, NAMELEN, randName, FIELDS, tformat, cformat, setup

DSNs = {
     'mysql': 'mysql://root@localhost/%s' % DBNAME,
    'sqlite': 'sqlite:///:memory:',
}

class Users(SQLObject):
    login  = StringCol(length=NAMELEN)
    userid = IntCol()
    projid = IntCol()
    def __str__(self):
        return ''.join(map(tformat,
            (self.login, self.userid, self.projid)))

class SQLObjectTest(object):
    def __init__(self, dsn):
        try:
            cxn = connectionForURI(dsn)
        except ImportError:
            raise RuntimeError()
        try:
            cxn.releaseConnection(cxn.getConnection())
        except dberrors.OperationalError:
            cxn = connectionForURI(dirname(dsn))
            cxn.query("CREATE DATABASE %s" % DBNAME)
            cxn = connectionForURI(dsn)
        self.cxn = sqlhub.processConnection = cxn

    def insert(self):
        for who, userid in randName():
            Users(login=who, userid=userid, projid=rand(1,5))

    def update(self):
        fr = rand(1,5)
        to = rand(1,5)
        i = -1
        users = Users.selectBy(projid=fr)
        for i, user in enumerate(users):
            user.projid = to
        return fr, to, i+1

    def delete(self):
        rm = rand(1,5)
        users = Users.selectBy(projid=rm)
        i = -1
        for i, user in enumerate(users):
            user.destroySelf()
        return rm, i+1

    def dbDump(self):
        printf('\n%s' % ''.join(map(cformat, FIELDS)))
        for user in Users.select():
            printf(user)

    def finish(self):
        self.cxn.close()

def main():
    printf('*** Connect to %r database' % DBNAME)
    db = setup()
    if db not in DSNs:
        printf('\nERROR: %r not supported, exit' % db)
        return

    try:
        orm = SQLObjectTest(DSNs[db])
    except RuntimeError:
        printf('\nERROR: %r not supported, exit' % db)
        return

    printf('\n*** Create users table (drop old one if appl.)')
    Users.dropTable(True)
    Users.createTable()

    printf('\n*** Insert names into table')
    orm.insert()
    orm.dbDump()

    printf('\n*** Move users to a random group')
    fr, to, num = orm.update()
    printf('\t(%d users moved) from (%d) to (%d)' % (num, fr, to))
    orm.dbDump()

    printf('\n*** Randomly delete group')
    rm, num = orm.delete()
    printf('\t(group #%d; %d users removed)' % (rm, num))
    orm.dbDump()

    printf('\n*** Drop users table')
    Users.dropTable()
    printf('\n*** Close cxns')
    orm.finish()

if __name__ == '__main__':
    main()
