#!/usr/bin/env python
'''
$Id: friends3.py,v 1.1 2000/12/31 01:32:45 wesc Exp $

Friends CGI demo
'''

import cgi
from urllib import quote_plus
from string import capwords
#from sys import stderr
#s = stderr.write

header = 'Content-Type: text/html\n\n'
url = 'http://localhost/cgi-bin/friends3.py'

errhtml = '''<HTML><HEAD><TITLE>Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back ONCLICK="window.history.back()"></FORM>
</BODY></HTML>'''

# showError() --> None
def showError(error_str):
    'showError() -- display error message'
    print header + errhtml % (error_str)

friendradio = '<INPUT TYPE=radio NAME=howmany VALUE="%s" %s> %s\n'

formhtml = '''<HTML><HEAD><TITLE>Friends CGI Demo</TITLE></HEAD>
<BODY><H3>Friends list for: <I>%s</I></H3>
<FORM ACTION="%s">
<B>Your Name:</B>
<INPUT TYPE=hidden NAME=action VALUE=edit>
<INPUT TYPE=text NAME=person VALUE="%s" SIZE=15>
<P><B>How many friends do you have?</B>
%s
<P><INPUT TYPE=submit></FORM></body></html>'''

# showForm() --> None
def showForm(who, howmany):
    'showForm() -- presents blank or data-filled form for new input'

    friends = ''
    for i in [0, 10, 25, 50, 100]:
        checked = ''
        if str(i) == howmany:
            checked = 'CHECKED'
        friends = friends + friendradio % (str(i), checked, str(i))
    print header + formhtml % (who, url, who, friends)

reshtml = '''<HTML><HEAD><TITLE>Friends CGI Demo</TITLE></HEAD>
<BODY><H3>Friends list for: <I>%s</I></H3>
Your name is: <B>%s</B><P>
You have <B>%s</B> friends.
<P>Click <a href="%s">here</a> to edit your data again.
</BODY></HTML>'''

# doResults() --> None
def doResults(who, howmany):
    'doResults() -- displays results with given form data'

    # substitute in real name and number of friends and return
    newurl = url + '?action=reedit&person=%s&howmany=%s' % (quote_plus(who), howmany)
    print header + reshtml % (who, who, howmany, newurl)

# process() --> None
def process():
    'process() does all the work:  grabs user data and determines routine to call'

    error = ''

    # initialize Data class object
    form = cgi.FieldStorage()
    #s('name: '+str(form.name)+'\n')
    #s('keys: '+str(form.keys())+'\n')
    #for i in form.keys():
            #s('item: '+str(form[i].name)+' has a value of '+str(form[i].value)+' and is a ' + form[i].__class__.__name__ + '\n')

    # get user name
    if form.has_key('person'):
        who = capwords(form['person'].value)
    else:
        who = 'NEW USER'

    # get name and number of friends
    if form.has_key('howmany'):
        howmany = form['howmany'].value
    else:
        if form.has_key('action') and form['action'].value == 'edit':
            error = 'Please select the number of friends you have.'
        else:
            howmany = 0

    # no errors, either display form or present results
    if not error:

        # if editing the first time, show results
        if form.has_key('action') and form['action'].value != 'reedit':
            doResults(who, howmany)

        # otherwise, show form
        else:
            showForm(who, howmany)

    # send error message back if error situation
    else:
        showError(error)


# invoke if called directly
if __name__ == '__main__':
    process()
