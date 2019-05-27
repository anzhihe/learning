# -*- coding: utf-8 -*-
#
#--------------------------------------------------------------------------
# views.py
#--------------------------------------------------------------------------
# auther:Liutiansi
# Email:liutiansi@gmail.com
#Blog:http://blog.liuts.com
# update:2010-11-06
#
#---------------------------------------------------------------------------
import string,re,os
import time,datetime
import logging
from  config import *
from pyExcelerator import *
from decimal import Decimal
import MySQLdb

class ExReport():
    #构造方法
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


    #虚构方法
    def __del__(self):
        try:
            self.cursor.close()
            self.conn.close()
        except Exception,e:
            logging.debug('__del__ object error!'+str(e))

    """
    =生成Excel报表方法
    -ExcelReport(_bigtitle,_timeobj,_navailableobj,_idcname,Sheet1,Sheet2,_starttime,_endtime)
    """
    def SetBackColor(self,colorid):
        #单元背景颜色(coloridcolor代号)
        BkgPat = Pattern()
        BkgPat.pattern = Pattern.SOLID_PATTERN
        BkgPat.pattern_fore_colour = colorid
        return BkgPat

    def ExcelReport(self,_id,_bigtitle,_timeobj,_navailableobj,_idcname,Sheet1,Sheet2,_starttime,_endtime):
   
        #对齐方式，上下及左右居中
        Alg = Alignment()
        Alg.horz = Alignment.HORZ_CENTER    #水平居中
        Alg.vert = Alignment.VERT_CENTER    #上下居中
    
        #对齐方式，上下居中，左右靠右
        Algr = Alignment()
        Algr.horz = Alignment.HORZ_RIGHT    #水平居中
        Algr.vert = Alignment.VERT_CENTER    #上下居中

        #大标题样式
        Titlestyle = XFStyle()
        Titlestyle.font.name = u'宋体'
        Titlestyle.font.bold = True
        Titlestyle.font.height = 450
        Titlestyle.alignment = Alg    

        #小标题样式(表格头)
        Theadstyle = XFStyle()
        Theadstyle.font.name = u'宋体'
        Theadstyle.font.colour_index = 17
        Theadstyle.font.size = 21
        Theadstyle.font.height = 250
        Theadstyle.font.outline = True
        Theadstyle.borders.left = 1
        Theadstyle.borders.right = 1
        Theadstyle.borders.top = 1
        Theadstyle.borders.bottom = 1
        Theadstyle.pattern = self.SetBackColor(22)
        Theadstyle.alignment = Alg
    
        #数据区样式
        Datestyle = XFStyle()
        Datestyle.font.name = u'宋体'
        Datestyle.font.colour_index = 8
        Datestyle.font.size = 19
        Datestyle.font.height = 200
        Datestyle.font.outline = True
        Datestyle.borders.left = 1
        Datestyle.borders.right = 1
        Datestyle.borders.top = 1
        Datestyle.borders.bottom = 1
        #Datestyle.num_format_str = '0.00'
        Datestyle.alignment = Algr

        #统计文字样式
        Statstyle = XFStyle()
        Statstyle.font.name = u'宋体'
        Statstyle.font.colour_index = 30
        Statstyle.font.size = 20
        Titlestyle.font.bold = True
        Statstyle.font.height = 220
        Statstyle.font.outline = True
        Statstyle.borders.left = 1
        Statstyle.borders.right = 1
        Statstyle.borders.top = 1
        Statstyle.borders.bottom = 1
        Statstyle.alignment = Alg

        #创建文档对象
        wb = Workbook()
        
        #创建第一个工作蒲
        ws0 = wb.add_sheet(unicode(Sheet1,"utf-8"))
    
        #设置大标题
        ws0.write_merge(0, 0, 0, 7, unicode(_bigtitle,"utf-8"), Titlestyle)

        #设置列宽度
        ws0.col(0).width=5200
        ws0.col(1).width=11500
        ws0.col(2).width=5200
        ws0.col(3).width=4500
        ws0.col(4).width=4500
        ws0.col(5).width=4000
        ws0.col(6).width=4000
        ws0.col(7).width=5200
    
        #设置小标题(表格头)-时间及下载
        #格式：write(行，列，内容，样式)
        ws0.write(1, 0, u'应用名称',Theadstyle)    
        ws0.write(1, 1, u'IDC名称',Theadstyle)    
        ws0.write(1, 2, u'DNS查询时间', Theadstyle)    
        ws0.write(1, 3, u'链接时间', Theadstyle)
        ws0.write(1, 4, u'开始传输时间', Theadstyle)
        ws0.write(1, 5, u'第一字节时间', Theadstyle)
        ws0.write(1, 6, u'总时间', Theadstyle)
        ws0.write(1, 7, u'下载速率(byte/s)', Theadstyle)
    
        #写应用数据
        i=2
        j=0
        try:
            for _data in _timeobj:
                ws0.write(i, 0, _idcname[j][1].decode('utf-8'), Statstyle)
                ws0.write(i, 1, _idcname[j][0], Statstyle)
                ws0.write(i, 2, str( Decimal(str(round(_data[0], 2)))), Datestyle)
                ws0.write(i, 3, str( Decimal(str(round(_data[1], 2)))), Datestyle)
                ws0.write(i, 4, str( Decimal(str(round(_data[2], 2)))), Datestyle)
                ws0.write(i, 5, str( Decimal(str(round(_data[3], 2)))), Datestyle)
                ws0.write(i, 6, str( Decimal(str(round(_data[4], 2)))), Datestyle)
                ws0.write(i, 7, str( Decimal(str(round(_data[5], 2)))), Datestyle)
                i+=1
                j+=1
        except Exception,e:
            logging.error('Write excel timedata error :'+str(e))
            return


	#设置小标题(表格头)-应用失效清单
	#格式：write(行，列，内容，样式)

        #隔一行
        i+=1
        ws0.write(i, 0, u'应用名称', Theadstyle)
        ws0.write(i, 1, u'错误报告', Theadstyle)
        ws0.write(i, 2, u'发生时间', Theadstyle)
        ws0.write(i, 3, u'累计总数', Theadstyle)
        i+=1
        downcount=0
        swapid=0
        currappcount=0
        for _data in _navailableobj:
            if swapid!=_data[2]:
                downappname=self.GetAppName(_data[2])
                if downcount!=0:
                    ws0.write(i-1, 3, str(currappcount), Statstyle)
                    currappcount=0
            else:
                ws0.write(i-1, 3, "", Statstyle)
            ws0.write(i, 0, downappname[0].decode('utf-8'), Statstyle)
            ws0.write(i, 1, str( _data[0]), Datestyle)
            ws0.write(i, 2, str( self.stamp2time(_data[1])), Datestyle)
            downcount+=1
            currappcount+=1
            i+=1
            swapid=_data[2]
        ws0.write(i-1, 3, str(currappcount), Statstyle)
        ws0.write(i, 3, "", Statstyle)
        ws0.write(i, 0, u'', Datestyle)
        ws0.write(i, 1, u'', Datestyle)
        ws0.write(i, 2, u'累计次数：'+str( downcount), Statstyle)
        return wb


    """
    ++++++++++++++++++++++++++++
    =获取应用表平均数据
    -GetAppDateReport(应用ID,starttime,endtime)
    ++++++++++++++++++++++++++++
    """
    def GetAppDateReport(self,ID,_starttime,_endtime):
        ReportListobj=[]
        try:
            for _id in ID:
                self.cursor.execute("select avg(NAMELOOKUP_TIME),avg(CONNECT_TIME),avg(PRETRANSFER_TIME),avg(STARTTRANSFER_TIME),avg(TOTAL_TIME),avg(SPEED_DOWNLOAD) from webmonitor_monitordata where HTTP_CODE='200' and FID='%d' and DATETIME>='%d' and DATETIME<='%d'"%(int(_id),int(_starttime),int(_endtime)))
                row = self.cursor.fetchone()
                ReportListobj.append(row)
            return ReportListobj
        except Exception,e:
            logging.error('select database error!'+str(e))
            return


    """
    =获取应用不可用数据
    -GetAppUnavailableReport(应用ID,starttime,endtime)
    """
    def GetAppUnavailableReport(self,ID,_starttime,_endtime):
        self.cursor.execute("select HTTP_CODE,DATETIME,FID from webmonitor_monitordata where HTTP_CODE!='200'  and DATETIME>='%d' and DATETIME<='%d' order by FID"%(int(_starttime),int(_endtime)))
        return self.cursor.fetchall()



    """
    =根据ID获取应用名称
    -GetAppName(应用ID)
    """
    def GetAppName(self,_id):
        self.cursor.execute("select AppName from webmonitor_hostinfo where ID='%d'"%(_id))
        return self.cursor.fetchone()


    """
    =获取当前应用数据中心ID清单
    -GetAppIDCId(应用ID)
    """
    def GetAppIDCId(self,_id):
        ID_list=[]
        try:
            self.cursor.execute("select ID from webmonitor_hostinfo")
            for row in self.cursor.fetchall():
                ID_list.append(row[0])
            return ID_list
        except Exception,e:
            logging.error('select database error!'+str(e))
            return

    """
    =获取当前应用数据中心名称清单
    -GetAppIDCName(应用ID)
    """
    def GetAppIDCName(self,_id):
        ID_list=[]
        try:
            self.cursor.execute('set names utf8')
            self.cursor.execute("select IDC,AppName from webmonitor_hostinfo")
            for row in self.cursor.fetchall():
                ID_list.append(row)
            return ID_list
        except Exception,e:
            logging.error('select database error!'+str(e))
            return


    """
    =获取应用表数据
    -GetHostinfo(应用ID)
    """
    def GetHostinfo(self,_id):
        self.cursor.execute("select * from webmonitor_hostinfo where ID='%d'"%(_id))
        return self.cursor.fetchall()

    """
    =日期转时间戳
    -time2stamp(日期＋时间)
    """
    def time2stamp(self,_datetime):
        return int(time.mktime(time.strptime(_datetime,'%Y-%m-%d %H:%M:%S')))

    """
    =时间戳转日期
    -stamp2time(时间戳)
    """
    def stamp2time(self,_stamp):
        stamp=time.localtime(_stamp)
        return time.strftime("%Y-%m-%d %H:%M:%S", stamp)


    """
    =获取上周天清单
    -GetLastweek(时间戳)    
    """
    def GetLastweek(self,_today):
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
    def CheckURLok(self,url):
        p = re.compile(r'^(http://)?[a-zA-Z0-9]+(.[a-zA-Z0-9]+)*(\w|/)+$')
        m = p.match(url)
        if m:
           return True
        else:
            return False


    """
    =获取URL域名
    -GetURLdomain(url)
    -返回URL域名,例如:www.tianya.cn
    """
    def GetURLdomain(self,url):
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
    def GetURLdopath(self,url):
        xurl=""
        if url[:7]=="http://":
            xurl=url[8:]
        else:
            xurl=url
        return xurl[xurl.find('/'):]

if __name__ == '__main__':
    Reporttype=sys.argv[1]
    App=ExReport()
    if Reporttype=='day':
        StartTime=time.strftime('%Y-%m-%d',time.localtime(time.time() - 24*60*60))+' 00:00:00'
        EndTime=time.strftime('%Y-%m-%d',time.localtime(time.time() - 24*60*60))+' 23:59:59'
        ReporttypeName="日报"
    elif  Reporttype=='week':
        Lastweek=App.GetLastweek(time.strftime('%Y%m%d',time.localtime(time.time())))
        StartTime=Lastweek[0]+' 00:00:00'
        EndTime=Lastweek[6]+' 23:59:59'
        ReporttypeName="周报"
    elif  Reporttype=='month':
        fireday=datetime.date(datetime.date.today().year,datetime.date.today().month-1,1)
        lastday=datetime.date(datetime.date.today().year,datetime.date.today().month,1)-datetime.timedelta(1)
        StartTime=fireday.strftime('%Y-%m-%d')+' 00:00:00'
        EndTime=lastday.strftime('%Y-%m-%d')+' 23:59:59'
        ReporttypeName="月报"
    elif  Reporttype=='year':
        fireday=datetime.date(datetime.date.today().year-1,1,1)
        lastday=datetime.date(datetime.date.today().year-1,12,31)
        StartTime=fireday.strftime('%Y-%m-%d')+' 00:00:00'
        EndTime=lastday.strftime('%Y-%m-%d')+' 23:59:59'
        ReporttypeName="年报"
    else:
        logging.error('input parment  error!')
        exit
    
    StarttimeStamp=App.time2stamp(StartTime)
    EndtimeStamp=App.time2stamp(EndTime)
    
    AllIDCId=App.GetAppIDCId(None)
    AllIDCName=App.GetAppIDCName(None)
    Sheet2=None
    _bigtitle="天涯应用监控报表"+'('+ReporttypeName+')'
    Downloadfilename='天涯应用监控报表'.decode('utf-8')+'（'.decode('utf-8')+ReporttypeName.decode('utf-8')+'）'.decode('utf-8')+str(time.strftime("%Y-%m-%d", time.localtime(StarttimeStamp)))+'~'+str(time.strftime("%Y-%m-%d", time.localtime(EndtimeStamp)))+'.xls'


    #获取记录各参数平均值
    Appdateobj=App.GetAppDateReport(AllIDCId,StarttimeStamp,EndtimeStamp)

    #获取记录不可用记录
    AppUnavailableobj=App.GetAppUnavailableReport(AllIDCId,StarttimeStamp,EndtimeStamp)
    _timedateobj=Appdateobj
    _navailableobj=AppUnavailableobj
        
    wb=App.ExcelReport(AllIDCId,_bigtitle,_timedateobj,_navailableobj,AllIDCName,ReporttypeName,Sheet2,StarttimeStamp,EndtimeStamp)
    #out excel file
    wb.save(EXCELPATH+'/'+Downloadfilename)
    os.system("/usr/local/bin/python /www/client/django/servermonitor/webmonitor/lib/SendMailMessage.py "+MAILTO+" 天涯应用监控报表\\(周报\\) 内容见附件\\(系统自动发送，无需回复\\)。 "+Downloadfilename.encode('utf-8'))
