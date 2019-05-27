#!/usr/bin/env python

import cgi

header = 'Content-Type: text/html\n\n'

formhtml = '''<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>Friends list for: <I>NEW USER</I></H3>
<FORM ACTION="/cgi-bin/friends2.py">
<B>Enter your Name:</B>
<INPUT TYPE=hidden NAME=action VALUE=edit>
<INPUT TYPE=text NAME=person VALUE="NEW USER" SIZE=15>
<P><B>How many friends do you have?</B>
%s
<P><INPUT TYPE=submit></FORM></BODY></HTML>'''

fradio = '<INPUT TYPE=radio NAME=howmany VALUE="%s" %s> %s\n'

def showForm():
    friends = ''
    for i in [0, 10, 25, 50, 100]:
        checked = ''
        if i == 0:
            checked = 'CHECKED'
        friends = friends + fradio % \
            (str(i), checked, str(i))

    print header + formhtml % (friends)

reshtml = '''<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>Friends list for: <I>%s</I></H3>
Your name is: <B>%s</B><P>
You have <B>%s</B> friends.
</BODY></HTML>'''

def doResults(who, howmany):
    print header + reshtml % (who, who, howmany)

def process():
    form = cgi.FieldStorage()
    if form.has_key('person'):
        who = form['person'].value
    else:
        who = 'NEW USER'

    if form.has_key('howmany'):
        howmany = form['howmany'].value
    else:
        howmany = 0

    if form.has_key('action'):
        doResults(who, howmany)
    else:
        showForm()

if __name__ == '__main__':
    process()
