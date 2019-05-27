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
from autoadmin.models import ServerFunCateg
from autoadmin.models import ServerAppCateg
from autoadmin.models import ServerList
from autoadmin.models import ModuleList
from django.conf import settings
from django.template import RequestContext
from public.views import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.utils.log import logger

"""
=OMserver main page
"""
def index(request):
    res_template_dist={'system_name': settings.SYSTEM_NAME}
    return render_to_response('autoadmin/main.html',res_template_dist)
    
"""
=Add module page
"""
def module_add(request):
    res_template_dist={'system_name': settings.SYSTEM_NAME}
    return render_to_response('autoadmin/module_add.html',res_template_dist)


"""
=Return server function categ
"""
def server_fun_categ(request):
    categ_id="-1"
    categ_name=u"<-请选择功能类别->"
    
    ServerFunObj = ServerFunCateg.objects.order_by('id')
    for e in ServerFunObj:
        categ_id+=","+str(e.id)
        categ_name+=","+e.server_categ_name
    fun_categ_string=categ_name+"|"+categ_id
    return HttpResponse(fun_categ_string)


"""
=Return server app categ
"""
def server_app_categ(request):
    categ_id="-1"
    categ_name=u"<-请选择应用类别->"

    if not 'fun_categId' in request.GET:
        fun_categId=""
    else:
        fun_categId=request.GET['fun_categId']
            
    ServerAppObj = ServerAppCateg.objects.filter(server_categ_id=fun_categId)
    for e in ServerAppObj:
        categ_id+=","+str(e.id)
        categ_name+=","+e.app_categ_name
    app_categ_string=categ_name+"|"+categ_id
    return HttpResponse(app_categ_string)


"""
=Return server IP list
"""
def server_list(request):
    ip=""
    ip_hostname=""

    if not 'app_categId' in request.GET:
        app_categId=""
    else:
        app_categId=request.GET['app_categId']
            
    ServerListObj = ServerList.objects.filter(server_app_id=app_categId)
    for e in ServerListObj:
        ip+=","+e.server_lip
        ip_hostname+=","+e.server_lip+"*"+e.server_name
    server_list_string=ip[1:]+"|"+ip_hostname[1:]
    return HttpResponse(server_list_string)


"""
=Return module list
"""
def module_list(request):
    module_id="-1"
    module_name=u"请选择功能模块..."
    
    ModuleObj = ModuleList.objects.order_by('id')
    for e in ModuleObj:
        module_id+=","+str(e.id)
        module_name+=","+e.module_name
    module_list_string=module_name+"|"+module_id
    return HttpResponse(module_list_string)


"""
=Return module info
"""
def module_info(request):

    if not 'Module_Id' in request.GET:
        Module_Id=""
    else:
        Module_Id=request.GET['Module_Id']
        
    ModuleObj = ModuleList.objects.get(id=Module_Id)
    module_info_string=str(ModuleObj.id)+"@@"+ModuleObj.module_name+"@@"+ModuleObj.module_caption+"@@"+ModuleObj.module_extend

    return HttpResponse(module_info_string)


"""
=Run module
"""
def module_run(request):
    import rpyc
    from cPickle import loads
    put_string=""
    
    if not 'ModuleID' in request.GET:
        Module_Id=""
    else:
        Module_Id=request.GET['ModuleID']
        put_string+=Module_Id+"@@"

    if not 'hosts' in request.GET:
        Hosts=""
    else:
        Hosts=request.GET['hosts']
        put_string+=Hosts+"@@"

    if not 'sys_param_1' in request.GET:
        Sys_param_1=""
    else:
        Sys_param_1=request.GET['sys_param_1']
        put_string+=Sys_param_1+"@@"

    if not 'sys_param_2' in request.GET:
        Sys_param_2=""
    else:
        Sys_param_2=request.GET['sys_param_2']
        put_string+=Sys_param_2+"@@"

    try:
        conn=rpyc.connect('192.168.1.20',11511)
        conn.root.login('OMuser','KJS23o4ij09gHF734iuhsdfhkGYSihoiwhj38u4h')
    except Exception,e:
        logger.error('connect rpyc server error:'+str(e))
        return HttpResponse('connect rpyc server error:'+str(e))

    put_string=tencode(put_string,settings.SECRET_KEY)
    OPresult=tdecode(conn.root.Runcommands(put_string),settings.SECRET_KEY)
    return HttpResponse(OPresult)

"""
=应该添加方法
"""
def module_add_post(request):
    if request.method == 'GET':

        #检查表单-应用名称 
        if not request.GET.get('module_name', ''):
            return HttpResponse("模块名称不能为空！")

        #检查表单-监控URL
        if not request.GET.get('module_caption', ''):
            return HttpResponse("模块功能描述不能为空！")
        

        module_name=request.GET['module_name']
        module_caption=request.GET['module_caption']
        module_extend=request.GET['module_extend']

        moduleobj = ModuleList(module_name=module_name, \
            module_caption=module_caption, \
            module_extend=module_extend)
        try:
            moduleobj.save()
            #lastId = moduleobj.objects.order_by('-pk')[0]
            lastId = ModuleList.objects.latest('id')
        except Exception,e:
            return HttpResponse("入库失败，请与管理员联系！"+str(e))
        
        InfoList="祝贺你，模块前端添加成功，模块ID为："+str(lastId.pk)+"，下一步请在服务器端编写模块逻辑！"
        return HttpResponse(InfoList)
        
    else:
        return HttpResponse("非法提交！")