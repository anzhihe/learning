# -*- coding: utf-8 -*-
import os,sys
import time
import sys
import string
import MySQLdb
from  config import *
import logging

class CteateRRD():
    #初始化    
    def __init__(self,_url):
        self.URL=_url[0]
        self.domain=self.GetURLdomain(_url[0])
        self.rrdfiletype=['time','download','unavailable']
        self.HID=[]
        logging.basicConfig(level=logging.DEBUG,
            format='%(asctime)s [%(levelname)s] %(message)s',
            filename=os.path.dirname(os.path.realpath(__file__))+'/syslog.log',
            filemode='a')

    #创建rrd
    def create(self):
        self.getID()
        for id in  self.HID:
            for filename in self.rrdfiletype:
                rrdpath=RRDPATH+'/'+str(self.domain)+'/'+str(id)+'_'+str(filename)+'.rrd'
                try:
                    os.system("/bin/sh  "+os.path.dirname(os.path.realpath(__file__))+'/createrrd.sh '+str(rrdpath)+' '+str(filename))
                except Exception,e:
                    logging.error('create rrd error!'+str(e))

    #获取ID
    def getID(self):
        conn =   MySQLdb.Connection(DBHOST, DBUSER, DBPASSWORD, DBNAME)
        cursor =   conn.cursor()
        cursor.execute("select ID from webmonitor_hostinfo where URL='%s'"%(self.URL))
        for row in cursor.fetchall():
            self.HID.append(row[0])
        conn.close()
        
    #获取URL域名
    def GetURLdomain(self,url):
        xurl=""
        if url[:7]=="http://":
            xurl=url[7:]
        else:
            xurl=url
        return string.split(xurl,'/')[0]

if __name__ == '__main__':
    app=CteateRRD(sys.argv[1:])
    app.create()