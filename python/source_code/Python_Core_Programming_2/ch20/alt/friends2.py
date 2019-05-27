#!/usr/bin/env python
'''
$Id: friends2.py,v 1.1 2000/12/31 01:32:45 wesc Exp $

CGI demo
'''

import cgi

header = 'Content-Type: text/html\n\n'

formhtml = '''<HTML><HEAD><TITLE>Friends CGI Demo</TITLE></HEAD>
<BODY><H3>Friends list for: <I>NEW USER</I></H3>
<FORM ACTION="/cgi-bin/friends2.py">
<B>Enter your Name:</B>
<INPUT TYPE=hidden NAME=action VALUE=edit>
<INPUT TYPE=text NAME=person VALUE="" SIZE=15>
<P><B>How many friends do you have?</B>
%s
<P><INPUT TYPE=submit></FORM></BODY></HTML>'''

friendradio = '<INPUT TYPE=radio NAME=howmany VALUE="%s" %s> %s\n'

def showForm():
    friends = ''
    for i in [0, 10, 25, 50, 100]:
        checked = ''
        if i == 0:
            checked = 'CHECKED'
        friends = friends + friendradio % (str(i), checked, str(i))
    print header + formhtml % (friends)


reshtml = '''<HTML><HEAD><TITLE>Friends CGI Demo</TITLE></HEAD>
<BODY><H3>Friends list for: <I>%s</I></H3>
Your name is: <B>%s</B><P>
You have <B>%s</B> friends.
</BODY></HTML>'''

def doResults(who, howmany):
    # substitute in real name and number of friends and return
    print header + reshtml % (who, who, howmany)


# process() does all the work
def process():

    # initialize Data class object
    form = cgi.FieldStorage()

    # get user name
    if form.has_key('person'):
        who = form['person'].value
    else:
        who = 'NEW USER'

    # get name and number of friends
    if form.has_key('howmany'):
        howmany = form['howmany'].value
    else:
        howmany = 0

    # if editing, show results
    if form.has_key('action'):
        doResults(who, howmany)

    # otherwise, show form
    else:
        showForm()

# invoke if called directly
if __name__ == '__main__':
    process()
