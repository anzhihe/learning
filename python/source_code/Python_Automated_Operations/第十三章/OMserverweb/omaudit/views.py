# -*- coding: utf-8 -*-
#
#--------------------------------------------------------------------------
# views.py
#--------------------------------------------------------------------------
# auther:liutiansi
# Email:liutiansi@gmail.com
# update:2014-05-20
#
#---------------------------------------------------------------------------

import os,sys,time
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context
from django.template.loader import get_template
from omaudit.models import ServerHistory
from django.conf import settings
from django.template import RequestContext
from public.views import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.utils.log import logger


def index(request):
    res_template_dist={'system_name': settings.SYSTEM_NAME}
    return render_to_response('autoadmin/omaudit.html',res_template_dist)


"""
=事件任务前端加载方法
"""
def omaudit_run(request):

    if not 'LastID' in request.GET:
        LastID=""
    else:
        LastID=request.GET['LastID']
        
    if not 'hosts' in request.GET:
        Hosts=""
    else:
        Hosts=request.GET['hosts']

    ServerHistory_string=""
    host_array=target_host(Hosts,"IP").split(';')

    if LastID=="0":
        if Hosts=="":
            ServerHistoryObj = ServerHistory.objects \
            .order_by('-id')[:5]
        else:
            ServerHistoryObj = ServerHistory.objects \
            .filter(history_ip__in=host_array).order_by('-id')[:5]
    else:
        if Hosts=="":
            ServerHistoryObj = ServerHistory.objects \
            .filter(id__gt=LastID).order_by('-id')
        else:
            ServerHistoryObj = ServerHistory.objects \
            .filter(id__gt=LastID,history_ip__in=host_array).order_by('-id')
    lastid=""
    i=0
    for e in ServerHistoryObj:
        if i==0:
            lastid=e.id
        ServerHistory_string+="<font color=#cccccc>"+e.history_ip+ \
        "</font>&nbsp;&nbsp;\t"+ e.history_user+"&nbsp;&nbsp;\t"+str(e.db_datetime)+"\t # <font color=#ffffff>"+e.history_command+"</font>*"
        i+=1
    ServerHistory_string+="@@"+str(lastid)
    return HttpResponse(ServerHistory_string)
    

"""
=事件任务pull方法
"""
def omaudit_pull(request):
    if request.method == 'GET':

        if not request.GET.get('history_id', ''):
            return HttpResponse("history_id null")

        if not request.GET.get('history_ip', ''):
            return HttpResponse("history_ip null")
        
        if not request.GET.get('history_user', ''):
            return HttpResponse("history_user null")

        if not request.GET.get('history_datetime', ''):
            return HttpResponse("history_datetime null")
            
        if not request.GET.get('history_command', ''):
            return HttpResponse("history_command null")
            
        history_id=request.GET['history_id']
        history_ip=request.GET['history_ip']
        history_user=request.GET['history_user']
        history_datetime=request.GET['history_datetime']
        history_command=request.GET['history_command']

        historyobj = ServerHistory(history_id=history_id, \
            history_ip=history_ip, \
            history_user=history_user, \
            history_datetime=history_datetime, \
            history_command=history_command)
        try:
            historyobj.save()
        except Exception,e:
            return HttpResponse("入库失败，请与管理员联系！"+str(e))
        
        Response_result="OK"
        return HttpResponse(Response_result)
        
    else:
        return HttpResponse("非法提交！")