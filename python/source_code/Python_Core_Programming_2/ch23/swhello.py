#!/usr/bin/env jython

from pawt import swing
import sys
from java.awt import Color, BorderLayout

def quit(e):
    sys.exit()

top = swing.JFrame("PySwing")
box = swing.JPanel(BorderLayout())
hello = swing.JLabel("Hello World!")
quit = swing.JButton("QUIT", actionPerformed=quit,
    background=Color.red, foreground=Color.white)

box.add("North", hello)
box.add("South", quit)
top.contentPane.add(box)
top.pack()
top.visible = 1	# or True for Jython 2.2+
