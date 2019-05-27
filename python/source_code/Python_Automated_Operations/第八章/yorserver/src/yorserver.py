#-*- coding:utf-8 -*-
#!/usr/bin/python
import logging
import string,cgi,time,os,socket,sys
from SocketServer import BaseServer
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn,ForkingMixIn
from CGIHTTPServer import CGIHTTPRequestHandler
import urllib
import shutil
from OpenSSL import SSL
from configobj import ConfigObj
from optparse import OptionParser
import pubutil

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

#----------------------------------------------------------------------------#
# Name:        yorserver.py                                                  #
# Purpose:     Simple webserver - yorserver                                  #
# Author:      Liutiansi                                                     #
# Email:       liutiansi@gamil.com                                           #
# Created:     2014/06/06                                                    #
# Copyright:   (c) 2014                                                      #
#----------------------------------------------------------------------------#

#read config file
try:
    configfilename=os.path.dirname(pubutil.cur_file_dir())+'/conf/yorserver.conf'
    yorconfig = ConfigObj(configfilename, encoding="utf8")
except IOError, e:
    print "Read yorserver.conf Error:"+str(e)
    sys.exit()


#defind Expires type
ExpiresTypes = {
    "d"	: 86400,
	"h"	: 3600,
	"m"	: 60,
}
    
#defind http mime.types
contentTypes=[]
for m in yorconfig['contentTypes']:
    tmp=[]
    tmp.append(m)
    tmp.append(yorconfig['contentTypes'][m])
    contentTypes.append(tmp)
contentTypes=dict(contentTypes)


#set web server version
server_version = yorconfig['server_version']

#bind webserver ip
bind_ip=yorconfig['bind_ip']

#bind webserver port
port=int(yorconfig['port'])

#set python version
sys_version = yorconfig['sys_version']

#set http protocol version
protocol_version = yorconfig['protocol_version']

#set gzip on/off
gzip=yorconfig['gzip']['gzip']
#set compress level(1~9)
compresslevel=int(yorconfig['gzip']['compresslevel'])

#set ssl(on/off)
ssl=yorconfig['ssl']['ssl']
privatekey=yorconfig['ssl']['privatekey']
certificate=yorconfig['ssl']['certificate']

#set file Expires(d/h/m).
Expires=yorconfig['Expires']

#Multithreading support
Multithreading=yorconfig['Multithreading']

#Multiprocess support
Multiprocess=yorconfig['Multiprocess']

#set document_root
DocumentRoot=yorconfig['DocumentRoot']

#set 404 page
page404=yorconfig['page404']

#directory list
Indexes=yorconfig['Indexes']

#set default page
indexpage=yorconfig['indexpage']

#set access log
Logfile=yorconfig['Logfile']

#set error log
errorfile=yorconfig['errorfile']

#set cgi(on/off)
cgi_moudle=yorconfig['cgim']['cgi_moudle']
cgi_path=yorconfig['cgim']['cgi_path']
cgi_extensions=eval(yorconfig['cgim']['cgi_extensions'], dict(__builtins__=None))

#check path
if ssl=="on":
    if not pubutil.checkfile(privatekey):
        print "Error: privatekey \""+privatekey+"\" No such file or directory."
        sys.exit()

    if not pubutil.checkfile(certificate):
        print "Error: certificate \""+certificate+"\" No such file or directory."
        sys.exit()

if not pubutil.checkpath(DocumentRoot):
    print "Error: DocumentRoot \""+DocumentRoot+"\" No such file or directory."
    sys.exit()

if not pubutil.checkfile(Logfile):
    print "Error: Logfile \""+Logfile+"\" No such file or directory."
    sys.exit()

if not pubutil.checkfile(errorfile):
    print "Error: errorfile \""+errorfile+"\" No such file or directory."
    sys.exit()

if cgi_moudle=="on":
    if len(cgi_path)==0:
        print "Error: cgi_path is null? please set."
        sys.exit()
    for _path in cgi_path:
        if not pubutil.checkpath(pubutil.cur_file_dir()+'/'+_path):
            print "Error: cgi_path \""+pubutil.cur_file_dir()+'/'+_path+"\" No such file or directory."
            sys.exit()

#system logs
try:
    logger=logging.getLogger()
    handler=logging.FileHandler(errorfile)
    logger.addHandler(handler)
    logger.setLevel(logging.NOTSET)
except IOError, e:
    print "+"+str(e)+"+"

    
class SecureHTTPServer(HTTPServer):
    def __init__(self, server_address, HandlerClass):
        BaseServer.__init__(self, server_address, HandlerClass)
        ctx = SSL.Context(SSL.SSLv23_METHOD)
        ctx.use_privatekey_file (privatekey)
        ctx.use_certificate_file(certificate)
        self.socket = SSL.Connection(ctx, socket.socket(self.address_family,self.socket_type))
        self.server_bind()
        self.server_activate()

class ServerHandler(CGIHTTPRequestHandler):
    
    #webserver info
    server_version=server_version
    sys_version=sys_version
    protocol_version=protocol_version
    CGIHTTPRequestHandler.cgi_directories = cgi_path

    def handle_one_request(self):
        try:
            self.raw_requestline = self.rfile.readline(65537)
            if len(self.raw_requestline) > 65536:
                self.requestline = ''
                self.request_version = ''
                self.command = ''
                self.send_error(414)
                return

            if not self.raw_requestline:
                self.close_connection = 1
                return
            if not self.parse_request():
                return

            mname = 'do_' + self.command
            if not hasattr(self, mname):
                self.send_error(501, "Unsupported method (%r)" % self.command)
                return
            method = getattr(self, mname)
            method()

            if not self.wfile.closed:
                self.wfile.flush() #actually send the response if not already done.

        except socket.timeout, e:
            logger.error(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+"-"+str(e))
            self.close_connection = 1
            return 

    def setup(self):
        self.connection = self.request
        self.rfile = socket._fileobject(self.request, "rb", self.rbufsize)
        self.wfile = socket._fileobject(self.request, "wb", self.wbufsize)

    def do_GET(self):
        try:
            #go to deault page.
            if self.path.endswith("/"):
                if Indexes=="on":
                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    f= self.list_directory(DocumentRoot+self.path)
                    self.copyfile(f, self.wfile)
                    f.close()
                    return
                elif indexpage!="":
                    self.send_response(302)
                    self.send_header("Location", indexpage)
                    self.end_headers()
                    return
                else:
                    self.send_response(404)
                
            if self.path=='/favicon.ico':
                return
 
            path_parts = self.path.split('.')
            try:
                content_type=contentTypes[path_parts[-1]]
            except:
                if page404=="":
                    self.send_response(404)
                else:
                    self.send_response(302)
                    self.send_header("Location", page404)
                self.end_headers()


            if cgi_moudle=="on" and self.path.endswith(cgi_extensions):
                return CGIHTTPRequestHandler.do_GET(self)

            else:
                    
                #do static content
                f = open(DocumentRoot + sep + self.path) #self.path has /test.html
                #note that this potentially makes every file on your computer readable by the internet
                fs = os.fstat(f.fileno())


                Expirestype=Expires[-1:]
                Expirenum=Expires[:-1]
                
                #set Expires
                expiration = pubutil.get_http_expiry(Expirestype,int(Expirenum))

                #set max-age
                CACHE_MAX_AGE=pubutil.secs_from_days(ExpiresTypes[Expirestype],int(Expirenum))
                cache_control = 'public; max-age=%d' % (CACHE_MAX_AGE, )

                client_cache_cc = self.headers.getheader('Cache-Control')
                client_cache_p = self.headers.getheader('Pragma')
                Modified_Since= self.headers.getheader('If-Modified-Since')
                if client_cache_cc=='no-cache' or client_cache_p=='no-cache' or \
                  (client_cache_cc==None and client_cache_p==None and Modified_Since==None):
                    client_modified=None
                else:
                    try:
                        client_modified = Modified_Since.split(';')[0]
                    except:
                        client_modified=None
                file_last_modified=self.date_time_string(fs.st_mtime)

                if client_modified==file_last_modified:
                    self.send_response(304)
                    self.end_headers()
                else:
                    if gzip=="on":
                        compressed_content = pubutil.compressBuf(f.read(),compresslevel)
                    else:
                        compressed_content = f.read()
                    self.send_response(200)
                    self.send_header('Last-Modified', file_last_modified)
                    self.send_header('Cache-Control', cache_control) 
                    self.send_header('Expires', expiration)
                    self.send_header('Content-type',content_type)
                    if gzip=="on":
                        self.send_header('Content-Encoding','gzip')
                    self.send_header ("Content-Length", str(len(compressed_content)))
                    self.end_headers()
                    self.wfile.write(compressed_content)
                f.close()
                return

            return
        except IOError, e:
            logger.error(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+"-"+str(e))
            
     
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
  
    def do_POST(self):
        global rootnode
        try:
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                query=cgi.parse_multipart(self.rfile, pdict)
            self.send_response(200)
            self.end_headers()
            upfilecontent = query.get('upfile')
            print "filecontent", upfilecontent[0]
            self.wfile.write("<HTML>POST OK.<BR><BR>");
            self.wfile.write(upfilecontent[0]);
            
        except :
            pass

    def list_directory(self, path):

        try:
            list = os.listdir(path)
        except os.error:
            self.send_error(404, "No permission to list directory");
            return None
        list.sort(lambda a, b: cmp(a.lower(), b.lower()))
        f = StringIO()
        f.write("<h2>Directory listing for %s</h2>\n" % self.path)
        f.write("<hr>\n<ul>\n")
        f.write('<li><a href="%s">Parent Directory</a>\n' % (pubutil.parent_dir(self.path)))
        for name in list:
            fullname = os.path.join(path, name)
            displayname = name = cgi.escape(name)
            if os.path.islink(fullname):
                displayname = name + "@"
            elif os.path.isdir(fullname):
                displayname = name + "/"
                name = name + os.sep
            f.write('<li><a href="%s">%s</a>\n' % (name, displayname))
        f.write("</ul>\n<hr>\n")
        f.seek(0)
        return f

    def copyfile(self, source, outputfile):
        try:
            shutil.copyfileobj(source, outputfile)
        except KeyboardInterrupt,e:
            pass

    def log_message(self, format, *args):
        open(Logfile, "a").write("%s - - [%s] %s\n" %(self.address_string(),self.log_date_time_string(),format%args))

#mul-processsupport.
class ProcessHTTPServer(ForkingMixIn, HTTPServer):
    pass
    
#mul-thread support.
class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass
    
def main(HandlerClass = ServerHandler,ServerClass = SecureHTTPServer):
    try:
        try:
            if ssl=="on":
                server = (bind_ip, port)
            elif Multiprocess=="on":
                server = ProcessHTTPServer((bind_ip, port), ServerHandler)
            elif Multithreading=="on":
                server = ThreadedHTTPServer((bind_ip, port), ServerHandler)
            else:
                server = HTTPServer((bind_ip, port), ServerHandler)
            print 'Started yorserver...[OK]'
        except Exception,e:
            print str(e)
            logger.error(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+"-"+str(e))
            return
        if ssl=="on":
            httpd = ServerClass(server, ServerHandler)
            httpd.serve_forever()
        else:
            server.serve_forever()
    except KeyboardInterrupt,e:
        print '^C received, shutting down server'
        if ssl=="on":
            httpd.socket.close()
        else:
            server.socket.close()

if __name__ == '__main__':
    #定义命令行参数
    MSG_USAGE = "yorserver [-v][-h]"
    parser = OptionParser(MSG_USAGE)

    parser.add_option("-v","--version", action="store_true", dest="verbose",
            help="view yorserver version info.")
    opts, args = parser.parse_args()

    if opts.verbose:
        print "YorServer V1.0.1 beta."
        sys.exit();
    main()

