import wsgiref.handlers

from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.ext.webapp import template

from google.appengine.ext.db import djangoforms

import birthDB

class BirthDetailsForm(djangoforms.ModelForm):
    class Meta:
        model = birthDB.BirthDetails

class SimpleInput(webapp.RequestHandler):
    def get(self):
        html = template.render('templates/header.html', {'title': 'Provide your birth details'})
        html = html + template.render('templates/form_start.html', {})
        html = html + str(BirthDetailsForm(auto_id=False))     
        html = html + template.render('templates/form_end.html', {'sub_title': 'Submit Details'})
        html = html + template.render('templates/footer.html', {'links': ''})
        self.response.out.write(html)

def main():
    app = webapp.WSGIApplication([('/.*', SimpleInput)], debug=True)
    wsgiref.handlers.CGIHandler().run(app)

if __name__ == '__main__':
    main()

    
