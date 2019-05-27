# -*- coding: utf-8 -*-
#
#--------------------------------------------------------------------------
# views.py
#--------------------------------------------------------------------------
# auther:Liutiansi
# Email:liutiansi@gmail.com
#Blog:http://blog.liuts.com
# update:2014-06-06
#
#---------------------------------------------------------------------------
import string,re,os
import time,datetime
import logging
import rrdtool
from webmonitor.models import Hostinfo
from webmonitor.models import MonitorData
from webmonitor.config import *
#from pyExcelerator import *
from decimal import Decimal
from django.conf import settings

#初始化日志对象
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    filename=os.path.dirname(os.path.realpath(__file__))+'/syslog.log',
                    filemode='a')


"""
=生成图表方法(日/月/年/当前图表)
-Graphrrd_normal(_id,url,appname)
参数说明：ID,开始时间，结束时间，URL，应用名称
"""
def Graphrrd_normal(_id,url,appname):

    rrdfiletype=['time','download','unavailable']
    GraphDate=['current','day','month','year']
    GraphStart=['-3h','-1day','-1month','-1year']
    GraphEnd=['now','now','now','now']
        
    Appdomain=str(GetURLdomain(url))
    time_rrdpath=settings.RRDPATH+'/'+Appdomain+'/'+str(_id)+'_'+str(rrdfiletype[0])+'.rrd'
    download_rrdpath=settings.RRDPATH+'/'+Appdomain+'/'+str(_id)+'_'+str(rrdfiletype[1])+'.rrd'
    unavailable_rrdpath=settings.RRDPATH+'/'+Appdomain+'/'+str(_id)+'_'+str(rrdfiletype[2])+'.rrd'
    
    i=0
    for datetype in GraphDate:
        time_pngpath=settings.PNGPATH+'/'+Appdomain+'/'+str(datetype)+'_'+str(_id)+'_'+str(rrdfiletype[0])+'.png'
        download_pngpath=settings.PNGPATH+'/'+Appdomain+'/'+str(datetype)+'_'+str(_id)+'_'+str(rrdfiletype[1])+'.png'
        unavailable_pngpath=settings.PNGPATH+'/'+Appdomain+'/'+str(datetype)+'_'+str(_id)+'_'+str(rrdfiletype[2])+'.png'

        try:
            os.system("/bin/sh  "+settings.MAINAPPPATH+'/graphrrd.sh '+str(time_rrdpath)+' '+str(time_pngpath)+' '+'time'+' '+appname.encode('utf-8')+' '+GraphStart[i]+' '+GraphEnd[i]+' '+str(settings.TIME_YMAX)+' '+str(settings.TIME_ALARM))
            os.system("/bin/sh  "+settings.MAINAPPPATH+'/graphrrd.sh '+str(download_rrdpath)+' '+str(download_pngpath)+' '+'download'+' '+appname.encode('utf-8')+' '+GraphStart[i]+' '+GraphEnd[i]+' '+str(settings.DOWN_APEED_YMAX))
            os.system("/bin/sh  "+settings.MAINAPPPATH+'/graphrrd.sh '+str(unavailable_rrdpath)+' '+str(unavailable_pngpath)+' '+'unavailable'+' '+appname.encode('utf-8')+' '+GraphStart[i]+' '+GraphEnd[i])
        except Exception,e:
            logging.error('Graphrrd normal rrd png error:'+str(e))
        i+=1
            
"""
=生成图表方法(自定义)
-Graphrrd(_id,_starttime,_endtime,url,appname)
参数说明：ID,开始时间，结束时间，URL，应用名称
"""
def Graphrrd_custom(_id,_starttime,_endtime,url,appname):
            #自定义时间查询及生成rrd图表
            StartTime=_starttime
            EndTime=_endtime
            #graphrrd user defind
            rrdfiletype=['time','download','unavailable']
            Appdomain=str(GetURLdomain(url))
            time_rrdpath=settings.RRDPATH+'/'+Appdomain+'/'+str(_id)+'_time.rrd'
            download_rrdpath=settings.RRDPATH+'/'+Appdomain+'/'+str(_id)+'_download.rrd'
            unavailable_rrdpath=settings.RRDPATH+'/'+Appdomain+'/'+str(_id)+'_unavailable.rrd'
        
            time_pngpath=settings.PNGPATH+'/'+Appdomain+'/'+str(_id)+'_time.png'
            download_pngpath=settings.PNGPATH+'/'+Appdomain+'/'+str(_id)+'_download.png'
            unavailable_pngpath=settings.PNGPATH+'/'+Appdomain+'/'+str(_id)+'_unavailable.png'
            try:
                os.system("/bin/sh  "+settings.MAINAPPPATH+'/graphrrd.sh '+str(time_rrdpath)+' '+str(time_pngpath)+' '+'time'+' '+appname.encode('utf-8')+' '+str(StartTime)+' '+str(EndTime)+' '+str(settings.TIME_YMAX)+' '+str(settings.TIME_ALARM))
                os.system("/bin/sh  "+settings.MAINAPPPATH+'/graphrrd.sh '+str(download_rrdpath)+' '+str(download_pngpath)+' '+'download'+' '+appname.encode('utf-8')+' '+str(StartTime)+' '+str(EndTime)+' '+str(settings.DOWN_APEED_YMAX))
                os.system("/bin/sh  "+settings.MAINAPPPATH+'/graphrrd.sh '+str(unavailable_rrdpath)+' '+str(unavailable_pngpath)+' '+'unavailable'+' '+appname.encode('utf-8')+' '+str(StartTime)+' '+str(EndTime))
            except Exception,e:
                logging.error('Graphrrd custom rrd png error:'+str(e))
                return


"""
=png2bmp
-png2bmp(source,target)
"""
def png2bmp(sourceadd,targetadd):
    from PIL import Image
    try:
        file_in = sourceadd
        img = Image.open(file_in)
        file_out = targetadd
        if len(img.split()) == 4:
            r, g, b, a = img.split()
            img = Image.merge("RGB", (r, g, b))
            img.save(file_out)
        else:
            img.save(file_out)
        return
    except Exception,e:
        logging.error('Graph png2bmp error:'+str(e))
        return



"""
=获取应用表平均数据
-GetAppDateReport(应用ID,starttime,endtime)
"""
def GetAppDateReport(ID,_starttime,_endtime):
    from django.db import connection
    ReportListobj=[]
    try:
        cursor = connection.cursor()
        for _id in ID:
            cursor.execute("select avg(NAMELOOKUP_TIME),avg(CONNECT_TIME),avg(PRETRANSFER_TIME),avg(STARTTRANSFER_TIME),avg(TOTAL_TIME),avg(SPEED_DOWNLOAD) from webmonitor_monitordata where HTTP_CODE='200' and FID='%d' and DATETIME>='%d' and DATETIME<='%d'"%(int(_id),int(_starttime),int(_endtime)))
            row = cursor.fetchone()
            ReportListobj.append(row)
        return ReportListobj
    except Exception,e:
        logging.error('select database error!'+str(e))
        return


"""
=获取应用不可用数据
-GetAppUnavailableReport(应用ID,starttime,endtime)
"""
def GetAppUnavailableReport(ID,_starttime,_endtime):
    if ID==None:
        return MonitorData.objects.values('HTTP_CODE','DATETIME','FID').filter(DATETIME__gte=_starttime,DATETIME__lte=_endtime).exclude(HTTP_CODE='200').order_by('FID','ID')
    else:
        return MonitorData.objects.values('HTTP_CODE','DATETIME','FID').filter(FID__in=ID, DATETIME__gte=_starttime,DATETIME__lte=_endtime).exclude(HTTP_CODE='200').order_by('FID','ID')


"""
=根据ID获取应用名称
-GetAppName(应用ID)
"""
def GetAppName(_id):
    return Hostinfo.objects.values('AppName').get(ID=_id)


"""
=获取当前应用数据中心ID清单
-GetAppIDCId(应用ID)
"""
def GetAppIDCId(_id):
    from django.db import connection
    ID_list=[]
    try:
        cursor = connection.cursor()
        if _id==None:
            cursor.execute("select ID from webmonitor_hostinfo")
        else:
            cursor.execute("select ID from webmonitor_hostinfo where URL in (select URL from webmonitor_hostinfo where ID='%d')"%(int(_id)))
        for row in cursor.fetchall():
            ID_list.append(row[0])
        return ID_list
    except Exception,e:
        logging.error('select database error!'+str(e))
        return


"""
=获取当前应用数据中心名称清单
-GetAppIDCName(应用ID)
"""
def GetAppIDCName(_id):
    from django.db import connection
    ID_list=[]
    try:
        cursor = connection.cursor()
        if _id==None:
            cursor.execute("select IDC,AppName from webmonitor_hostinfo")
        else:
            cursor.execute("select IDC,AppName from webmonitor_hostinfo where URL in (select URL from webmonitor_hostinfo where ID='%d')"%(int(_id)))
        for row in cursor.fetchall():
            ID_list.append(row)
        return ID_list
    except Exception,e:
        logging.error('select database error!'+str(e))
        return


"""
=获取应用表数据
-GetHostinfo(应用ID)
"""
def GetHostinfo(_id):
        return Hostinfo.objects.filter(ID=_id)

"""
=日期转时间戳
-time2stamp(日期＋时间)
"""
def time2stamp(_datetime):
        return int(time.mktime(time.strptime(_datetime,'%Y-%m-%d %H:%M:%S')))

"""
=时间戳转日期
-stamp2time(时间戳)
"""
def stamp2time(_stamp):
        stamp=time.localtime(_stamp)
        return time.strftime("%Y-%m-%d %H:%M:%S", stamp)


"""
=获取上周天清单
-GetLastweek(时间戳)
"""
def GetLastweek(_today):
    date = _today
    year, mon, day = int(date[:4]), int(date[4:6]), int(date[6:])
    d = datetime.datetime(year, mon, day)
    b = d-datetime.timedelta(d.weekday() + 1)
    days = []
    for i in range(6, -1, -1):
    	c = b-datetime.timedelta(i)
    	days.append(c.strftime('%Y-%m-%d'))
    return days


"""
=校验URL合法性
-CheckURLok(url字串符)
-True:合法
-False:非法
"""
def CheckURLok(url):
    p = re.compile(r'^(http://)?[a-zA-Z0-9]+(.[a-zA-Z0-9]+)*(\w|/)+$')
    m = p.match(url)
    if m:
       return True
    else:
        return False


"""
=获取URL域名
-GetURLdomain(url)
-返回URL域名,例如:www.baidu.com
"""
def GetURLdomain(url):
    xurl=""
    if url[:7]=="http://":
        xurl=url[7:]
    else:
        xurl=url
    return string.split(xurl,'/')[0]


"""
=获取URL路径部分
-GetURLpath(url)
-返回URL路径,例如:/pub/content/1/364563.html
"""
def GetURLdopath(url):
    xurl=""
    if url[:7]=="http://":
        xurl=url[8:]
    else:
        xurl=url
    return xurl[xurl.find('/'):]
    

"""
=获取监控URL ID
-getID(url)
"""
def getID(url):
    URL=url
    HID=[]
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("select ID from webmonitor_hostinfo where URL='%s'"%(URL))
    for row in cursor.fetchall():
        HID.append(row[0])
    connection.close()
    return HID
        

"""
=创建rrd
-create_rrd(url)
"""
def create_rrd(url):
    URL=url
    domain=GetURLdomain(url)
    HID=[]
    cur_time=str(int(time.time()))
    
    HID=getID(URL)
    for id in  HID:
        try:
            rrd_time=rrdtool.create(settings.RRDPATH+'/'+str(domain)+'/'+str(id)+ \
                    '_time.rrd','--step','300','--start',cur_time,
                    'DS:NAMELOOKUP_TIME:GAUGE:600:0:U',
                    'DS:CONNECT_TIME:GAUGE:600:0:U',
                    'DS:PRETRANSFER_TIME:GAUGE:600:0:U',
                    'DS:STARTTRANSFER_TIME:GAUGE:600:0:U',
                    'DS:TOTAL_TIME:GAUGE:600:0:U',
                    'RRA:AVERAGE:0.5:1:600',
                    'RRA:AVERAGE:0.5:6:700',
                    'RRA:AVERAGE:0.5:24:775',
                    'RRA:AVERAGE:0.5:288:797',
                    'RRA:MAX:0.5:1:600',
                    'RRA:MAX:0.5:6:700',
                    'RRA:MAX:0.5:24:775',
                    'RRA:MAX:0.5:444:797',
                    'RRA:MIN:0.5:1:600',
                    'RRA:MIN:0.5:6:700',
                    'RRA:MIN:0.5:24:775',
                    'RRA:MIN:0.5:444:797')
            if rrd_time:
                logging.error(rrdtool.error())

            rrd_download=rrdtool.create(settings.RRDPATH+'/'+str(domain)+'/'+str(id)+ \
                    '_download.rrd','--step','300','--start',cur_time,
                    'DS:SPEED_DOWNLOAD:GAUGE:600:0:U',
                    'RRA:AVERAGE:0.5:1:600',
                    'RRA:AVERAGE:0.5:6:700',
                    'RRA:AVERAGE:0.5:24:775',
                    'RRA:AVERAGE:0.5:288:797',
                    'RRA:MAX:0.5:1:600',
                    'RRA:MAX:0.5:6:700',
                    'RRA:MAX:0.5:24:775',
                    'RRA:MAX:0.5:444:797',
                    'RRA:MIN:0.5:1:600',
                    'RRA:MIN:0.5:6:700',
                    'RRA:MIN:0.5:24:775',
                    'RRA:MIN:0.5:444:797')
            if rrd_download:
                logging.error(rrdtool.error())

            rrd_unavailable=rrdtool.create(settings.RRDPATH+'/'+str(domain)+'/'+str(id)+'_unavailable.rrd','--step','300','--start',cur_time, \
                    'DS:UNAVAILABLE:GAUGE:600:0:U',
                    'RRA:AVERAGE:0.5:1:600',
                    'RRA:AVERAGE:0.5:6:700',
                    'RRA:AVERAGE:0.5:24:775',
                    'RRA:AVERAGE:0.5:288:797',
                    'RRA:MAX:0.5:1:600',
                    'RRA:MAX:0.5:6:700',
                    'RRA:MAX:0.5:24:775',
                    'RRA:MAX:0.5:444:797',
                    'RRA:MIN:0.5:1:600',
                    'RRA:MIN:0.5:6:700',
                    'RRA:MIN:0.5:24:775',
                    'RRA:MIN:0.5:444:797')
            if rrd_unavailable:
                logging.error(rrdtool.error())

        except Exception,e:
            logging.error('create rrd error!'+str(e))
