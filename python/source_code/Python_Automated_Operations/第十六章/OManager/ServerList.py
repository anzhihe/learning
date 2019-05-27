# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import os
import sys

#----------------------------------------------------------------------------#
# Name:        ServerList.py                                                 #
# Purpose:     connection to Database update it                              #
# Author:      Liutiansi                                                     #
# Email:       liutiansi@gamil.com                                           #
# Created:     2008/10/17                                                    #
# Copyright:   (c) 2008                                                      #
#-----------------------------------------------------------------------------
root_tree = ET.parse(sys.path[0]+'/data/ServerOptioninfo.xml')
class_tree = ET.parse(sys.path[0]+'/data/Serverinfo.xml')

root_doc = root_tree.getroot()
class_doc = class_tree.getroot()
        

class ServerClassList():

    def Resurn_list(self,UserPrivileges):
        
        ServerList_KEY=[]
        serverclass=[]
        serverapp=[]

        for root_child in root_doc:

            if not root_child.get('id') in UserPrivileges and not UserPrivileges[0]=="root":
                continue
            serverclass.append(root_child[0].text.encode('gbk'))
            serverapp=[]
            for class_child in class_doc:
                if class_child[6].text==root_child.get('id'):
                    try:
                        serverapp.index(class_child[4].text.encode('gbk'))
                    except:
                        serverapp.append(class_child[4].text.encode('gbk'))
            
            serverclass.append(serverapp)
            ServerList_KEY.append(serverclass)
            serverclass=[]
        return ServerList_KEY