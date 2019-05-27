#!/usr/bin/env python
# $Id: tkhello4.py,v 1.2 2000/02/21 10:56:50 wesc Exp $
#
# tkhello4.py -- "Hello World!" 4 in Tkinter:
#        - label, button, and scale widgets
#
# created by wesc 00/02/21
#

# import all Tkinter module attributes
from Tkinter import *

# callback function to resize label when Scale is slid
def resize(ev=None):
    label.config(font='Helvetica -%d bold' % scale.get())

# create toplevel window with a 250x150 pixel geometry
top = Tk()
top.geometry('250x150')

# create and pack label
label = Label(top, text='Hello World!', font='Helvetica -12 bold')
label.pack(fill=Y, expand=1)

# create and pack Scale/slider
scale = Scale(top, from_=10, to=40, orient=HORIZONTAL, command=resize)
scale.set(12)
scale.pack(fill=X, expand=1)

# create and pack button
quit = Button(top, text='QUIT', command=top.quit, activeforeground='white', activebackground='red')
quit.pack()

# enter main loop
mainloop()
