#-*- coding:utf-8 -*-
#!/usr/bin/python
import datetime
import time,os,sys

#----------------------------------------------------------------------------#
# Name:        pubutil.py                                                    #
# Purpose:     Simple webserver - yorserver                                  #
# Author:      Liutiansi                                                     #
# Email:       liutiansi@gamil.com                                           #
# Created:     2014/06/06                                                    #
# Copyright:   (c) 2014                                                      #
#----------------------------------------------------------------------------#

 #return Expires
def get_http_expiry(_Expirestype,_num):
    """
    Adds the given number of days on to the current date and returns the future
    date as a string, in the format: "Mon, 18 Jan 2010 17:10:02 GMT"
    """
    if _Expirestype=="d":
        expire_date = datetime.datetime.now() + datetime.timedelta(days=_num)
    elif _Expirestype=="h":
        expire_date = datetime.datetime.now() + datetime.timedelta(hours=_num)
    else:
        expire_date = datetime.datetime.now() + datetime.timedelta(minutes=_num)
    return expire_date.strftime('%a, %d %b %Y %H:%M:%S GMT')

 #return max-age
def secs_from_days(_seconds,_num):
    """
    Returns the number of seconds that are in the given number of days.
    (i.e. 1 returns 86400)
    """
    return _seconds * _num
    
#set gzip
def compressBuf(buf,_compresslevel):
    import gzip, cStringIO
    zbuf = cStringIO.StringIO()
    zfile = gzip.GzipFile(mode = 'wb',  fileobj = zbuf, compresslevel = _compresslevel)
    zfile.write(buf)
    zfile.close()
    return zbuf.getvalue()

def cur_file_dir():
     path = sys.path[0]
     if os.path.isdir(path):
         return path
     elif os.path.isfile(path):
         return os.path.dirname(path)
         
#check file
def checkfile(_path):
    return os.path.isfile(_path)
    
#check path
def checkpath(_path):
    return os.path.exists(_path)

#get parent dir
def parent_dir(_path):
    parent_dir_string=""
    if _path=="/":
        return parent_dir_string
        
    dir_list=_path.split("/")
    if len(dir_list)==2:
        return parent_dir_string
    else:
        for i in range(0,len(dir_list)-2):
            parent_dir_string+=dir_list[i]+"/"
    return parent_dir_string