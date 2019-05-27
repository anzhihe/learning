# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------#
# Name:        DBclass.py                                                    #
# Purpose:     Management App Server DBclass(by socket)                      #
# Author:      Liutiansi                                                     #
# Email:       liutiansi@gamil.com                                           #
# Created:     2008/10/18                                                    #
# Copyright:   (c) 2008                                                      #
#-----------------------------------------------------------------------------

import sys
import MySQLdb
import ConfigParser
class DBclass:

#----------------------------------------------------------------------------#
# 初始化数据连接的构造函数及销毁连接函数               	                     #
#----------------------------------------------------------------------------#
#                                                                            #
#   调用方法：参数读取config.py          	                             #
#                                                                            #
#                                                                            #
#-----------------------------------------------------------------------------
    def __init__(self):
        try:
            self.cf = ConfigParser.ConfigParser()
            self.cf.read(sys.path[0]+'/data/config.ini')
            self.db_ip= self.cf.get("db","db_ip")
            self.db_user= self.cf.get("db","db_user")
            self.db_pass= self.cf.get("db","db_pass")
            self.db_name= self.cf.get("db","db_name")
            self.connection = MySQLdb.connect(self.db_ip,self.db_user,self.db_pass,self.db_name,charset="utf8")
            self.cur = self.connection.cursor()
            self.cur.execute("SET NAMES utf8")
            self.cur.execute("SET CHARACTER_SET_CLIENT=utf8")
            self.cur.execute("SET CHARACTER_SET_RESULTS=utf8")
        except MySQLdb.OperationalError, message:
            print  u"Error:连接数据库出现，请速与liutiansi@gamil.com联系。"
            return

    def __del__(self):
        self.connection.close()
        

#----------------------------------------------------------------------------#
# 管理员登录验证方法                            	                     #
#----------------------------------------------------------------------------#
#                                                                            #
#   调用方法：fetchone(self,sql语句)       	                             #
#                                                                            #
#                                                                            #
#-----------------------------------------------------------------------------
    def fetchone(self, sql):
        try:
            self.cur.execute(sql)
            return self.cur.rowcount
        except Exception, exception:
            return False


    def fetchallq(self, sql):
        try:
            self.cur.execute(sql)
            return self.cur.fetchall()
        except Exception,e:
            print  str(e)
            return False
 
    
           
    def execute(self, sql, param=None):
        try:
            self.cur.execute(sql)
        except Exception,e:
            print  str(e)
            return None
            
    
class User():
    def Check(self,name, password,Privatekey):
        import md5
        m = md5.new(password)
        md5pass=m.hexdigest()
        myrow=DBclass()
        sql = "select admin,privileges from users where admin='%s' and passwd='%s' and Privatekey='%s'"% (name, md5pass,Privatekey)
        result = myrow.fetchallq(sql)
        return result
    
class sysbash():
    def __init__(self):
        self.myrow=DBclass()
        

    def GetUpdateVersion(self):
        result=[]
        sql = "select version from upgrade"
        result = self.myrow.fetchallq(sql)
        return result
    

    def Addsyslogs(self,user,event):
        sql = "insert into user_logs(user,event)values('%s','%s')" % (user,event)
        return self.myrow.execute(sql)