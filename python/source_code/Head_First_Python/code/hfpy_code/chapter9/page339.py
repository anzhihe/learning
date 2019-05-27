#! /usr/local/bin/python3

import athletemodel
import yate

athletes = athletemodel.get_namesID_from_store()

print(yate.start_response())
print(yate.include_header("The NUAC's List of Athletes"))
print(yate.start_form("generate_timing_data.py"))
print(yate.para("Select an athlete from the list to work with:"))
for each_athlete in sorted(athletes):
    print(yate.radio_button_id("which_athlete", each_athlete[0], each_athlete[1]))
print(yate.end_form("Select"))
print(yate.include_footer({"Home": "/index.html"}))
