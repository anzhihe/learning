#!/usr/bin/env python

from cgi import FieldStorage
from os import environ
from StringIO import StringIO
from urllib import quote, unquote

class AdvCGI(object):
    header = 'Content-Type: text/html\n\n'
    url = '/cgi-bin/advcgi.py'

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
<H3>Enter file to upload <SMALL>(max size 4K)</SMALL></H3>
<INPUT TYPE=file NAME=upfile VALUE="%s" SIZE=45>
<P><INPUT TYPE=submit>
</FORM></BODY></HTML>'''

    langSet = ('Python', 'Ruby', 'Java', 'C++', 'PHP', 'C', 'JavaScript')
    langItem = '<INPUT TYPE=checkbox NAME=lang VALUE="%s"%s> %s\n'

    def getCPPCookies(self):    # reads cookies from client
        if 'HTTP_COOKIE' in environ:
            cookies = [x.strip() for x in environ['HTTP_COOKIE'].split(';')]
            for eachCookie in cookies:
                if len(eachCookie) > 6 and eachCookie[:3] == 'CPP':
                    tag = eachCookie[3:7]
                    try:
                        self.cookies[tag] = eval(unquote(eachCookie[8:]))
                    except (NameError, SyntaxError):
                        self.cookies[tag] = unquote(eachCookie[8:])
            if 'info' not in self.cookies:
                self.cookies['info'] = ''
            if 'user' not in self.cookies:
                self.cookies['user'] = ''
        else:
            self.cookies['info'] = self.cookies['user'] = ''

        if self.cookies['info'] != '':
            self.who, langStr, self.fn = self.cookies['info'].split(':')
            self.langs = langStr.split(',')
        else:
            self.who = self.fn = ''
            self.langs = ['Python']

    def getUserCookie(self):
        # see if user cookie set up yet
        if not ('user' in self.cookies and self.cookies['user']):
            cookStatus = '<I>(cookie has not been set yet)</I>'
            userCook = ''
        else:
            userCook = cookStatus = self.cookies['user']
        return userCook

    def showForm(self):
        self.getCPPCookies()

        # put together language checkboxes
        langStr = []
        for eachLang in AdvCGI.langSet:
            langStr.append(AdvCGI.langItem % (eachLang,
                ' CHECKED' if eachLang in self.langs else '',
                eachLang))

        userCook = self.getUserCookie()
        print '%s%s' % (AdvCGI.header, AdvCGI.formhtml % (
            AdvCGI.url, cookStatus, userCook, self.who,
            ''.join(langStr), self.fn))

    errhtml = '''<HTML><HEAD><TITLE>
Advanced CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>'''

    def showError(self):
        print '%s%s' % (AdvCGI.header, AdvCGI.errhtml % (self.error))

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
        for eachCookie in self.cookies:
            print 'Set-Cookie: CPP%s=%s; path=/' % (
                eachCookie, quote(self.cookies[eachCookie]))

    def doResults(self):
        MAXBYTES = 4096
        langList = ''.join(
            '<LI>%s<BR>' % eachLang for eachLang in self.langs)
        filedata = self.fp.read(MAXBYTES)
        if len(filedata) == MAXBYTES and f.read():
            filedata = '%s%s' % (filedata,
              '... <B><I>(file truncated due to size)</I></B>')
        self.fp.close()
        if filedata == '':
            filedata = '<B><I>(file not given or upload error)</I></B>'
        filename = self.fn
        userCook = self.getUserCookie()

        # set cookies
        self.cookies['info'] = ':'.join(
            (self.who, ','.join(self.langs), filename))
        self.setCPPCookies()

        print '%s%s' % (AdvCGI.header, AdvCGI.reshtml % (
            cookStatus, self.who, langList,
            filename, filedata, AdvCGI.url))

    def go(self):
        self.cookies = {}
        self.error = ''
        form = FieldStorage()
        if not form.keys():
            self.showForm()
            return

        if 'person' in form:
            self.who = form['person'].value.strip().title()
            if self.who == '':
                self.error = 'Your name is required. (blank)'
        else:
            self.error = 'Your name is required. (missing)'

        self.cookies['user'] = unquote(form['cookie'].value.strip()) if 'cookie' in form else ''
        if 'lang' in form:
            langData = form['lang']
            if isinstance(langData, list):
                self.langs = [eachLang.value for eachLang in langData]
            else:
                self.langs = [langData.value]
        else:
            self.error = 'At least one language required.'

        if 'upfile' in form:
            upfile = form['upfile']
            self.fn = upfile.filename or ''
            if upfile.file:
                self.fp = upfile.file
            else:
                self.fp = StringIO('(no data)')
        else:
            self.fp = StringIO('(no file)')
            self.fn = ''

        if not self.error:
            self.doResults()
        else:
            self.showError()

if __name__ == '__main__':
    page = AdvCGI()
    page.go()
