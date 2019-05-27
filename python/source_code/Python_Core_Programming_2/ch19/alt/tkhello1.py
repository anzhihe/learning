#!/usr/bin/env python
# $Id: tkhello1.py,v 1.1 2000/02/21 09:04:25 wesc Exp $
#
# tkhello1.py -- "Hello World!" 1 in Tkinter:
#        - "Hello World!" label (need to close window to quit)
#
# created by wesc 00/02/20
#

# import Tkinter module
import Tkinter

# create toplevel window
top = Tkinter.Tk()

# create label
label = Tkinter.Label(top, text='Hello World!')

# pack label
label.pack()

# enter main loop
Tkinter.mainloop()

"""
same as:

import Tkinter
Tkinter.Label(Tkinter.Tk(), text='Hello World!').pack()
Tkinter.mainloop()
"""
