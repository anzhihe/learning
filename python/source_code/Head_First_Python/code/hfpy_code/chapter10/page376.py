
from google.appengine.ext import db

_FINS =   ['Falcate', 'Triangular', 'Rounded']
_WHALES = ['Humpback', 'Orca', 'Blue', 'Killer', 'Beluga', 'Fin', 'Gray', 'Sperm']
_BLOWS =  ['Tall', 'Bushy', 'Dense']
_WAVES =  ['Flat', 'Small', 'Moderate', 'Large', 'Breaking', 'High']

class Sighting(db.Model):
    name =       db.StringProperty()
    email =      db.StringProperty()
    date =       db.StringProperty()
    time =       db.StringProperty()
    location =   db.StringProperty(multiline=True)
    fin_type =   db.StringProperty(choices=_FINS)
    whale_type = db.StringProperty(choices=_WHALES)
    blow_type =  db.StringProperty(choices=_BLOWS)
    wave_type =  db.StringProperty(choices=_WAVES)
    which_user = db.UserProperty()

