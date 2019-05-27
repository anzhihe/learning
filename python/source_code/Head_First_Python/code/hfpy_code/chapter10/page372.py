
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.ext.webapp import template
from google.appengine.ext.db import djangoforms
from google.appengine.api import users

import hfwwgDB

class SightingForm(djangoforms.ModelForm):
    class Meta:
        model = hfwwgDB.Sighting
        exclude = ['which_user']

class SightingInputPage(webapp.RequestHandler):
    def get(self):
        html = template.render('templates/header.html', {'title': 'Report a Possible Sighting'})
        html = html + template.render('templates/form_start.html', {})
        html = html + str(SightingForm(auto_id=False))     
        html = html + template.render('templates/form_end.html', {'sub_title': 'Submit Sighting'})
        html = html + template.render('templates/footer.html', {'links': ''})
        self.response.out.write(html)

        
app = webapp.WSGIApplication([('/.*', SightingInputPage)], debug=True)

def main():
    run_wsgi_app(app)

if __name__ == '__main__':
    main()
