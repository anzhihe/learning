# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------#
# Name:        ServManager.py                                                #
# Purpose:     Management App Server login(by socket)                        #
# Author:      Liutiansi                                                     #
# Email:       liutiansi@gamil.com                                           #
# Created:     2014/06/18                                                    #
# Copyright:   (c) 2014                                                      #
#-----------------------------------------------------------------------------

import wx
import os
import sys

import wx.lib.hyperlink as hl
from ServManagerMain import ServManageFrame
from DBclass import User
from Verification import *
from wx.lib.stattext import GenStaticText as StaticText
from wx.lib.statbmp  import GenStaticBitmap as StaticBitmap

class Login(wx.Dialog):
    
#----------------------------------------------------------------------------#
# 初始化登录对话框，包括用户名、密码、私钥等。                        	     #
#----------------------------------------------------------------------------#
#                                                                            #
#                                        	                             #
#                                                                            #
#                                                                            #
#-----------------------------------------------------------------------------    
    def __init__(self):
        wx.Dialog.__init__(self, parent=None, id=-1,title=u"OManager服务器管理 ",style=wx.STAY_ON_TOP)
        self.Center()
        sizer = wx.GridBagSizer(hgap=5, vgap=10)
        self.SetBackgroundColour("#ffffff")
        self.SetIcon(wx.Icon(sys.path[0]+'/img/Loading.ico',wx.BITMAP_TYPE_ICO))
        bmp = wx.Image(sys.path[0]+'/img/title.jpg', wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
        self.logo = wx.StaticBitmap(self, -1, bmp, size=(320, bmp.GetHeight()))
        sizer.Add(self.logo, pos=(0, 0), span=(1,6), flag=wx.EXPAND)
        
        #Loging text
        self.logintext=StaticText(self, -1, u"正在验证,请稍等...", (70, 210))
        self.logintext.Show(False)
        
        # Label
        sizer.Add(wx.StaticText(self, -1, u"用户名：　"), pos=(1, 1), flag=wx.ALIGN_RIGHT)
        sizer.Add(wx.StaticText(self, -1, u"密　码：　"), pos=(2, 1), flag=wx.ALIGN_RIGHT)
        sizer.Add(wx.StaticText(self, -1, u"私　钥：　"), pos=(3, 1), flag=wx.ALIGN_RIGHT)
        
        # Text
        self.username = wx.TextCtrl(self, -1,"", size=(120, 20))
        self.username.SetMaxLength(20)
        self.password = wx.TextCtrl(self, -1,"", size=(120, 20), style=wx.TE_PASSWORD)
        self.password.SetMaxLength(20)
        self.Privatekey = wx.TextCtrl(self, -1,"", size=(160, 20))
        self.Privatekey.SetMaxLength(60)        
        sizer.Add(self.username, pos=(1,2), span=(1,1))
        sizer.Add(self.password, pos=(2,2), span=(1,1))
        sizer.Add(self.Privatekey, pos=(3,2), span=(1,1))
        
        
        # Button
        self.Open = wx.Button(self, -1, u"浏览...", (10, 10))
        #self.Open.SetForegroundColour("#ffffff")
        #self.Open.SetBackgroundColour("#154786")
        self.ok = wx.Button(self, -1, u"登    录", (35, 20))
        self.ok.SetForegroundColour("#FF245D")
        self.cancel = wx.Button(self, -1, u"退   出", (35, 20))
        self.cancel.SetForegroundColour("#006699")

        
        # bind the evt
        self.ok.Bind(wx.EVT_LEFT_DOWN,self.OnDisplayInfo)
        self.ok.Bind(wx.EVT_LEFT_UP, self.OnOK)
        self.Bind(wx.EVT_BUTTON, self.OnCancel, self.cancel)
        #self.logo.Bind(wx.EVT_LEFT_DOWN, self.OnCancel)
        self.Bind(wx.EVT_BUTTON, self.OnOpenbutton,self.Open)
        
        sizer.Add(self.ok, pos=(4,1),flag=wx.EXPAND)
        sizer.Add(self.cancel, pos=(4,2))
        sizer.Add(self.Open, pos=(3,3))
        sizer.Add((4, 2), (6, 2))
        #sizer.SetEmptyCellSize((10, 40))
        sizer.AddGrowableCol(3)
        sizer.AddGrowableRow(3)        
        self.SetSizer(sizer)
        self.Fit()
 
 
 
#----------------------------------------------------------------------------#
# 定义［确定］按钮方法。                              	                     #
#----------------------------------------------------------------------------#
#                                                                            #
# 验证相关域是否为空                          	                             #
#                                                                            #
#                                                                            #
#-----------------------------------------------------------------------------
    def OnDisplayInfo(self,event):
        self.logintext.Show(True)
        
    def OnOK(self, event):
        
        user = User()
        if not self.username.GetValue():
            wx.MessageBox(u'请输入用户名。', u"提示")
            self.username.SetFocus()
            self.logintext.Show(False)
            return

        if not self.password.GetValue():
            wx.MessageBox(u'请输入密码。', u"提示")
            self.password.SetFocus()
            self.logintext.Show(False)
            return

        if not self.Privatekey.GetValue():
            wx.MessageBox(u'请选择私钥文件。', u"提示")
            self.Privatekey.SetFocus()
            self.logintext.Show(False)
            return
        elif not os.path.exists(self.Privatekey.GetValue()):
            wx.MessageBox(u'选择的私钥文件不存在！', u"提示")
            self.Privatekey.SetFocus()
            self.logintext.Show(False)
            return
        try:
            self.GetcheckRow=user.Check(self.username.GetValue(), self.password.GetValue(),md5(self.Privatekey.GetValue()))
            if  not self.GetcheckRow:
                wx.MessageBox(u'用户名、密码错误或私钥验证不通过，请确认后重新输入。', u"错误")
                self.username.SetFocus()
                self.logintext.Show(False)
                return
        except Exception,e:
            message=u"系统出现异常："+str(e)
            wx.MessageBox(message,u"OManager服务器管理平台：",style=wx.OK|wx.ICON_ERROR)              
        self.EndModal(wx.ID_OK)

    def OnGetuserInfo(self):
        return self.GetcheckRow

#----------------------------------------------------------------------------#
# 定义［浏览］按钮方法。                              	                     #
#----------------------------------------------------------------------------#
#                                                                            #
# 弹出打开对话框选择私钥文件并赋值给文本框。                          	     #
#                                                                            #
#                                                                            #
#-----------------------------------------------------------------------------  
    def OnOpenbutton(self, event):
        """[打开]按钮方法(调用打开文件对话框)"""
        dlg = wx.FileDialog(self, message=u"选择私钥",defaultDir=os.getcwd(),defaultFile="",style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR)
        if dlg.ShowModal() == wx.ID_OK:
            self.Importfilename = dlg.GetPaths()
            self.Privatekey.SetValue("%s" % (self.Importfilename[0]))
        dlg.Destroy()

    def OnCancel(self, event):
        self.EndModal(wx.ID_CANCEL)        


#----------------------------------------------------------------------------#
# 应用方法。                                    	                         #
#----------------------------------------------------------------------------#
#                                                                            #
# 帐号验证通过后调用主程序。                                    	         #
#                                                                            #
#                                                                            #
#----------------------------------------------------------------------------- 
class MisApp(wx.App):
    def OnInit(self):
        login = Login()
        ret = login.ShowModal()
        self.username = login.username.GetValue()
        self.password = login.password.GetValue()
        self.userInfo = login.OnGetuserInfo()
        login.Destroy()

        if (ret == wx.ID_OK):
            self.frame = ServManageFrame(None,u"OManager服务器管理 ")
            self.frame.Show()
            self.SetTopWindow(self.frame)
        return True

if __name__ == "__main__":
    try:
        import psyco
        psyco.full()
    except ImportError:
        pass    
    app = MisApp()
    app.MainLoop()
