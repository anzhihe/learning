# -*- coding: utf-8 -*-
#
#--------------------------------------------------------------------------
# views.py
#--------------------------------------------------------------------------
# auther:Liutiansi
# Email:liutiansi@gmail.com
#Blog:http://blog.liuts.com
# update:2014-06-05
#
#---------------------------------------------------------------------------
import os,time
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context
from django.template.loader import get_template
from webmonitor.models import Hostinfo
from webmonitor.models import MonitorData
from django.conf import settings
from django.template import RequestContext
from publicclass.views import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from config import *
from django.core.servers.basehttp import FileWrapper
import mimetypes
"""
=输出404内容
"""
def head404(request):
    return HttpResponse("404")


"""
=图表及查询显示页
"""
def index(request):
    #获取应用清单
    Hostinfoobj = Hostinfo.objects.order_by('AppName')
    res_template_dist={'system_name': settings.SYSTEM_NAME}
    if  request.method == 'GET'  and 'AppId' in request.GET:
        ID=request.GET['AppId']
        Hostinforow=GetHostinfo(ID)[0]
        
        if not 'StartTime' in request.GET or request.GET['StartTime']=="":
            StartTime=int(str(time.time()).split('.')[0])-86400*3
            EndTime=int(str(time.time()).split('.')[0])
            UserFind="0"
            Graphrrd_normal(Hostinforow.ID,Hostinforow.URL,Hostinforow.AppName)    #custom graph rrd
        else:
            
            #自定义时间查询及生成rrd图表
            StartTime=time2stamp(request.GET['StartTime'])
            EndTime=time2stamp(request.GET['EndTime'])
            UserFind="1"
            #graphrrd user defind
            try:
                Graphrrd_custom(Hostinforow.ID,StartTime,EndTime,Hostinforow.URL,Hostinforow.AppName)    #custom graph rrd
            except Exception,e:
                InfoList=['系统提示：','图型绘制失败，原因('+str(e)+')','/webmonitor/']
                return render_to_response('webmonitor/info.html',{'DisplayInfo':InfoList })
        return render_to_response('webmonitor/main.html',{'Hostinfoobj': Hostinfoobj,'Hostinforow':Hostinforow,'StartTime':StartTime,'EndTime':EndTime,'UserFind':UserFind,'system_name': settings.SYSTEM_NAME})
    else:
        return render_to_response('webmonitor/main.html',{'Hostinfoobj': Hostinfoobj,'system_name': settings.SYSTEM_NAME})


"""
=监控列表
"""
def monitorlist(request):
    #获取应用清单
    if  request.method == 'GET'  and 'AppId' in request.GET and 'StartTime' in request.GET and 'EndTime' in request.GET:
        ID=request.GET['AppId']
        StartTime= request.GET['StartTime']
        EndTime= request.GET['EndTime']

        contact_list = MonitorData.objects.filter(FID=ID, DATETIME__gte=StartTime,DATETIME__lte=EndTime).order_by("-DATETIME")

        paginator = Paginator(contact_list, 15) # Show 10 contacts per page

        # Make sure page request is an int. If not, deliver first page.
        try:
            page = int(request.GET.get('page', '1'))
        except ValueError:
            page = 1

        # If page request (9999) is out of range, deliver last page of results.
        try:
            contacts = paginator.page(page)
        except (EmptyPage, InvalidPage):
            contacts = paginator.page(paginator.num_pages)
        return render_to_response('webmonitor/monitorlist.html',{'contacts': contacts,'ID':ID,'StartTime':StartTime,'EndTime':EndTime})
    else:
        return render_to_response('webmonitor/monitorlist.html',{})

"""
=添加应用页面
"""
def add(request):
    idc_str=""
    for (k,v) in  settings.IDC.items(): 
        idc_str+="<label for=\""+k+"\"><input name=\"idc\" type=\"checkbox\" value=\""+k+"\" id=\""+k+"\">"+v+"</label>\n"
    res_template_dist={'system_name': settings.SYSTEM_NAME,'IDC':idc_str}
    return render_to_response('webmonitor/HostAdd.html',res_template_dist)
    
"""
=应该添加方法
"""
def adddo(request):
    if request.method == 'GET':

        #检查表单-应用名称 
        if not request.GET.get('AppName', ''):
            return HttpResponse("应用名称 不能为空！")

        #检查表单-监控URL
        if not request.GET.get('HostDomain', ''):
            return HttpResponse("监控URL不能为空！")

        #检查探测点
        if len(request.GET.getlist('idc'))==0:
            return HttpResponse("探测点不能为空！")
            
        #检查表单-探测规则
        status=request.GET.getlist('status')
        responsechar=request.GET.get('responsechar')

        if  len(status)==0 and len(responsechar)==0:
            return HttpResponse("应用探测规则不能为空！")
        elif  len(status)!=0:
            GetAlarmconditions="200"
        else:
            GetAlarmconditions=responsechar

        AppName=request.GET['AppName']
        HostDomain=request.GET['HostDomain']
        hotice=request.GET['hotice']
        idc=request.GET.getlist('idc')


        for _idc in idc: 
            hostobj = Hostinfo(AppName=AppName, \
                URL=HostDomain, \
                IDC=_idc, \
                Alarmtype=hotice, \
                Alarmconditions=GetAlarmconditions)
            try:
                hostobj.save()
            except Exception,e:
                return HttpResponse("入库失败，请与管理员联系！"+str(e))
                break;
            hostobj=None

        try:
            if not os.path.isdir(settings.RRDPATH+'/'+GetURLdomain(HostDomain)):
                os.makedirs(settings.RRDPATH+'/'+GetURLdomain(HostDomain))
            
            if not os.path.isdir(settings.PNGPATH+'/'+GetURLdomain(HostDomain)):
                os.makedirs(settings.PNGPATH+'/'+GetURLdomain(HostDomain))

        except Exception,e:
            return HttpResponse("目录创建失败！"+str(e))
        
        try:
            create_rrd(str(HostDomain))
        except Exception,e:
            return HttpResponse("目录RRD文件失败！"+str(e))
        
        InfoList=['系统提示：','祝贺你，应用添加成功！请返回。','/webmonitor/add/']
        return render_to_response('webmonitor/info.html',{'DisplayInfo':InfoList })
        
    else:
        return HttpResponse("非法提交！")