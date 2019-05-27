#!/usr/bin/env python

CODEC = 'UTF-8'
UNICODE_HELLO = u'''
Hello!
\u00A1Hola!
\u4F60\u597D!
\u3053\u3093\u306B\u3061\u306F!
'''.replace('\n', '<P>')

print '''Content-Type: text/html; charset=%s

<HTML><HEAD><TITLE>Unicode CGI Demo</TITLE></HEAD>
<BODY><H1>Unicode CGI Demo</H1><P>
<BIG>%s</BIG></BODY></HTML>
'''.replace('\n', '\r\n') % (CODEC, UNICODE_HELLO.encode(CODEC))
