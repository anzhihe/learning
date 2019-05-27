import wsgiref.handlers

from google.appengine.ext import webapp

class IndexPage(webapp.RequestHandler):
    def get(self):
        pass

def main():
    app = webapp.WSGIApplication([('/.*', IndexPage)], debug=True)
    wsgiref.handlers.CGIHandler().run(app)

if __name__ == '__main__':
    main()
