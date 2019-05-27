#!/usr/bin/env python

from tkinter import Tk
from time import sleep
from tkinter.messagebox import showwarning
import win32com.client as win32

warn = lambda app: showwarning(app, 'Exit?')
RANGE = list(range(3, 8))

def ppoint():
    app = 'PowerPoint'
    ppoint = win32.gencache.EnsureDispatch('%s.Application' % app)
    pres = ppoint.Presentations.Add()
    ppoint.Visible = True

    s1 = pres.Slides.Add(1, win32.constants.ppLayoutText)
    sleep(1)
    s1a = s1.Shapes[0].TextFrame.TextRange
    s1a.Text = 'Python-to-%s Demo' % app
    sleep(1)
    s1b = s1.Shapes[1].TextFrame.TextRange
    for i in RANGE:
        s1b.InsertAfter("Line %d\r\n" % i)
        sleep(1)
    s1b.InsertAfter("\r\nTh-th-th-that's all folks!")

    warn(app)
    pres.Close()
    ppoint.Quit()

if __name__=='__main__':
    Tk().withdraw()
    ppoint()
