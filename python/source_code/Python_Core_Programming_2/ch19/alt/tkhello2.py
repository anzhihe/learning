#!/usr/bin/env python
# $Id: tkhello2.py,v 1.1 2000/02/21 09:04:25 wesc Exp $
#
# tkhello2.py -- "Hello World!" 2 in Tkinter:
#        - "Hello World!" with just a button (which quits the app)
#
# created by wesc 00/02/20
#

# import Tkinter module
import Tkinter

# create toplevel window
top = Tkinter.Tk()

# create button
quit = Tkinter.Button(top, text='Hello World!', command=top.quit)

# pack button
quit.pack()

# enter main loop
Tkinter.mainloop()
