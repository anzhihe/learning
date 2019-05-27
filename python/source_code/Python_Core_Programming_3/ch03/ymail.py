#!/usr/bin/env python
'ymail.py - demo Yahoo!Mail SMTP/SSL, POP, IMAP'

from cStringIO import StringIO
from imaplib import IMAP4_SSL
from platform import python_version
from poplib import POP3_SSL, error_proto
from socket import error

# SMTP_SSL added in 2.6, fixed in 2.6.3
release = python_version()
if release > '2.6.2':
    from smtplib import SMTP_SSL, SMTPServerDisconnected
else:
    SMTP_SSL = None

from secret import *    # you need to provide MAILBOX, PASSWD

who = '%s@yahoo.com' % MAILBOX
from_ = who
to = [who]

headers = [
    'From: %s' % from_,
    'To: %s' % ', '.join(to),
    'Subject: test SMTP send via 465/SSL',
]
body = [
    'Hello',
    'World!',
]
msg = '\r\n\r\n'.join(('\r\n'.join(headers), '\r\n'.join(body)))

def getSubject(msg, default='(no Subject line)'):
    '''\
    getSubject(msg) - iterate over 'msg' looking for
    Subject line; return if found, otherwise 'default'
    '''
    for line in msg:
        if line.startswith('Subject:'):
            return line.rstrip()
        if not line:
            return default

# SMTP/SSL
print '*** Doing SMTP send via SSL...'
if SMTP_SSL:
    try:
        s = SMTP_SSL('smtp.mail.yahoo.com', 465)
        s.login(MAILBOX, PASSWD)
        s.sendmail(from_, to, msg)
        s.quit()
        print '    SSL mail sent!'
    except SMTPServerDisconnected:
        print '    error: server unexpectedly disconnected... try again'
else:
    print '    error: SMTP_SSL requires 2.6.3+'

# POP
print '*** Doing POP recv...'
try:
    s = POP3_SSL('pop.mail.yahoo.com', 995)
    s.user(MAILBOX)
    s.pass_(PASSWD)
    rv, msg, sz = s.retr(s.stat()[0])
    s.quit()
    line = getSubject(msg)
    print '    Received msg via POP: %r' % line
except error_proto:
    print '    error: POP for Yahoo!Mail Plus subscribers only'

# IMAP
print '*** Doing IMAP recv...'
try:
    s = IMAP4_SSL('imap.n.mail.yahoo.com', 993)
    s.login(MAILBOX, PASSWD)
    rsp, msgs = s.select('INBOX', True)
    rsp, data = s.fetch(msgs[0], '(RFC822)')
    line = getSubject(StringIO(data[0][1]))
    s.close()
    s.logout()
    print '    Received msg via IMAP: %r' % line
except error:
    print '    error: IMAP for Yahoo!Mail Plus subscribers only'
