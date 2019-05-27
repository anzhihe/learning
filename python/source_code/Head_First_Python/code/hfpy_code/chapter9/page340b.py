#! /usr/local/bin/python3

import cgi
import json
import athletemodel
import yate

form_data = cgi.FieldStorage()
athlete_id = form_data['which_athlete'].value
athlete = athletemodel.get_athlete_from_id(athlete_id)

print(yate.start_response('application/json'))
print(json.dumps(athlete))

