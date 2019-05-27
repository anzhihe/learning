#!/usr/bin/env python

import tkinter

top = tkinter.Tk()
quit = tkinter.Button(top, text='Hello World!',
    command=top.quit)
quit.pack()
tkinter.mainloop()
