#!/usr/bin/env python
'''
$Id: advcgi.py,v 1.1 2000/12/31 01:32:45 wesc Exp $

advcgi.py -- tests CGI file uploads and multi-valued CGI variables

Advanced CGI demo

created by wesc on 00/07/25
'''

from cgi import FieldStorage
from os import environ
from StringIO import StringIO
from urllib import quote, unquote
#from sys import stderr
#s = stderr.write

class AdvCGI(object):

        header = 'Content-Type: text/html\n\n'
        url = '/py/advcgi.py'

        formhtml = '''<HTML><HEAD><TITLE>
Advanced CGI Demo</TITLE></HEAD>
<BODY><H2>Advanced CGI Demo Form</H2>
<FORM METHOD=post ACTION="%s" ENCTYPE="multipart/form-data">
<H3>My Cookie Setting</H3>
<LI> <CODE><B>CPPuser = %s</B></CODE>
<H3>Enter cookie value<BR>
<INPUT NAME=cookie value="%s"> (<I>optional</I>)</H3>
<H3>Enter your name<BR>
<INPUT NAME=person VALUE="%s"> (<I>required</I>)</H3>
<H3>What languages can you program in?
(<I>at least one required</I>)</H3>
%s
<H3>Enter file to upload</H3>
<INPUT TYPE=file NAME=upfile VALUE="%s" SIZE=45>
<P><INPUT TYPE=submit>
</FORM></BODY></HTML>'''

        langSet = ('Python', 'PERL', 'Java', 'C++', 'PHP', 'C', 'JavaScript')
        langItem = '<INPUT TYPE=checkbox NAME=lang VALUE="%s"%s> %s\n'


        # reads cookies from client, creates cookies, who, langs
        def getCPPCookies(self):
                if environ.has_key('HTTP_COOKIE'):
                        #s('reading cookies from server...\n')
                        #for eachCookie in map(strip, split(environ['HTTP_COOKIE'], ';')):
                        cookies = [x.strip() for x in environ['HTTP_COOKIE'].split(';')]
                        for eachCookie in cookies:
                                if len(eachCookie) > 6 and eachCookie[:3] == 'CPP':
                                        tag = eachCookie[3:7]
                                        try:
                                                self.cookies[tag] = eval(unquote(eachCookie[8:]))
                                        except (NameError, SyntaxError):
                                                self.cookies[tag] = unquote(eachCookie[8:])
                        if not self.cookies.has_key('info'):
                            self.cookies['info'] = ''
                        if not self.cookies.has_key('user'):
                            self.cookies['user'] = ''
                else:
                        #s('no cookies on server...\n')
                        self.cookies['info'] = self.cookies['user'] = ''

                #s('cookies: %s\n' % str(self.cookies))
                if self.cookies['info'] != '':
                        self.who, langStr, self.fn = self.cookies['info'].split(':')
                        self.langs = langStr.split(',')
                else:
                        self.who = self.fn = ''
                        self.langs = ['Python']


        def showForm(self):
                self.getCPPCookies()                # get cookies

                # put together lang checkboxes
                langStr = ''
                for eachLang in AdvCGI.langSet:
                        if eachLang in self.langs:
                                langStr = langStr + AdvCGI.langItem % (eachLang, ' CHECKED', eachLang)
                        else:
                                langStr = langStr + AdvCGI.langItem % (eachLang, '', eachLang)

                # see if user cookie set up yet
                if not self.cookies.has_key('user') or self.cookies['user'] == '':
                        cookieStatus = '<I>(cookie has not been set yet)</I>'
                        userCook = ''
                else:
                        userCook = cookieStatus = self.cookies['user']

                # output results
                #s('filename: ' + self.fn + '\n')
                print AdvCGI.header + AdvCGI.formhtml % (AdvCGI.url, cookieStatus, userCook, self.who, langStr, self.fn)
                #print AdvCGI.header + AdvCGI.formhtml % (AdvCGI.url, cookieStatus, userCook, self.who, langStr)


        errhtml = '''<HTML><HEAD><TITLE>
Advanced CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>'''


        def showError(self):
                print AdvCGI.header + AdvCGI.errhtml % (self.error)


        reshtml = '''<HTML><HEAD><TITLE>
Advanced CGI Demo</TITLE></HEAD>
<BODY><H2>Your Uploaded Data</H2>
<H3>Your cookie value is: <B>%s</B></H3>
<H3>Your name is: <B>%s</B></H3>
<H3>You can program in the following languages:</H3>
<UL>%s</UL>
<H3>Your uploaded file...<BR>
Name: <I>%s</I><BR>
Contents:</H3>
<PRE>%s</PRE>
Click <A HREF="%s"><B>here</B></A> to return to form.
</BODY></HTML>'''


        def setCPPCookies(self):
                for eachCookie in self.cookies.keys():
                        #s('setting %s cookie...\n' % eachCookie)
                        print 'Set-Cookie: CPP%s=%s; path=/' % (eachCookie, quote(self.cookies[eachCookie]))


        def doResults(self):
                MAXBYTES = 1024
                langlist = ''
                for eachLang in self.langs:
                        langlist = langlist + '<LI>%s<BR>' % eachLang
                filedata = ''
                while len(filedata) < MAXBYTES:
                        data = self.fp.readline()
                        if data == '': break
                        filedata = filedata + data
                else:
                        filedata = filedata + '... <B><I>(file truncated due to size)</I></B>'
                self.fp.close()
                if filedata == '':
                        filedata = '<B><I>(file upload error or file not given)</I></B>'
                filename = self.fn

                # see if user cookie set up yet
                if not self.cookies.has_key('user') or self.cookies['user'] == '':
                        cookieStatus = '<I>(cookie has not been set yet)</I>'
                        userCook = ''
                else:
                        userCook = cookieStatus = self.cookies['user']

                # set cookies
                self.cookies['info'] = ':'.join([self.who, ','.join(self.langs), filename])
                self.setCPPCookies()

                # output page
                print AdvCGI.header + AdvCGI.reshtml % (cookieStatus, self.who, langlist, filename, filedata, AdvCGI.url)


        def __init__(self):
                self.cookies = {}


        def go(self):
                self.error = ''

                form = FieldStorage()

                if form.keys() == []:
                    #s('calling showForm()\n')
                    self.showForm()
                    return

                if form.has_key('person'):
                        self.who = form['person'].value.strip().title()
                        if self.who == '':
                                self.error = 'Your name is required. (blank)'
                else:
                        self.error = 'Your name is required. (missing)'

                if form.has_key('cookie'):
                        self.cookies['user'] = unquote(form['cookie'].value.strip())
                else:
                        self.cookies['user'] = ''

                self.langs = []
                if form.has_key('lang'):
                        langdata = form['lang']
                        if type(langdata) == type([]):
                                for eachLang in langdata:
                                        self.langs.append(eachLang.value)
                        else:
                                self.langs.append(langdata.value)
                else:
                        self.error = 'At least one language required.'

                if form.has_key('upfile'):
                        upfile = form["upfile"]
                        self.fn = upfile.filename or ''
                        #s('filename is %s??\n' % self.fn)
                        if upfile.file:
                                self.fp = upfile.file
                        else:
                                self.fp = StringIO('(no data)')
                else:
                        self.fp = StringIO('(no file)')
                        self.fn = ''

                if not self.error:
                        #s('calling doResults()\n')
                        self.doResults()
                else:
                        #s('calling showError()\n')
                        self.showError()


if __name__ == '__main__':
        page = AdvCGI()
        page.go()
