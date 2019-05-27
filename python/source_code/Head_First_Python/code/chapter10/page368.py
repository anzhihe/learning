
from google.appengine.ext import db

class BirthDetails(db.Model):
    name =          db.StringProperty()
    date_of_birth = db.DateProperty()
    time_of_birth = db.TimeProperty()

