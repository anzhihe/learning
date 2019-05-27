#!/usr/bin/env python

from os import curdir, sep, getcwd
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

# subclass BaseHTTPRequestHandler and support GET requests
class MyHandler(BaseHTTPRequestHandler):

    # handle GET request
    def do_GET(self):
        # check if we can read file and return it
        try:
            f = open(curdir + sep + self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()

        # if not, assume non-existent file
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)


def main():

    # attempt to start server
    try:
        # change directory if necessary by adding call to os.chdir()
        #os.chdir('/usr/local/httpd/htdocs')

        # create server
        server = HTTPServer(('', 80), MyHandler)
        print 'Welcome to the machine... hit ^C once or twice to quit'
        print 'cwd:', getcwd()

        # enter server loop
        server.serve_forever()

    # quit requested
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()


if __name__ == '__main__':
    main()
