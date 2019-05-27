# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import os
import re
import time
import sys
import string
import ServerList
import random, base64
from hashlib import sha1

#----------------------------------------------------------------------------#
# Name:        ServerFunction.py                                             #
# Purpose:     system Logic Module                                           #
# Author:      Liutiansi                                                     #
# Email:       liutiansi@gamil.com                                           #
# Created:     2014/05/03                                                    #
# Copyright:   (c) 2014                                                      #
#-----------------------------------------------------------------------------

class ServerFunction():
    def __init__(self):
        
        #服务器列表初始化
        self.serverlist=[]
        
        #服务器分类(一级分类)标志
        self.root_child_id=""



#----------------------------------------------------------------------------#
# 递归遍历服务器信息(XML)到self.serverlist                                   #
#----------------------------------------------------------------------------#
# 其中XML对象从ServerList包获取;                                             #
# 参数：（当前选择的服务器分类(一级/二级)）     	          	             #
#                                                                            #
#                                                                            #
#-----------------------------------------------------------------------------
    def SelectServerList(self,root_server):
        
        #判断选择的是否是一级类别，如果是则获取id值;
        for root_child in ServerList.root_doc:
            if root_child[0].text==root_server:
                self.root_child_id=root_child.get('id')
                break;
        
        #递归出当前选择的服务器类别/应用类别一致的服务器wip清单;
        for class_child in ServerList.class_doc:
            if class_child[6].text==self.root_child_id or class_child[4].text==root_server:
                self.serverlist.append(class_child[1].text)
 


#----------------------------------------------------------------------------#
# 返回服务器列表self.serverlist                                              #
#----------------------------------------------------------------------------#
#                                                                            #
#      	          	                                                         #
#                                                                            #
#                                                                            #
#-----------------------------------------------------------------------------   
    def getServerList(self):
        return self.serverlist



#----------------------------------------------------------------------------#
# 递归遍历服务器信息(XML)到相关域数据                                        #
#----------------------------------------------------------------------------#
# return_type=lip：返回lip;                                                  #
# return_type=os：返回os;     	          	                                 #
# return_type=app：返回app;                                                  #
# return_type=locate：返回locate;                                            #
# return_type=option: 返回option;                                            #
# return_type=serverserial :返回serverserial;                                #
# return_type=serverserial_ip :返回主机名+IP，'192.168.1.20*sn2013-08-020'   #
#----------------------------------------------------------------------------#
    def GetServerinfo(self,server_ip,return_type):
        for class_child in ServerList.class_doc:
            if class_child[1].text.strip()==server_ip or class_child[2].text.strip()==server_ip or class_child[0].text.strip()==server_ip:
                if return_type=="serverserial_ip":
                    return class_child.find("lip").text+"*"+class_child.find("serverserial").text
                else:
                    return class_child.find(return_type).text
        return "Null"


#----------------------------------------------------------------------------#
# 返回用户Ping CNC/NT值                                                      #
#----------------------------------------------------------------------------#
#                                                                            #
#----------------------------------------------------------------------------#
    def GetServerPingValue(self,server_ip):
        try:
            #匹配time=value的正则；
            ip=server_ip
            p=re.compile(r'(?<=time=)(\d+(?:.\d+)?)')

            #执行ping命令；
            pingaling = os.popen("ping -n 1 "+ip,"r")
            #sys.stdout.flush()

            #初始化运算变量；
            i=0
            Counter=0
            Average=0

            #根据3次ping的结果，取出有time=value的行，累加value/有效的行数；
            while 1:
                line = pingaling.readline()
                if line!='':
                    tmplist=p.findall(line)
                    if len(tmplist)!=0:
                        i+=1         
                        Counter+=float(tmplist[0])
                        status=Counter/i
                else:
                    break
            return str("%.2f"%status)
        except Exception,e:
            return str(e)



#----------------------------------------------------------------------------#
# RGB TO HEX COLOR                                                           #
#----------------------------------------------------------------------------#
#                                                                            #
#     	          	                                                         #
#                                                                            #
#                                                                            #
#                                                                            #
#----------------------------------------------------------------------------#
    def RGB2HEX(self,R,G,B):
        rgb=int(R)*256*256+int(G)*256+int(B)
        srgb=hex(rgb)
        srgb=srgb.replace('0x','')
        srgb=srgb.zfill(6)
        return '#'+srgb
    

#----------------------------------------------------------------------------#
# Return Module Parameter                                                    #
#----------------------------------------------------------------------------#
# 'fun'=Fun type                                                             #
# 'id'=Module ID  	                                                         #
# 'name'=Module Name                                                         #
#                                                                            #
#----------------------------------------------------------------------------#
    def ModuleParameter(self,ModuleName,Returntype):
        Modulerow=string.split(ModuleName,'_')
        if Returntype=='fun':
            return Modulerow[0]
        elif Returntype=='id':
            return Modulerow[1]
        elif Returntype=='name':
            return Modulerow[2]
        

#----------------------------------------------------------------------------#
# List to str                                                                #
#----------------------------------------------------------------------------#
#                                                                            #
#   	                                                                     #
#                                                                            #
#                                                                            #
#----------------------------------------------------------------------------#
    def List2str(self,ListArray,hz):
        sharstr=""
        for i in ListArray:
            sharstr+=self.GetServerinfo(str(i)[str(i).find('sn'):len(str(i))-1],'lip')+'...........'+str(i)[0:10]+hz
        return sharstr

  
#----------------------------------------------------------------------------#
# Dict to str                                                                #
#----------------------------------------------------------------------------#
# gettype=0 正常分析字典                                                     #
# gettype=1 获取字典列表英                                                   #
#                                                                            # 
#                                                                            #
#----------------------------------------------------------------------------#
    def Dict2str(self,Dict,gettype=0):
        try:
            sharstr=""
            for (host,details) in Dict.iteritems():
                if gettype==1:
                    return details[1]
                sharstr+=u"主机："+self.GetServerinfo(host,'lip')+"\n"
                if details[0]==0:
                    sharstr+=u"运行结果：成功\n"
                    sharstr+=details[1]
                else:
                    sharstr+=u"运行结果：失败\n"
                    sharstr+=details[2]
                sharstr+="---------------------------------------------------------------------------------------------------------\n"
            return sharstr
        except Exception,e:
            return str(Dict)
            

#----------------------------------------------------------------------------#
# Replace string                                                             #
#----------------------------------------------------------------------------#
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
#----------------------------------------------------------------------------#
    def Replace_str(self,string_content="",source="",target=""):
        try:
            return string_content.replace(source,target)
        except Exception,e:
            pass
            


#----------------------------------------------------------------------------#
# AE加解密码                                                                 #
#----------------------------------------------------------------------------#
#                                                                            #                                                                            #
#                                                                            #
#                                                                            #                                                                            #
#                                                                            #
#----------------------------------------------------------------------------#
    def crypt(self,data, key):
        """RC4 algorithm"""
        x = 0
        box = range(256)
        for i in range(256):
            x = (x + box[i] + ord(key[i % len(key)])) % 256
            box[i], box[x] = box[x], box[i]
        x = y = 0
        out = []
        for char in data:
            x = (x + 1) % 256
            y = (y + box[x]) % 256
            box[x], box[y] = box[y], box[x]
            out.append(chr(ord(char) ^ box[(box[x] + box[y]) % 256]))

        return ''.join(out)

    def tencode(self,data, key, encode=base64.b64encode, salt_length=16):
        """RC4 encryption with random salt and final encoding"""
        salt = ''
        for n in range(salt_length):
            salt += chr(random.randrange(256))
        data = salt + self.crypt(data, sha1(key + salt).digest())
        if encode:
            data = encode(data)
        return data

    def tdecode(self,data, key, decode=base64.b64decode, salt_length=16):
        """RC4 decryption of encoded data"""
        if decode:
            data = decode(data)
        salt = data[:salt_length]
        return self.crypt(data[salt_length:], sha1(key + salt).digest())


#----------------------------------------------------------------------------#
# farmat response string                                                     #
#----------------------------------------------------------------------------#
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
#----------------------------------------------------------------------------#
    def format_str(self,response_content=""):
        try:
            outstring=""
            outstring=self.Replace_str(response_content,"<font color=\'#eeeeee\'>","")
            outstring=self.Replace_str(outstring,"<font color=#ffffff>","")
            outstring=self.Replace_str(outstring,"<font color=\'#006699\'>","")
            outstring=self.Replace_str(outstring,"<font color=\'red\'>","")
            outstring=self.Replace_str(outstring,"<b>","")
            outstring=self.Replace_str(outstring,"</b>","")
            outstring=self.Replace_str(outstring,"</font>","")
            outstring=self.Replace_str(outstring,"<br>","\n")
            outstring=self.Replace_str(outstring,"<table width=\'100%\' height=\'15\'><tbody><tr><td background=\'/static/images/B24.gif\'></td></tr></tbody></table>","")
            return outstring
        except Exception,e:
            return str(e)