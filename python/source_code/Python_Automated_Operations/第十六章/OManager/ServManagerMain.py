# -*- coding: utf-8 -*-
import os
import sys
import wx
from wx import xrc
import re
import time
import wx.aui
import wx.grid
from wx.lib.stattext import GenStaticText as StaticText
import wx.lib.flatnotebook as fnb
from wx.lib.statbmp  import GenStaticBitmap as StaticBitmap
from wx.lib.wordwrap import wordwrap
import ConfigParser
import webbrowser
import string
import urllib
import socket
from urllib import urlopen
import wx.lib.buttons

from ServerList import ServerClassList
from DBclass import sysbash
from ServerFunction import ServerFunction


#----------------------------------------------------------------------------#
# 模块展示窗口                                                   	         #
#----------------------------------------------------------------------------#
# Frame为主窗体，                                                            #
#                                			          	                     #
#                                                                            #
#                                                                            #
#-----------------------------------------------------------------------------
class DisplayModuleFrame(wx.Frame):
    def __init__(
            self, parent, ID, title, pos,
            size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE,CurrMoudelName=""
            ):
        wx.Frame.__init__(self, parent, ID, title, pos, size, style,CurrMoudelName)
        
        #功能类对象
        FunApp=ServerFunction()

        #模ID
        self.ModuleID="0"
        
        #操作参数符对象
        self.Parameter1=""
        self.Parameter2=""
        
        #操作参数值
        self.Parameter1_value=""
        self.Parameter2_value=""
        
        
        #返回给主窗口变量，窗口各控件参数串
        self.ModulelStr=""        
        
        #窗体属性设置
        self.SetIcon(wx.Icon(sys.path[0]+'/img/APP.ico',wx.BITMAP_TYPE_ICO))
        self.CentreOnScreen(wx.BOTH)
        self.SetBackgroundColour("#DBEAF0")
        
        
        #读取XRC模块文件
        self.res = xrc.XmlResource(sys.path[0]+'/Module/'+str(CurrMoudelName))
        panel = self.res.LoadPanel(self, "panel")
        
        
        #获取XRC模块控件及值
        self.ModuleID=FunApp.ModuleParameter(CurrMoudelName,'id')
        
        #获取第一个参数控件值
        try:
            self.Parameter1 = xrc.XRCCTRL(panel, 'Parameter1_object_id')
        except Exception,e:
            pass

        #获取第二个参数控件值
        try:
            self.Parameter2 = xrc.XRCCTRL(panel, 'Parameter2_object_id')
        except Exception,e:
            pass
        
    #返回"模块ID,参数1，参数2"
    def GetTxtValue(self):
        self.ModulelStr=str(self.ModuleID)
        try:
            if self.Parameter1.GetClassName()=="wxSpinCtrl":
                self.Parameter1_value=self.Parameter1.GetValue()
            elif self.Parameter1.GetClassName()=="wxListBox":
                self.Parameter1_value=self.Parameter1.GetStringSelection()
            self.ModulelStr+=","+str(self.Parameter1_value)
        except Exception,e:
            pass

        try:
            if self.Parameter2.GetClassName()=="wxSpinCtrl":
                self.Parameter2_value=self.Parameter2.GetValue()
            elif self.Parameter2.GetClassName()=="wxListBox":
                self.Parameter2_value=self.Parameter2.GetStringSelection()
            self.ModulelStr+=","+str(self.Parameter2_value)
        except Exception,e:
            pass

        return self.ModulelStr

    def OnCloseWindow(self):
        self.Destroy()


#----------------------------------------------------------------------------#
# 系统托盘类                                                     	         #
#----------------------------------------------------------------------------#
# 系统托盘类                                                                 #
#                                			          	                     #
#                                                                            #
#                                                                            #
#-----------------------------------------------------------------------------
class TaskBarIcon(wx.TaskBarIcon):
    ID_Hello = wx.NewId()

    def __init__(self, frame):

        wx.TaskBarIcon.__init__(self)
        self.frame = frame
        self.SetIcon(wx.Icon(name=sys.path[0]+'/img/Loading.ico', type=wx.BITMAP_TYPE_ICO), u'OManager服务器管理平台')
        self.Bind(wx.EVT_MENU, self.OnHello, id=self.ID_Hello)
        self.Bind(wx.EVT_TASKBAR_LEFT_DCLICK, self.OnTaskBarLeftDClick)


    def OnTaskBarLeftDClick(self, event):
        if self.frame.IsIconized():
           self.frame.Iconize(False)
        if not self.frame.IsShown():
           self.frame.Show(True)
        self.frame.Raise()

    def OnHello(self, event):
        wx.MessageBox(u'运维进行时 CopyRight 2008-2014\n\n作者：刘天斯', u'版权信息')

        
    def CreatePopupMenu(self):
        menu = wx.Menu()
        menu.Append(self.ID_Hello, u'版权信息')
        return menu

#----------------------------------------------------------------------------#
# 系统升级窗口                                                   	         #
#----------------------------------------------------------------------------#
# Frame为主窗体，                                                            #
#                                			          	                     #
#                                                                            #
#                                                                            #
#-----------------------------------------------------------------------------
class UpdateFrame(wx.Frame):
    def __init__(
            self, parent, ID, title, pos=wx.DefaultPosition,
            size=wx.DefaultSize, style=wx.STAY_ON_TOP,lastversion=''
            ):
        
        wx.Frame.__init__(self, parent, ID, title, pos, size, style)
        self.SetIcon(wx.Icon(sys.path[0]+'/img/Save.ico',wx.BITMAP_TYPE_ICO))
        self.CentreOnScreen(wx.BOTH)
        self.SetBackgroundColour("#DBEAF0")
        
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(sys.path[0]+'/data/config.ini')
        
        #初始化变量
        self.updateURL=self.cf.get("system","upgrade_url")
        
        self.lastversion=lastversion
        
        #创建面板及静态文本
        panel = wx.Panel(self, -1,pos=wx.Point(0, 0),size=wx.Size(392, 216),style=wx.TAB_TRAVERSAL)
        self.ConnStaticText=StaticText(panel, -1, u"点击[更新]按钮开始升级系统数据包.",(80, 25),(195, 20))

        png_logo = wx.Image(sys.path[0]+'/img/Next.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        StaticBitmap(self, -1, png_logo, (25, 20), (png_logo.GetWidth(), png_logo.GetHeight()))

        #创建button，应用self.OnCloseMe(wx.EVT_BUTTON)关闭窗口
        self.button = wx.Button(panel, -1, u"更新",(150, 60))
        #button.SetPosition(50, 20)
 
        #frame onload event
        #self.Bind(wx.EVT_SHOW, self.load_data,button)
        
        #frame close
        self.Bind(wx.EVT_BUTTON, self.load_data, self.button)
   
        
    def OnCloseWindow(self, event):
        self.Destroy()

    
    #窗口onload方法    
    def load_data(self,event):
        try:

            if self.button.GetLabel()==u"关闭":
                self.Destroy()

                #下载描述文件
            url=self.updateURL+"/updateMS.xml"
            localfile=sys.path[0]+'/tmp/updateMS.xml'
            if not self.download(url,localfile):
                return
        except Exception,e:
            wx.MessageBox(u"更新描述文件下载失败，请与管理员联系liutiansi@gmail.com,错误0："+str(e),u"OManager服务器管理平台：",style=wx.OK|wx.ICON_ERROR)
            self.Destroy()
            return

        try:
            import xml.etree.ElementTree as ET
            update_tree = ET.parse(sys.path[0]+'/tmp/updateMS.xml')
            up_doc = update_tree.getroot()
        except Exception,e:
            wx.MessageBox(u"导入更新包出错，请重启应用后再升级。",u"OManager服务器管理平台：",style=wx.OK|wx.ICON_ERROR)
            self.Destroy()
            return
        
        #遍历描述文件
        try:
            upgrade_count=0
            for cur_child in up_doc:
                upgrade_count+=1
                url=self.updateURL+cur_child[1].text
                localfile=sys.path[0]+'/'+cur_child[0].text
                if self.download(url,localfile)==False:
                    break

                
            #更新升级版本号
            self.cf.set("system", "Upversion", self.lastversion)
            self.cf.write(open(sys.path[0]+'/data/config.ini', "w"))
            self.ConnStaticText.SetLabel(u"成功更新"+str(upgrade_count)+"个数据包，重启程序生效。".decode('utf-8'))
            self.button.SetLabel(u"关闭")
        except Exception,e:
            wx.MessageBox(u"系统文件下载失败，请与管理员联系liutiansi@gmail.com,错误1："+str(e),u"OManager服务器管理平台：",style=wx.OK|wx.ICON_ERROR)
            self.Destroy()
            return
        finally:
            pass

        event.Skip()
     
    #==下载方法 ==
    def download(self,url,filename):
        try:
            lib=urllib.urlopen(url).read()
            if len(str(lib).strip())==0:
                wx.MessageBox(u"文件下载失败，请与管理员联系liutiansi@gmail.com,错误3：",u"OManager服务器管理平台：",style=wx.OK|wx.ICON_ERROR)
            f=open(filename,"wb")
            f.write(lib)
            f.close()
            return 1
        except Exception,e:
            wx.MessageBox(u"文件下载失败，请与管理员联系liutiansi@gmail.com,错误2："+str(e),u"OManager服务器管理平台：",style=wx.OK|wx.ICON_ERROR)
            return
            
#----------------------------------------------------------------------------#
# Name:        ServManagerMain.py                                            #
# Purpose:     Management App Server(by socket)                              #
# Author:      Liutiansi                                                     #
# Email:       liutiansi@gamil.com                                           #
# Created:     2008/10/17                                                    #
# Copyright:   (c) 2014                                                      #
#-----------------------------------------------------------------------------



#----------------------------------------------------------------------------#
# 程序主体类ServManageFrame                                          	     #
#----------------------------------------------------------------------------#
# Frame为主窗体，aui.AuiManager实现多窗口的窗口;                             #
# 元素包括菜单、工具栏等。            			          	                 #
#                                                                            #
#                                                                            #
#-----------------------------------------------------------------------------
class ServManageFrame(wx.Frame):
    def __init__(self, parent, title):
        if wx.GetApp().username==None:
             self.Destroy()
        self.CurrentAdmin=wx.GetApp().username
        self.CurrentPrivileges=string.split(wx.GetApp().userInfo[0][1],',')

        #-------------------------将登录写入日志----------------
        Intologs=sysbash()
        Intologs.Addsyslogs(self.CurrentAdmin,u"登录系统    IP:"+socket.gethostbyname(socket.gethostname()))

        #===调用托盘类===
        self.taskBarIcon = TaskBarIcon(self)
        
        #===变量初始化===
        
        #定义导入、导出文件对话框扩展名；
        self.FileexList = "Txt File (*.txt)|*.txt|Html File (*.html)|*.html|CSV (*.csv)|*.csv|All files (*.*)|*.*"
        
        #读取配置文件
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(sys.path[0]+'/data/config.ini')
        self._syswidth= self.cf.get("system","Width")
        self._sysheight= self.cf.get("system","Height")
        self._timeout=self.cf.get("system","Timeout")
        self._ip=self.cf.get("system","IP")
        self._port=self.cf.get("system","Port")
        self._max_servers=self.cf.get("system","max_servers")
        self._secret_key=self.cf.get("system","secret_key")
        self._sysversion= self.cf.get("system","Version")
        self._sysUpversion= self.cf.get("system","Upversion")
        self._upgrade_url= self.cf.get("system","upgrade_url")
        
        self._db_ip= self.cf.get("db","db_ip")
        self._db_user= self.cf.get("db","db_user")
        self._db_pass= self.cf.get("db","db_pass")
        self._db_name= self.cf.get("db","db_name")
        
        #关注清单参数
        self.NoticeList = [u'邮件通知',u'短信通知']
        self.NoticeIp = [u'外网',u'内网']  

        #关注清单服务器limit key.
        self.lastquery=0
        
        #服务器列表列表
        self.Serverlist_array=[]
        
        self._newPageCounter=1
        
        # ---初始窗体---
        wx.Frame.__init__(self, parent, -1, title+str(self._sysversion), pos=(0, 0), size=(int(self._syswidth), int(self._sysheight)))
        self.SetIcon(wx.Icon(sys.path[0]+'/img/imac.ico',wx.BITMAP_TYPE_ICO))
        self.CentreOnScreen(wx.BOTH)
        self.SetMinSize(wx.Size(400, 300))
            
        # ---调用AuiManager控件实现多窗口---
        mgr = wx.aui.AuiManager()
        mgr.SetManagedWindow(self)
        self.mgr = mgr

        # ---创建菜单栏---
        mb = wx.MenuBar()
        
        # 定义第一列［文件］菜单
        file_menu = wx.Menu()
        mb.Append(file_menu, u"文件(&F)")
        savelog=wx.MenuItem(file_menu,21, u"保存记录\tCtrl-S",u"保存操作记录")
        savelog.SetBitmap(wx.Bitmap(sys.path[0]+'/img/Save_s.png'))
        file_menu.AppendItem(savelog)

        clearlog=wx.MenuItem(file_menu,25, u"清空记录\tCtrl-L",u"清空操作记录")
        clearlog.SetBitmap(wx.Bitmap(sys.path[0]+'/img/DB.png'))
        file_menu.AppendItem(clearlog)
        
        systemquit=wx.MenuItem(file_menu,wx.ID_EXIT, u"退    出\tAlt-X",u"退出本系统")
        systemquit.SetBitmap(wx.Bitmap(sys.path[0]+'/img/Exit_s.png'))
        file_menu.AppendItem(systemquit)        
        
        # 定义第二列［视图］菜单
        self.view_menu = wx.Menu()
        mb.Append(self.view_menu, u"视图(&E)")
        self.view_menu.Append(22, u"服务器类别",u"显示/关闭服务器类别",wx.ITEM_CHECK)
        self.view_menu.Append(23, u"服务器列表",u"显示/关闭服务器列表",wx.ITEM_CHECK)
        self.view_menu.Append(24, u"记录窗口",u"显示/关闭记录窗口",wx.ITEM_CHECK)
        self.view_menu.Check(22, True)
        self.view_menu.Check(23, True)
        self.view_menu.Check(24, True)
        
        # 定义第三列［功能］菜单
        self.function_menu = wx.Menu()
        mb.Append(self.function_menu, u"功能(&D)")

        bashmenu = wx.Menu()
        appmenu = wx.Menu()
        dbmenu = wx.Menu()
        servicemenu = wx.Menu()
        middlemenu = wx.Menu()

        #模块列表
        self.Moduledetail=os.listdir(sys.path[0]+'/Module')
        
        for file_info in self.Moduledetail:
            file_array=string.split(file_info,'_')
            if file_info[0:3]=="bas":
                bashmenu.Append(int(file_array[1]),file_array[2],file_array[2])
            elif file_info[0:3]=="app":
                appmenu.Append(int(file_array[1]),file_array[2],file_array[2])
            elif file_info[0:3]=="dba":
                dbmenu.Append(int(file_array[1]),file_array[2],file_array[2])
            elif file_info[0:3]=="ser":
                servicemenu.Append(int(file_array[1]),file_array[2],file_array[2])
            elif file_info[0:3]=="mid":
                middlemenu.Append(int(file_array[1]),file_array[2],file_array[2])
            self.Bind(wx.EVT_MENU, self.OnOpenOptapp, id=int(file_array[1]))
                
        self.function_menu.AppendMenu(31, u"基本功能",bashmenu)
        self.function_menu.AppendMenu(32, u"应用功能",appmenu)
        self.function_menu.AppendMenu(33, u"数据库功能",dbmenu)
        self.function_menu.AppendMenu(34, u"后台服务功能",servicemenu)
        self.function_menu.AppendMenu(36, u"中间件功能",middlemenu)
        self.function_menu.Append(35, u"系统配置",u"系统配置功能")
        
        
        help_menu = wx.Menu()
      
        mb.Append(help_menu, u"帮助(&H)")
        systemabout=wx.MenuItem(help_menu,41, u"关 于\tCtrl-B",u"关于本系统")
        systemabout.SetBitmap(wx.Bitmap(sys.path[0]+'/img/Info_s.png'))
        help_menu.AppendItem(systemabout)

        systemhelp=wx.MenuItem(help_menu,42, u"帮 助\tCtrl-H",u"系统帮助信息")
        systemhelp.SetBitmap(wx.Bitmap(sys.path[0]+'/img/help_s.png'))
        help_menu.AppendItem(systemhelp)
        
        # 邦定菜单
        self.SetMenuBar(mb)


        # ---创建工具栏---
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.toolbar = wx.ToolBar(self, -1, style= wx.TB_HORIZONTAL |wx.NO_BORDER | wx.TB_FLAT | wx.TB_TEXT) 
        self.toolbar.AddSimpleTool(1, wx.Image(sys.path[0]+'/img/home.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap(),u"欢迎窗口",u"欢迎窗口")
        self.toolbar.AddSimpleTool(2, wx.Image(sys.path[0]+'/img/clean.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap(),u"清空记录",u"清空记录")
        self.toolbar.AddSimpleTool(3, wx.Image(sys.path[0]+'/img/logsave.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap(),u"保存记录",u"保存记录")
        self.toolbar.AddSimpleTool(5, wx.Image(sys.path[0]+'/img/play.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap(), u"运行模块",u"运行选择的模块")
        self.toolbar.AddSimpleTool(6, wx.Image(sys.path[0]+'/img/run.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap(), u"系统配置",u"系统相关配置")
        self.toolbar.AddSimpleTool(7, wx.Image(sys.path[0]+'/img/Save.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap(), u"系统升级",u"系统升级")
        self.toolbar.AddSimpleTool(8, wx.Image(sys.path[0]+'/img/Back.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap(), u"向左标签",u"向左标签")
        self.toolbar.AddSimpleTool(9, wx.Image(sys.path[0]+'/img/forward.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap(), u"向右标签",u"向右标签")
        self.toolbar.AddSimpleTool(14, wx.Image(sys.path[0]+'/img/hide.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap(), u"隐藏窗口",u"隐藏窗口")
        
        #添加一个分隔符   
        self.toolbar.AddSeparator()
        self.toolbar.AddSimpleTool(10, wx.Image(sys.path[0]+'/img/Info.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap(),u"关于",u"关于本系统")
        self.toolbar.AddSimpleTool(13, wx.Image(sys.path[0]+'/img/help.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap(),u"帮助",u"关于本系统的帮助信息")
        self.toolbar.AddSimpleTool(11, wx.Image(sys.path[0]+'/img/Exit.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap(),u"退出",u"退出本系统")
        tsize = (48, 48)
        
        #以下两个方法注意先后顺序，不然会出现所有图标粘到第一个图标上。
        self.toolbar.SetToolBitmapSize(tsize)        
        self.toolbar.Realize()
        vbox.Add(self.toolbar, 10, wx.EXPAND)    
   
        self.SetSizer(vbox)
        
 
        #右下角时间
        self.timer = wx.Timer(self,id=51)
        self.Bind(wx.EVT_TIMER,self.OnNotify,self.timer)
        self.timer.Start(1000)

        #Update check timeer
        self.timer_p = wx.Timer(self,id=52)
        self.Bind(wx.EVT_TIMER,self.OnUpdatecheck,self.timer_p)       
        
        #每隔30分钟检测是否有新版本。
        self.timer_p.Start(1800000)
        
        
        # ---创建状态栏(3栏)---
        self.statusbar = self.CreateStatusBar(3, wx.ST_SIZEGRIP)
        #定义三个栏的宽度比例
        self.statusbar.SetStatusWidths([-4, -16,-4])
        self.statusbar.SetStatusText(u"就绪", 0)
        
        
        self.statusbar.SetStatusText(u"作者：刘天斯                操作员："+str(self.CurrentAdmin), 1)
        
        t = time.localtime(time.time())
        st = time.strftime("%Y-%m-%d %H:%M:%S", t)
        self.statusbar.SetStatusText("  "+str(st),2)
        

        # ---创建消息框---
        TextCtrltext = ""
        self.SysMessaegText=wx.TextCtrl(self,-1, TextCtrltext, wx.Point(0, 0), wx.Size(150, 98),wx.NO_BORDER | wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_RICH2)
        self.SysMessaegText.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL,False, u'\u5b8b\u4f53'))
        self.SysMessaegText.SetForegroundColour(wx.Colour(255, 255, 255))
        self.SysMessaegText.SetBackgroundColour(wx.Colour(0, 0, 0))


        # ---创建服务器类别列表---
        self.tree = wx.TreeCtrl(self,-1,wx.DefaultPosition, wx.DefaultSize,wx.TR_HAS_BUTTONS)


        #---创建图像对象---
        isz = (16,16)
        il = wx.ImageList(isz[0], isz[1])        
        self.fldridx     = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER,wx.ART_OTHER, isz))
        self.fldropenidx = il.Add(wx.ArtProvider_GetBitmap(wx.ART_FILE_OPEN,wx.ART_OTHER, isz))
        self.fileidx     = il.Add(wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, isz))
        self.tree.SetImageList(il)
        self.il = il
        
        # Add a root node
        GetServerListApp=ServerClassList()
        root = self.tree.AddRoot(u"选择类别")
        
        #处理值班用户的权限
        if self.CurrentPrivileges[0]=="zhiban":
            self.toolbar.EnableTool(5,False)
            self.toolbar.EnableTool(12,False)
            mb.EnableTop(2, False)
            tree=[]
        else:
            tree = GetServerListApp.Resurn_list(self.CurrentPrivileges)
        self.AddTreeNodes(root, tree)
        self.tree.SetItemImage(root, self.fldridx, wx.TreeItemIcon_Normal)
        self.tree.SetItemImage(root, self.fldropenidx, wx.TreeItemIcon_Expanded)
        # Expand the first level
        self.tree.Expand(root)
        
        
        
        # ---创建服务器列表---
        self.ServerList = wx.ListBox(self,-1,choices=self.Serverlist_array,name='ServerList',size=wx.Size(200, 500), style=wx.LB_EXTENDED)
        self.SysMessaegText.WriteText(u"============================欢迎使用OManager服务器管理平台===============================")
        self.SysMessaegText.SetInsertionPoint(0)

       
        # ---主欢迎窗口---
        welcome_jpg=wx.Image(sys.path[0]+'/img/welcome.jpg', wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
        self.SysWelcome=wx.StaticBitmap(self, -1, welcome_jpg,(0, 0), (welcome_jpg.GetWidth(), welcome_jpg.GetHeight()))
    
        
         # ---主窗体TAB控件-欢迎窗口---
        self.MainFlatNotebook = fnb.FlatNotebook(self, -1, style=fnb.FNB_BOTTOM|fnb.FNB_VC8 | fnb.FNB_DROPDOWN_TABS_LIST | fnb.FNB_TABS_BORDER_SIMPLE | fnb.FNB_BACKGROUND_GRADIENT)
        self.MainFlatNotebook.SetNonActiveTabTextColour("#006699")
        self.MainFlatNotebook.SetActiveTabColour("#ffffff")
        self.MainFlatNotebook.SetActiveTabTextColour("#006699")
        self.MainFlatNotebook.AddPage(self.SysWelcome, u"欢迎窗口")
        
        
        # ---添加self.tree(服务器类别)控件到面板---
        self.mgr.AddPane(self.tree, wx.aui.AuiPaneInfo().Name("ServerClass_Pane").Caption(u"服务器类别").
                Left().Layer(1).Position(1).CloseButton(True).MaximizeButton(True))
        
        
        # ---添加self.ServerList(服务器列表)控件到面板---
        self.mgr.AddPane(self.ServerList, wx.aui.AuiPaneInfo().Name("ServerList_Pane").Caption(u"服务器列表").
                Left().Layer(1).Position(1).CloseButton(True).MaximizeButton(True))
        
        
        # ---添加self.MainFlatNotebook(主界面，默认为webcome)控件到面板---
        self.mgr.AddPane(self.MainFlatNotebook, wx.aui.AuiPaneInfo().Name("main").CenterPane())


        # ---添加self.SysMessaegText(输出消息框)控件到面板---
        self.mgr.AddPane(self.SysMessaegText, wx.aui.AuiPaneInfo().
                          Name("System_messages").Caption(u"输出消息").
                          Bottom().Layer(1).Position(1).CloseButton(True).MaximizeButton(True))
        
        
        # ---添加self.toolbar(工具条)控件到面板---
        self.mgr.AddPane(self.toolbar, wx.aui.AuiPaneInfo().
                          Name("toolbar").Caption("Big Toolbar").
                          ToolbarPane().Top().
                          LeftDockable(False).RightDockable(False))
        
        
        # ---刷新mgr面板---
        self.mgr.Update()

        #---------------------------菜单栏邦定事件----------------------------
        #quit
        self.Bind(wx.EVT_TOOL, self.OnExit, id=wx.ID_EXIT)   
        
        #保存记录
        self.Bind(wx.EVT_MENU, self.OnSaveLog, id=21)
        
        #清空记录
        self.Bind(wx.EVT_MENU, self.OnClearLog, id=25)
        
        #视图事件
        self.Bind(wx.EVT_MENU, self.OnCloseOpenpane, id=22)
        self.Bind(wx.EVT_MENU, self.OnCloseOpenpane, id=23)
        self.Bind(wx.EVT_MENU, self.OnCloseOpenpane, id=24)
        
        #功能菜单
        self.Bind(wx.EVT_MENU, self.OnOpenConapp, id=35)
        
        #about
        self.Bind(wx.EVT_MENU, self.OnOpenSystemAbout,id=41)
        
        #help
        self.Bind(wx.EVT_MENU, self.OnOpenSystemHelp,id=42)
        
        #---------------------------工具栏邦定事件----------------------------
        #welcome按钮事件
        wx.EVT_TOOL(self,1, self.OnOpenwelcome)

        #清空记录按钮事件
        wx.EVT_TOOL(self,2, self.OnClearLog)
        
        #保存记录按钮事件
        wx.EVT_TOOL(self,3, self.OnSaveLog)
        
        #运行模块按钮事件
        self.toolbar.Bind(wx.EVT_LEFT_DOWN,self.OnOpenRunappMessage)
        wx.EVT_TOOL(self,5, self.OnOpenRunapp)

        #系统配置按钮事件
        wx.EVT_TOOL(self,6, self.OnOpenConapp)

        #系统升级按钮事件
        wx.EVT_TOOL(self,7, self.OnOpenSystemUpdate)
        
        #向左标签按钮事件
        wx.EVT_TOOL(self,8, self.OnOpenSystemLeft)
        
        #向右标签按钮事件
        wx.EVT_TOOL(self,9, self.OnOpenSystemRight)
        
        #关于事件
        wx.EVT_TOOL(self,10, self.OnOpenSystemAbout)        

        #退出事件
        wx.EVT_TOOL(self,11, self.OnExit)
       
        #帮助
        wx.EVT_TOOL(self,13, self.OnOpenSystemHelp)        

        #隐藏窗口
        wx.EVT_TOOL(self,14, self.OnHide) 
        
        #服务器类别树控件改变事件
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged, self.tree)
        
        #TAB窗口关闭事件
        self.MainFlatNotebook.Bind(fnb.EVT_FLATNOTEBOOK_PAGE_CLOSING,self.OnStopclose)
        
       
        #消息框单击事件
        self.SysMessaegText.Bind(wx.EVT_LEFT_UP, self.OnTextCtrlTopCurr)
        
        #aui面板关闭事件
        self.Bind(wx.aui.EVT_AUI_PANE_CLOSE, self.OnPaneClose)
        
        #最小化窗口变托盘
        self.Bind(wx.EVT_ICONIZE, self.OnIconfiy)


#----------------------------------------------------------------------------#
# 获取当前选择服务器信息                                                     # 
#----------------------------------------------------------------------------#
# return_type=lip：返回lip;                                                  #
# return_type=os：返回os;     	          	                                 #
# return_type=app：返回app;                                                  #
# return_type=locate：返回locate;                                            #
# return_type=option: 返回option;                                            #
# return_type=serverserial: 返回主机名                                       #
# return_type=serverserial_ip :返回主机名+IP，'192.168.1.20*sn2013-08-020'   #
# datatype=1 :返回str                                                        #
# datetype=0 :返回列表[]                                                     #
# servernum :服务器的最大数                                                  #
#----------------------------------------------------------------------------#

    def OnGetSelectServerinfo(self,returntype,datatype=1,servernum=1):
            Funapp=ServerFunction()
        
            #返回字符串类型
            datatype1=""
            
            #返回列表类型
            datatype0=[]
            
            if len(self.ServerList.GetSelections())==0:
                wx.MessageBox(u"服务器地址不能为空，请在左侧窗口选择。",u"OManager服务器管理平台：",style=wx.OK|wx.ICON_ERROR)
                return
            else:
                if self.ServerList.GetSelections().__len__()>servernum:
                    wx.MessageBox(u"选择服务器的数量超过模块设定值"+str(servernum)+u"，请重新选择。",u"OManager服务器管理平台：",style=wx.OK|wx.ICON_ERROR)
                    return                    
                for i in self.ServerList.GetSelections():
                    IP=self.ServerList.GetString(i)
                    if datatype==1:
                        datatype1+=str(Funapp.GetServerinfo(IP,returntype)).strip()+','
                    elif datatype==0:
                        datatype0.append[Funapp.GetServerinfo(IP,returntype)]
                if datatype==1:    
                    return datatype1[0:-1]
                else:
                    return datatype0


#----------------------------------------------------------------------------#
# 帮助                                                                       #
#----------------------------------------------------------------------------#
#                                                                            #
#             		                         	          	                 #
#                                                                            #
#                                                                            #
#----------------------------------------------------------------------------# 
    def OnOpenSystemHelp(self,event):
        wx.MessageBox(u"有时间再补上:)",u"OManager服务器管理平台：",style=wx.OK|wx.ICON_EXCLAMATION)
        event.Skip()

#----------------------------------------------------------------------------#
# 左击工具栏显示消息                                                         #
#----------------------------------------------------------------------------#
#                                                                            #
#             		                         	          	                 #
#                                                                            #
#                                                                            #
#----------------------------------------------------------------------------#
    def OnOpenRunappMessage(self,event):
        self.OnWriteMessageBox(u"系统正在加载中...")
        event.Skip()
        
        
#----------------------------------------------------------------------------#
# 检测有无新升级包                                                           #
#----------------------------------------------------------------------------#
#                                                                            #
#             		                         	          	                 #
#                                                                            #
#                                                                            #
#----------------------------------------------------------------------------#
    def OnUpdatecheck(self,event):
        #创建数据库实例，获取最新版本号
        GetUpdateNum=sysbash()       
        verdata=GetUpdateNum.GetUpdateVersion()
        
        #重新读取配置文件，方便比较升级版本号
        self.cf.read(sys.path[0]+'/data/config.ini')
        self._sysUpversion= self.cf.get("system","Upversion")
        
        if str(verdata[0][0])>str(self._sysUpversion):
            self.OnWriteMessageBox(u"系统发现有新版本下载，请点击[系统升级]按钮进行升级。")
            yndlg = wx.MessageDialog(None, u'系统发现有新版本供下载，现在开始升级吗？',u'提示信息：', wx.YES_NO | wx.ICON_QUESTION)
            if yndlg.ShowModal()==wx.ID_YES:
                self.OnOpenSystemUpdate(7)
        event.Skip()
        

#----------------------------------------------------------------------------#
# 显示/关闭aui面板                                                           #
#----------------------------------------------------------------------------#
# 获取菜单ID，判断是否被选中                                                 #
# 然后再调用关闭或显示方法            			          	                 #
#                                                                            #
#                                                                            #
#----------------------------------------------------------------------------# 
    def OnCloseOpenpane(self,event):
        ObjectID=event.GetId()
        if ObjectID==22:
            currpane=self.mgr.GetPane("ServerClass_Pane")
            if not event.IsChecked():
                self.view_menu.Check(22, False)
                self.mgr.ClosePane(currpane)
            else:
                currpane.Show()
                self.view_menu.Check(22, True)
        elif ObjectID==23:
            currpane=self.mgr.GetPane("ServerList_Pane")
            if not event.IsChecked():
                self.view_menu.Check(23, False)
                self.mgr.ClosePane(currpane)
            else:
                currpane.Show()
                self.view_menu.Check(23, True)
        elif ObjectID==24:
            currpane=self.mgr.GetPane("System_messages")
            if not event.IsChecked():
                self.view_menu.Check(24, False)
                self.mgr.ClosePane(currpane)
            else:
                currpane.Show()
                self.view_menu.Check(24, True)
        self.mgr.Update()
        event.Skip()


#----------------------------------------------------------------------------#
# 清空操作记录方法                                                           #
#----------------------------------------------------------------------------#
#                                                                            #
#                                			          	                     #
#                                                                            #
#                                                                            #
#----------------------------------------------------------------------------# 
    def OnClearLog(self,event):
        self.SysMessaegText.Clear()
        event.Skip()


#----------------------------------------------------------------------------#
# 保存记录方法                                                               #
#----------------------------------------------------------------------------#
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
#----------------------------------------------------------------------------# 
    def OnSaveLog(self,event):
        #弹出文件保存对话框；
        self.mgr.GetPane("toolbar").Show()
        savedlg = wx.FileDialog(self, message=u"保存记录...", defaultDir=os.getcwd(),defaultFile="", wildcard=self.FileexList, style=wx.SAVE)
        try:
            if savedlg.ShowModal() == wx.ID_OK:
                path = savedlg.GetPath()
                #如果目标文件已经存在则提示是否要覆盖；
                if os.path.exists(path):
                    yndlg = wx.MessageDialog(None, u'保存的文件名已经存在，是否要覆盖？',u'警告信息：', wx.YES_NO | wx.ICON_QUESTION)
                    if yndlg.ShowModal()==wx.ID_YES:
                        os.remove(path)
                        self.OnSaveFileDo(path)
                else:
                    self.OnSaveFileDo(path)
        except Exception,e:
            wx.MessageBox(u"保存出现异常(1)："+str(e),u"OManager服务器管理平台：",style=wx.OK|wx.ICON_EXCLAMATION)
        event.Skip()

    def OnSaveFileDo(self,path):
        try:
            self.wof=open(path,"w")
            self.wof.write(self.SysMessaegText.GetValue().encode('gbk'))
            self.wof.close()
            wx.MessageBox(u"文件保存成功!",u"OManager服务器管理平台：",style=wx.OK|wx.ICON_EXCLAMATION)       
        except Exception,e:
            wx.MessageBox(u"保存出现异常(2)："+str(e),u"OManager服务器管理平台：",style=wx.OK|wx.ICON_EXCLAMATION)


#----------------------------------------------------------------------------#
# 关于方法                                                                   #
#----------------------------------------------------------------------------#
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
#----------------------------------------------------------------------------# 
    def OnOpenSystemAbout(self,event):
        info = wx.AboutDialogInfo()
        info.Name = u"OManager服务器管理平台"
        info.Version = self._sysversion
        info.Copyright = u"(C) 2014 运维进行时"
        info.Description = wordwrap(u"OManager服务器管理平台使用说明。",
            900, wx.ClientDC(self))
        info.Developers = [u"作者：刘天斯    BLOG：http://blog.liuts.com"]
        licenseText=u"关于OManager服务器管理平台，任何第三方都不可以擅自作商业用途。"
        info.License = wordwrap(licenseText, 500, wx.ClientDC(self))
        wx.AboutBox(info)
        event.Skip()




#----------------------------------------------------------------------------#
# 向左/右标签按钮方法                                                        #
#----------------------------------------------------------------------------#
#                                                                            #
#                                			          	                     #
#                                                                            #
#                                                                            #
#----------------------------------------------------------------------------#
    def OnOpenSystemLeft(self,event):
        if self.MainFlatNotebook.GetSelection()>0:
            self.MainFlatNotebook.SetSelection(self.MainFlatNotebook.GetSelection()-1)
        event.Skip()

    def OnOpenSystemRight(self,event):
        if self.MainFlatNotebook.GetSelection()<self.MainFlatNotebook.GetPageCount():
            self.MainFlatNotebook.SetSelection(self.MainFlatNotebook.GetSelection()+1)
        event.Skip()



#----------------------------------------------------------------------------#
# 写消息框方法                                                               #
#----------------------------------------------------------------------------#
# 参数：message                                                              #
#                                			          	                     #
#                                                                            #
#                                                                            #
#----------------------------------------------------------------------------#
    def OnWriteMessageBox(self,message):
        t = time.localtime(time.time())
        st = time.strftime("%Y-%m-%d %H:%M:%S", t)
        self.SysMessaegText.SetInsertionPoint(0)
        self.SysMessaegText.WriteText("++++++++++++++++++++++++++++++++"+str(st)+"++++++++++++++++++++++++++++++++\n"+message+"\n")
        self.SysMessaegText.SetInsertionPoint(0)



#----------------------------------------------------------------------------#
# 更新系统配置按钮方法                                                       #
#----------------------------------------------------------------------------#
#                                                                            #
#                                			          	                     #
#                                                                            #
#                                                                            #
#----------------------------------------------------------------------------#       
    def OnUpdateButtonWra(self,event):
        try:
            self.cf.set("system", "Width", self.WidthText.GetValue())
            self.cf.set("system", "height", self.HeightText.GetValue())
            self.cf.set("system", "ip", self.IP.GetValue())
            self.cf.set("system", "port", self.Port.GetValue())
            self.cf.set("system", "timeout", self.TimeOut.GetValue())
            self.cf.set("system", "max_servers", self.Max_servers.GetValue())
            self.cf.set("system", "secret_key", self.Secret_key.GetValue())
            self.cf.set("system", "upgrade_url", self.Upgrade_url.GetValue())
            
            self.cf.set("db", "db_ip", self.DB_ip.GetValue())
            self.cf.set("db", "db_user", self.DB_user.GetValue())
            self.cf.set("db", "db_pass", self.DB_pass.GetValue())
            self.cf.set("db", "db_name", self.DB_name.GetValue())
            
            self.cf.write(open(sys.path[0]+'/data/config.ini', "w"))
            message=u"数据已成功更新，新配置将在下次启动时生效。"
            wx.MessageBox(message,style=wx.OK|wx.ICON_INFORMATION)
        except Exception,e:
            message=u"更新数据出现异常："+str(e)
            wx.MessageBox(message,u"OManager服务器管理平台：",style=wx.OK|wx.ICON_ERROR)
        self.OnWriteMessageBox(message)
        event.Skip()



#----------------------------------------------------------------------------#
# 报警按钮方法                                                               #
#----------------------------------------------------------------------------#
#                                                                            #
#                                			          	                     #
#                                                                            #
#                                                                            #
#----------------------------------------------------------------------------#
    def OnWraClick(self,event):
        ServerFunctionApp=ServerFunction()
        dlg = wx.ColourDialog(self)
        dlg.GetColourData().SetChooseFull(True)
        if dlg.ShowModal() == wx.ID_OK:
            data = dlg.GetColourData()
            ClickObject=event.GetEventObject()
            ClickObject.SetBackgroundColour(data.GetColour().Get())
        dlg.Destroy()
        event.Skip()




#----------------------------------------------------------------------------#
# 每隔1秒显示时间方法                                                        #
#----------------------------------------------------------------------------#
#                                                                            #
#                                			          	                     #
#                                                                            #
#                                                                            #
#----------------------------------------------------------------------------#
    def OnNotify(self,evt):
        t = time.localtime(time.time())
        st = time.strftime("%Y-%m-%d %H:%M:%S", t)
        self.statusbar.SetStatusText("  "+str(st),2)
        evt.Skip()




#----------------------------------------------------------------------------#
# 消息框单击事件                                                             #
#----------------------------------------------------------------------------#
# 保证光标停留在(0,0)的位置;                                                 #
#                                			          	                     #
#                                                                            #
#                                                                            #
#----------------------------------------------------------------------------#
    def OnTextCtrlTopCurr(self,evt):
        #self.SysMessaegText.SetInsertionPoint(0)
        evt.Skip()


#----------------------------------------------------------------------------#
# 递归遍历服务器信息(XML)到self.Tree控件                                     #
#----------------------------------------------------------------------------#
# 从数据目录读取XML数据到self.tree控件;                                      #
#                                			          	                     #
#                                                                            #
#                                                                            #
#----------------------------------------------------------------------------#
    def AddTreeNodes(self, parentItem, items):
        """
        Recursively traverses the data structure, adding tree nodes to
        match it.
        """
        for item in items:
            if type(item) == str:
                child =self.tree.AppendItem(parentItem, item)
                self.tree.SetItemImage(child, self.fileidx, wx.TreeItemIcon_Normal)
                self.tree.SetItemImage(child, self.fldropenidx, wx.TreeItemIcon_Expanded)                
            else:
                newItem = self.tree.AppendItem(parentItem, item[0])
                self.tree.SetItemImage(newItem, self.fldridx, wx.TreeItemIcon_Normal)
                self.tree.SetItemImage(newItem, self.fldropenidx, wx.TreeItemIcon_Expanded)                
                self.AddTreeNodes(newItem, item[1])





#----------------------------------------------------------------------------#
# self.Tree控件的单击事件OnSelChanged，将结果导入服务器列清框。              #
#----------------------------------------------------------------------------#
# 调用ServerFunction类中的AppSelectServer方法;                               #
# 参数：(服务器分类(一级分类)或服务器类别(二级分类) )              	         #
# 返回：[服务器WIP列表]                                                      #
#                                                                            #
#----------------------------------------------------------------------------#
    def OnSelChanged(self, event):
        self.ServerList.Clear()
        self.item = event.GetItem()
        if self.item:
            #创建对象实例;
            AppSelectServer=ServerFunction()
            
            #调用SelectServerList进行递归遍历运算，筛选当前类别的服务器WIP;
            AppSelectServer.SelectServerList(self.tree.GetItemText(self.item))
            
            #获取返回列表值;
            self.Serverlist_array=AppSelectServer.getServerList()
            
            #将该值给服务器列表框的InsertItems方法进行赋值;
            self.ServerList.InsertItems(self.Serverlist_array,0)
        event.Skip()



#----------------------------------------------------------------------------#
# 判断当前的TAB标签是否存在。                                                #
#----------------------------------------------------------------------------#
#  存在->忽略;                                                               #
#  不存在->创建;      	                                                     #
#                                                                            #
#                                                                            #
#----------------------------------------------------------------------------#
    def NotebookPageExist(self, curr_caption, curr_tabid,RefurbMask=0):
        AppSelectServer=ServerFunction()
        
        PageExist=True
        self.Freeze()
        GetPageCount=self.MainFlatNotebook.GetPageCount()
        if self.MainFlatNotebook.GetPageCount()>0:
            for item in range(0,GetPageCount):
                if self.MainFlatNotebook.GetPageText(item)[:4]==curr_caption[:4]:
                    PageExist=False
                    if RefurbMask==0:
                        self.MainFlatNotebook.SetSelection(int(item))
                    break

            if (PageExist==True and RefurbMask==0) or (RefurbMask==1 and PageExist==False):
                self._newPageCounter+=1
                #====================================================欢迎页===================================================
                if curr_tabid==0:
                    self.MainFlatNotebook.AddPage(self.SysMessaegText, curr_caption+'['+str(self._newPageCounter)+']',True,-1)
                
                #=====================================================运行模块===================================================
                elif curr_tabid==4:
                    self.res = xrc.XmlResource(os.path.abspath(u'Module/'+str(CurrMoudelID).decode('gbk')))
                    panel = self.res.LoadPanel(self, "panel")
                    self.text1 = xrc.XRCCTRL(panel, 'text1')
                    self.text2 = xrc.XRCCTRL(panel, 'text2')
                    if PageExist!=False:
                        self.MainFlatNotebook.AddPage(panel, curr_caption ,True,-1)

                    pass
                
                #=====================================================系统配置===================================================
                elif curr_tabid==5:
                    #新建面板
                    self.ConfigPanel = wx.Panel(self,-1,pos=wx.Point(0, 0),
                                           size=wx.Size(392, 216),style=wx.TAB_TRAVERSAL)
                    self.ConfigPanel.SetBackgroundColour("#eeeeee")
                    self.MainFlatNotebook.AddPage(self.ConfigPanel, curr_caption ,True,-1)

                    #窗口两个StaticBox
                    SYSbsizer = wx.StaticBox(self.ConfigPanel,-1,u'系统参数',(50, 16), (600, 230))
                    DBbsizer = wx.StaticBox(self.ConfigPanel,-1,u'数据库参数',(50, 270), (600, 150))
                    
                    #[系统参数]元素控件(列，行),(宽，高)
                    StaticText(self.ConfigPanel, -1, u"系统宽度：",(60, 41),(70, 20))
                    StaticText(self.ConfigPanel, -1, u"系统高度：",(60, 66),(70, 20))
                    StaticText(self.ConfigPanel, -1, u"主控服务器IP：",(60, 91),(100, 20))
                    StaticText(self.ConfigPanel, -1, u"主控服务器端口：",(60, 116),(100, 20))
                    StaticText(self.ConfigPanel, -1, u"连接主控端超时(s)：",(60, 141),(120, 20))
                    StaticText(self.ConfigPanel, -1, u"可操作服务器数：",(60, 166),(120, 20))
                    StaticText(self.ConfigPanel, -1, u"传输加密密钥：",(60, 191),(120, 20))
                    StaticText(self.ConfigPanel, -1, u"升级URL：",(60, 216),(120, 20))
                    self.WidthText = wx.TextCtrl(self.ConfigPanel,-1, self._syswidth, (170, 40),size=(50, 20))
                    self.HeightText = wx.TextCtrl(self.ConfigPanel,-1,self._sysheight, (170, 65),size=(50, 20))
                    self.IP = wx.TextCtrl(self.ConfigPanel,-1,self._ip, (170, 90),size=(90, 20))
                    self.Port = wx.TextCtrl(self.ConfigPanel,-1,self._port, (170, 115),size=(50, 20))
                    self.TimeOut = wx.TextCtrl(self.ConfigPanel,-1,self._timeout, (170, 140),size=(40, 20))
                    self.Max_servers = wx.TextCtrl(self.ConfigPanel,-1,self._max_servers, (170, 165),size=(40, 20))
                    self.Secret_key = wx.TextCtrl(self.ConfigPanel,-1,self._secret_key, (170, 190),size=(380, 20))
                    self.Upgrade_url = wx.TextCtrl(self.ConfigPanel,-1,self._upgrade_url, (170, 215),size=(380, 20))

                    #[数据库参数]元素控件(列，行),(宽，高)
                    StaticText(self.ConfigPanel, -1, u"数据库IP：",(60, 295),(70, 20))
                    StaticText(self.ConfigPanel, -1, u"数据库用户：",(60, 320),(70, 20))
                    StaticText(self.ConfigPanel, -1, u"数据库密码：",(60, 345),(70, 20))
                    StaticText(self.ConfigPanel, -1, u"数据库名：",(60, 370),(70, 20))
                    self.DB_ip = wx.TextCtrl(self.ConfigPanel,-1,self._db_ip, (150, 295),size=(160, 20))
                    self.DB_user = wx.TextCtrl(self.ConfigPanel,-1,self._db_user, (150, 320),size=(160, 20))
                    self.DB_pass = wx.TextCtrl(self.ConfigPanel,-1,self._db_pass, (150, 345),size=(160, 20))
                    self.DB_name = wx.TextCtrl(self.ConfigPanel,-1,self._db_name, (150, 370),size=(160, 20))
                    
                    #update button
                    UpdateButton =wx.lib.buttons.GenBitmapTextButton(self.ConfigPanel,-1,bitmap=wx.Image(sys.path[0]+'/img/Modify.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap(),label=u' 更新配置 ', pos=wx.Point(300, 430),size=wx.Size(85, 35), style=0)
                    self.MainFlatNotebook.SetSelection(GetPageCount)

                    self.Bind(wx.EVT_BUTTON, self.OnUpdateButtonWra,UpdateButton)
                    
        else:
            self._newPageCounter+=1
            self.MainFlatNotebook.AddPage(self.SysWelcome, curr_caption+str(self._newPageCounter),True,-1)
        self.MainFlatNotebook.SetSelection(self.MainFlatNotebook.GetPageCount())
        self.MainFlatNotebook.SetWindowStyleFlag(fnb.FNB_BOTTOM|fnb.FNB_VC8 | fnb.FNB_DROPDOWN_TABS_LIST | fnb.FNB_TABS_BORDER_SIMPLE | fnb.FNB_BACKGROUND_GRADIENT)
        self.MainFlatNotebook.Refresh()
        self.Thaw()
        

#----------------------------------------------------------------------------#
# 显示工具栏按钮相关方法。                                                   #
#----------------------------------------------------------------------------#
#                                                                            #
#               	                                                         #
#                                                                            #
#                                                                            #
#----------------------------------------------------------------------------#
    #欢迎窗口
    def OnOpenwelcome(self, event):
        self.NotebookPageExist(u"欢迎窗口",0)
        self.SysMessaegText.WriteText(u"[欢迎窗口]\n")
        self.SysMessaegText.SetInsertionPoint(0)
        event.Skip()

   
    #操作模块
    def OnOpenOptapp(self, event):
        try:
            #定义高窗口体的模板清单
            BigFrameModuleID=[3300]
            
            for file_info in self.Moduledetail:
                if str(file_info).find(str(event.GetId()))!=-1:
                    curr_module=file_info
                    break;
            try:
                BigFrameModuleID.index(event.GetId())
                FrameHeight=430
                FrameWidth=610
            except Exception,e:
                FrameHeight=230
                FrameWidth=430
            
            self.SysMessaegText.WriteText(u"[操作模块] - "+str(curr_module).decode('gbk','ignore')+"\n")
            
            #弹出模块窗口
            try:
                if self.showwin.ModulelStr!=None:
                    self.showwin.OnCloseWindow()
                self.showwin = DisplayModuleFrame(self, -1, u"操作模块 - "+str(curr_module).decode('gbk','ignore'), pos=(500,500),size=(FrameWidth, FrameHeight),style = wx.MINIMIZE_BOX |wx.SYSTEM_MENU |wx.CAPTION,CurrMoudelName=curr_module)
                self.showwin.Show(True)
            except:
                self.showwin = DisplayModuleFrame(self, -1, u"操作模块 - "+str(curr_module).decode('gbk','ignore'), pos=(500,500),size=(FrameWidth, FrameHeight),style = wx.MINIMIZE_BOX |wx.SYSTEM_MENU |wx.CAPTION,CurrMoudelName=curr_module)
                self.showwin.Show(True)
            self.SysMessaegText.SetInsertionPoint(0)
        except Exception,e:
            message=u"系统出现异常(OpenOptapp)："+str(e)
            wx.MessageBox(message,u"OManager服务器管理平台：",style=wx.OK|wx.ICON_ERROR)        
        event.Skip()

    
    #系统配置
    def OnOpenConapp(self, event):
        try:        
            self.NotebookPageExist(u"系统配置",5)
            self.SysMessaegText.WriteText(u"[系统配置]\n")
            self.SysMessaegText.SetInsertionPoint(0)
        except Exception,e:
            message=u"系统出现异常："+str(e)
            wx.MessageBox(message,u"OManager服务器管理平台：",style=wx.OK|wx.ICON_ERROR)        
        event.Skip()
    

    #系统升级方法
    def OnOpenSystemUpdate(self,event):
        #创建数据实例
        GetUpdateNum=sysbash()
        verdata=GetUpdateNum.GetUpdateVersion()
        
        #重新读取配置文件，方便比较升级版本号
        self.cf.read(sys.path[0]+'/data/config.ini')
        self._sysUpversion= self.cf.get("system","Upversion")
        
        if str(verdata[0][0])==str(self._sysUpversion):
            self.OnWriteMessageBox(u"系统数据已经是最新，无需升级。[当前升级版本号："+self._sysUpversion+"]")
        elif str(verdata[0][0])>str(self._sysUpversion):
            
            #弹出升级窗口
            Upwin = UpdateFrame(self, -1, u"系统升级...", size=(350, 100),style = wx.STAY_ON_TOP,lastversion=verdata[0][0])
            Upwin.Show(True)


    #===========================================运行模块============================================
    def OnOpenRunapp(self,event):
        import rpyc
        from cPickle import loads
        FunApp=ServerFunction()
        Intologs=sysbash()
        
        #设置连接超时
        socket.setdefaulttimeout(int(self._timeout))
        
        #连接rpyc服务器
        try:
            conn=rpyc.connect(self._ip,int(self._port))
            conn.root.login('OMuser','KJS23o4ij09gHF734iuhsdfhkGYSihoiwhj38u4h')
        except Exception,e:
            message=u"系统提示：连接远程服务器超时。"+str(e)
            wx.MessageBox(message,u"OManager服务器管理平台：",style=wx.OK|wx.ICON_ERROR)
            return
        
        self.SysMessaegText.SetInsertionPoint(0)
        
        #应用逻辑操作域
        try:
            put_string=""
            Parameter_string=""
            #获取模块对话框返回的模块信息串
            try:
                GetModelestr=self.showwin.GetTxtValue()
            except Exception,e:
                wx.MessageBox(u"请先选择功能模块及目标服务器再执行！",u"OManager服务器管理平台：",style=wx.OK|wx.ICON_ERROR)
                return

            GetModelestrrow=string.split(GetModelestr,',')

            for i in range(1,len(GetModelestrrow)):
                Parameter_string+=GetModelestrrow[i]+"@@"
                
            #调用OnGetSelectServerinfo方法获取计算机名|字符串|服务器数量
            _server_list=self.OnGetSelectServerinfo('serverserial_ip',1,int(self._max_servers))

            #判断用户是否选择了至少一台服务器，不选则直接返回。
            if not _server_list:
                return

            #-------------------------将操作写入记录----------------
            Intologs.Addsyslogs(self.CurrentAdmin,u"操作对象："+self.OnGetSelectServerinfo('lip',1,20)+u"-操作MID:"+GetModelestrrow[0])
            
            #合并提交串
            put_string+=str(GetModelestrrow[0])+"@@"+_server_list+"@@"+Parameter_string
            #加密提交串
            put_string=FunApp.tencode(put_string,self._secret_key)

            #调用rpyc的Runcommands()方法执行任务，返回的结果通过tdecode()方法解密
            OPresult=FunApp.tdecode(conn.root.Runcommands(put_string),self._secret_key).decode('utf8')
            
            #在“输出消息”框打印返回结果
            self.OnWriteMessageBox(FunApp.format_str(OPresult))
           
            conn.close()
        except Exception,e:
            message=str(e).decode('utf8')
            wx.MessageBox(message,u"OManager服务器管理平台：",style=wx.OK|wx.ICON_ERROR)
            return

    def OnStopclose(self,event):
        event.Veto()
        return

 
#----------------------------------------------------------------------------#
# 关闭AuiManager面板邦定视图菜单。                                           #
#----------------------------------------------------------------------------#
#                                                                            #
#               	                                                         #
#                                                                            #
#                                                                            #
#----------------------------------------------------------------------------#
    def OnPaneClose(self, event):
        Panename = event.GetPane().name
        if Panename=="ServerClass_Pane":
            self.view_menu.Check(22, False)
        elif Panename=="ServerList_Pane":
            self.view_menu.Check(23, False)
        elif Panename=="System_messages":
            self.view_menu.Check(24, False)            
            
#----------------------------------------------------------------------------#
# 退出系统。                                                                 #
#----------------------------------------------------------------------------#
# Destroy窗体退出系统                                                        #
#               	                                                         #
#                                                                            #
#                                                                            #
#----------------------------------------------------------------------------#
    def OnExit(self, event):
        #-------------------------将退出注销写入日志----------------
        Intologs=sysbash()
        
        self.OnWriteMessageBox(u"用户准备退出系统。")
        yndlg = wx.MessageDialog(None, u'确定要退出系统？',u'警告信息：', wx.YES_NO | wx.ICON_QUESTION)
        if yndlg.ShowModal()==wx.ID_YES:
            Intologs.Addsyslogs(self.CurrentAdmin,u"退出系统    IP:"+socket.gethostbyname(socket.gethostname()))
            self.taskBarIcon.Destroy()
            self.Destroy()


#----------------------------------------------------------------------------#
# 托盘隐藏。                                                                 #
#----------------------------------------------------------------------------#
# 托盘隐藏                                                                   #
#               	                                                         #
#                                                                            #
#                                                                            #
#----------------------------------------------------------------------------#
    def OnHide(self, event):
        self.Hide()
        event.Skip()


    def OnIconfiy(self, event):
        self.Hide()
        event.Skip()


#----------------------------------------------------------------------------#
# 应程序启动句柄，调用主程序并实现监听事件                            	     #
#----------------------------------------------------------------------------#
#                                                                            #
#   ServManageApp(LOOP)=> ServManageFrame     	                             #
#                                                                            #
#                                                                            #
#----------------------------------------------------------------------------#
class ServManageApp(wx.App):
    def OnInit(self):
        "OnInit"
        frame = ServManageFrame(None, u"OManager服务器管理")
        frame.Show()
        self.SetTopWindow(frame)
        return True

    def OnExit(self):
        "OnExit"
        pass

#ServManageApp(redirect=False).MainLoop() 