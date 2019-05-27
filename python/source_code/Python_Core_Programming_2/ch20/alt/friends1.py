#!/usr/bin/env python
'''
$Id: friends1.py,v 1.1 2000/12/31 01:32:45 wesc Exp $

Friends CGI demo
'''

import cgi
from string import atoi,replace

reshtml = '''Content-Type: text/html\n
<HTML><HEAD><TITLE>Friends CGI Demo (dynamic screen)</TITLE></HEAD>
<BODY><H3>Friends list for: <I>%s</I></H3>
Your name is: <B>%s</B><P>
You have <B>%s</B> friends.
</BODY></HTML>'''

# process() does all the work
def process():

    # initialize Data class object
    form = cgi.FieldStorage()

    # get name and number of friends
    who = form['person'].value
    howmany = form['howmany'].value

    # substitute in real name and number of friends and return
    print reshtml % (who, who, howmany)

# invoke if called directly
if __name__ == '__main__':
    process()
