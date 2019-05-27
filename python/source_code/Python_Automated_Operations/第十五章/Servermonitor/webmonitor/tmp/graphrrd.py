# -*- coding: utf-8 -*-
import os,sys
import time
import sys
import pycurl
import string
import MySQLdb
from  config import *
import logging

class GraphRRD():
    #初始化    
    def __init__(self):
        #初始化日志对象
        logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    filename=os.path.dirname(os.path.realpath(__file__))+'/syslog.log',
                    filemode='a')
        
        #连接数据
        try:
            self.conn =   MySQLdb.Connection(DBHOST, DBUSER, DBPASSWORD, DBNAME)
            self.cursor =  self.conn.cursor()
        except Exception,e:
            logging.error('connect database error!'+str(e))
            return
        
        self.rrdfiletype=['time','download','unavailable']
        self.GraphDate=['current','day','month','year']
        self.GraphStart=['-3h','-1day','-1month','-1year']
        self.GraphEnd=['now','now','now','now']

    #虚构方法
    def __del__(self):
        try:
            self.cursor.close()
            self.conn.close()
        except Exception,e:
            logging.debug('__del__ object error!'+str(e))

    #更新rrd文件
    def RungraphRRD(self,rowobj):
        Appdomain=str(self.GetURLdomain(rowobj[2]))
        time_rrdpath=RRDPATH+'/'+Appdomain+'/'+str(rowobj[0])+'_'+str(self.rrdfiletype[0])+'.rrd'
        download_rrdpath=RRDPATH+'/'+Appdomain+'/'+str(rowobj[0])+'_'+str(self.rrdfiletype[1])+'.rrd'
        unavailable_rrdpath=RRDPATH+'/'+Appdomain+'/'+str(rowobj[0])+'_'+str(self.rrdfiletype[2])+'.rrd'
        
        i=0
        for datetype in self.GraphDate:
            time_pngpath=PNGPATH+'/'+Appdomain+'/'+str(datetype)+'_'+str(rowobj[0])+'_'+str(self.rrdfiletype[0])+'.png'
            download_pngpath=PNGPATH+'/'+Appdomain+'/'+str(datetype)+'_'+str(rowobj[0])+'_'+str(self.rrdfiletype[1])+'.png'
            unavailable_pngpath=PNGPATH+'/'+Appdomain+'/'+str(datetype)+'_'+str(rowobj[0])+'_'+str(self.rrdfiletype[2])+'.png'

            try:
                os.system("/bin/sh  "+os.path.dirname(os.path.realpath(__file__))+'/graphrrd.sh '+str(time_rrdpath)+' '+str(time_pngpath)+' '+'time'+' '+str(rowobj[1])+' '+self.GraphStart[i]+' '+self.GraphEnd[i]+' '+str(TIME_YMAX)+' '+str(TIME_ALARM))
                os.system("/bin/sh  "+os.path.dirname(os.path.realpath(__file__))+'/graphrrd.sh '+str(download_rrdpath)+' '+str(download_pngpath)+' '+'download'+' '+str(rowobj[1])+' '+self.GraphStart[i]+' '+self.GraphEnd[i]+' '+str(DOWN_APEED_YMAX))
                os.system("/bin/sh  "+os.path.dirname(os.path.realpath(__file__))+'/graphrrd.sh '+str(unavailable_rrdpath)+' '+str(unavailable_pngpath)+' '+'unavailable'+' '+str(rowobj[1])+' '+self.GraphStart[i]+' '+self.GraphEnd[i])
            except Exception,e:
                logging.error('graph rrd error:'+str(e))
            i+=1

    #获取应用信息
    def getHostdata(self):
        try:
            self.cursor.execute("select ID,AppName,URL from webmonitor_hostinfo")
            for row in self.cursor.fetchall():
                self.RungraphRRD(row)
        except Exception,e:
            logging.error('Get Host data  error:'+str(e))

    #获取URL域名
    def GetURLdomain(self,url):
        xurl=""
        if url[:7]=="http://":
            xurl=url[7:]
        else:
            xurl=url
        return string.split(xurl,'/')[0]

if __name__ == '__main__':
    app=GraphRRD()
    app.getHostdata()