#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import pango

class GTKapp(object):
    def __init__(self):
    top = gtk.Window(gtk.WINDOW_TOPLEVEL)
    top.connect("delete_event", gtk.main_quit)
    top.connect("destroy", gtk.main_quit)
    box = gtk.VBox(False, 0)
    lb = gtk.Label(
        'Animals (in pairs; min: pair, max: dozen)')
    box.pack_start(lb)

    sb = gtk.HBox(False, 0)
    adj = gtk.Adjustment(2, 2, 12, 2, 4, 0)
    sl = gtk.Label('Number:')
    sl.modify_font(
        pango.FontDescription("Arial Bold 10"))
    sb.pack_start(sl)
    ct = gtk.SpinButton(adj, 0, 0)
    sb.pack_start(ct)
    box.pack_start(sb)

    cb = gtk.HBox(False, 0)
    c2 = gtk.Label('Type:')
    cb.pack_start(c2)
    ce = gtk.combo_box_entry_new_text()
    for animal in ('dog', 'cat', 'hamster', 'python'):
        ce.append_text(animal)
    cb.pack_start(ce)
    box.pack_start(cb)

    qb = gtk.Button("")
    red = gtk.gdk.color_parse('red')
    sty = qb.get_style()
    for st in (gtk.STATE_NORMAL,
        gtk.STATE_PRELIGHT, gtk.STATE_ACTIVE):
        sty.bg[st] = red
    qb.set_style(sty)
    ql = qb.child
    ql.set_markup('<span color="white">QUIT</span>')
    qb.connect_object("clicked",
        gtk.Widget.destroy, top)
    box.pack_start(qb)
    top.add(box)
    top.show_all()

if __name__ == '__main__':
    animal = GTKapp()
    gtk.main()
