#!/usr/bin/env python

import Tkinter

top = Tkinter.Tk()
quit = Tkinter.Button(top, text='Hello World!',
    command=top.quit)
quit.pack()
Tkinter.mainloop()
