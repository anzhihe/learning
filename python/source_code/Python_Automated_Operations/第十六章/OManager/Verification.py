# -*- coding: utf-8 -*-
import os, sys, hashlib

#----------------------------------------------------------------------------#
# Name:        Verification.py                                                 #
# Purpose:     md5 check			                              #
# Author:      from internet                                                     #
# Email:                                                  #
# Created:     2008/10/17                                                    #
# Copyright:   (c) 2008                                                      #
#-----------------------------------------------------------------------------

def md5(fileName, excludeLine="", includeLine=""):
    """Compute md5 hash of the specified file"""
    m = hashlib.md5()
    try:
        fd = open(fileName,"rb")
    except IOError:
        print "Unable to open the file in readmode:", filename
        return
    eachLine = fd.readline()
    while eachLine:
        if excludeLine and eachLine.startswith(excludeLine):
            continue
        m.update(eachLine)
        eachLine = fd.readline()
    m.update(includeLine)
    fd.close()
    return m.hexdigest()
