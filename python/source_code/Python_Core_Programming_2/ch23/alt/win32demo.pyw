#!/usr/bin/env python

from Tkinter import Tk
from tkMessageBox import showwarning, askyesno

def fromImport(mod, attr=None):
    # set attributes to import, if any
    if attr:
	if isinstance(attr, (list, tuple)):
	    fromlist = attr
	else:
	    fromlist = [attr]

    # perform actual import
    try:
	module = __import__(mod, globals(), locals(), fromlist)
    except ImportError:
	return None

    # return desired object
    if attr:
	return vars(module)[attr]
    else:
	return module

if __name__=='__main__':
    Tk().withdraw()

    # app name; module and function name(s)
    dispatch = {
	'Excel': 'excel',
	'Word': 'word',
	'Outlook': 'olook',
	'PowerPoint': 'ppoint',
    }

    # run each main function for each app
    for eachApp in dispatch:
	if askyesno(eachApp, "Launch %s demo?" % eachApp):
	    target = dispatch[eachApp]
	    # "from target import target"
	    targetFunc = fromImport(target, target)

	    # exec if function imported successfully
	    if targetFunc:
		targetFunc()
	    else:
		showwarning('Could not start "%s"' % eachApp)
