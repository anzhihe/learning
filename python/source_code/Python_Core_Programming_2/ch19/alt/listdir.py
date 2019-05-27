#!/usr/bin/env python
# $Id: listdir.py,v 1.8 2000/05/26 10:19:30 wesc Exp $
#
# listdir.py -- traverse directory tree
#
# created by wesc 00/02/20
#

import Tkinter, os, time, string
__version__ = string.split('$Revision: 1.8 $')[1]

class DirList:

    # do everything!
    def __init__(self, initdir=None):
	self.top = Tkinter.Tk()
	self.label = Tkinter.Label(self.top, text='Directory Lister' + ' v' + __version__)
	self.label.pack()
	self.cwd=Tkinter.StringVar(self.top)
	self.dirl = Tkinter.Label(self.top, fg='blue', font=('Helvetica', 12, 'bold'))
	self.dirl.pack()

	self.dirfm = Tkinter.Frame(self.top)
	self.dirsb = Tkinter.Scrollbar(self.dirfm)
	self.dirsb.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)

	self.dirs = Tkinter.Listbox(self.dirfm, height=15, width=50, yscrollcommand=self.dirsb.set)
	self.dirs.bind('<Double-1>', self.setdirandgo)
	self.dirsb.config(command=self.dirs.yview)
	self.dirs.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH)
	self.dirfm.pack()

	self.dirn = Tkinter.Entry(self.top, width=50, textvariable=self.cwd)
	self.dirn.bind('<Return>', self.dols)
	self.dirn.pack()

	self.bfm = Tkinter.Frame(self.top)
	self.clr = Tkinter.Button(self.bfm, text='Clear', command=self.clrdir, activeforeground='white', activebackground='blue')
	self.ls = Tkinter.Button(self.bfm, text='List Directory', command=self.dols, activeforeground='white', activebackground='green')
	self.quit = Tkinter.Button(self.bfm, text='Quit', command=self.top.quit, activeforeground='white', activebackground='red')
	self.clr.pack(side=Tkinter.LEFT)
	self.ls.pack(side=Tkinter.LEFT)
	self.quit.pack(side=Tkinter.LEFT)
	self.bfm.pack()

	if initdir:
	    # put selection in entry and do it
	    self.cwd.set(os.curdir)
	    self.dols()


    # clear entry
    def clrdir(self, ev=None):
	self.cwd.set('')

    # set dir entry
    def setdirandgo(self, ev=None):

	# save last search
	self.last = self.cwd.get()

	# set red bg while searching
	self.dirs.config(selectbackground='red')

	# grab listbox selection, default to ('.') os.curdir if not there
	check = self.dirs.get(self.dirs.curselection())
	if not check:
	    check = os.curdir

	# grab selection and strip any extra chars (a la 'ls -F')
	if check[-1] in '@/*': check = check[:-1]

	# set entry and run
	self.cwd.set(check)
	self.dols()


    def dols(self, ev=None):

	error = ''
	# check if a exist and if directory
	tdir = self.cwd.get()
	vi = 0
	if not tdir:
	    tdir = os.curdir
	if not os.path.exists(tdir):
	    error = tdir + ': no such file'
	elif not os.path.isdir(tdir):
	    if os.name == 'posix':
		vi = 1
		error = tdir + ': starting "vi" in xterm...'
	    else:
		error = tdir + ': not a directory'
	if error:
	    self.cwd.set(error)
	    self.top.update()
	    time.sleep(2)
	    if not (hasattr(self, 'last') and self.last):
		self.last = os.curdir
	    self.cwd.set(self.last)
	    self.dirs.config(selectbackground='LightSkyBlue')
	    self.top.update()
	    if vi:
		os.system("xterm -rv -e vi " + tdir)
	    return

	# get listing
	self.cwd.set('FETCHING DIRECTORY CONTENTS...')
	self.top.update()
	dirlist = os.listdir(tdir)

	# go there to for relativity
	os.chdir(tdir)
	self.dirl.config(text=os.getcwd())

	# replace old file listing
	self.dirs.delete(0, Tkinter.END)
	self.dirs.insert(Tkinter.END, os.curdir)
	self.dirs.insert(Tkinter.END, os.pardir)
	for eachFile in dirlist:
	    self.dirs.insert(Tkinter.END, eachFile)
	self.cwd.set(tdir)
	self.dirs.config(selectbackground='LightSkyBlue')

d = DirList(os.curdir)
Tkinter.mainloop()
