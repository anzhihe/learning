#!/usr/bin/env python
# $Id: tkhello0.py,v 1.1 2000/02/21 09:04:25 wesc Exp $
#
# tkhello0.py -- "Hello World!" 0 in Tkinter:
#	- "Hello World!" label (need to close window to quit)
#	- just like tkhello1.py except for no toplevel
#
# created by wesc 00/02/20
#

import Tkinter
label = Tkinter.Label(text='Hello World!')
label.pack()
label.mainloop()
