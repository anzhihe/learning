#! /usr/local/bin/python3

import cgi
import sqlite3

import yate

print(yate.start_response('text/plain'))

form = cgi.FieldStorage()
the_id = form_data['Athlete'].value
the_time = form_data['Time'].value

connection = sqlite3.connect('coachdata.sqlite')
cursor = connection.cursor()
cursor.execute("INSERT INTO timing_data (athlete_id, value) VALUES (?, ?)",
                       (the_id, the_time))
connection.commit()
connection.close()

print('OK.')
