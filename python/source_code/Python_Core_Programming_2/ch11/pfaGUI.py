#!/usr/local/bin/python2.5

from functools import partial
import Tkinter

root = Tkinter.Tk()
MyButton = partial(Tkinter.Button,
    root, fg='white', bg='blue')
b1 = MyButton(text='Button 1')
b2 = MyButton(text='Button 2')
qb = MyButton(text='QUIT', bg='red',
    command=root.quit)
b1.pack()
b2.pack()
qb.pack(fill=Tkinter.X, expand=True)
root.title('PFAs!')
root.mainloop()
