
import android
import json
import time

from urllib import urlencode
from urllib2 import urlopen

hello_msg     = "Welcome to Coach Kelly's Timing App"
list_title    = 'Here is your list of athletes:'
quit_msg      = "Quitting Coach Kelly's App."

web_server    = 'http://192.168.1.33:8080'

get_names_cgi = '/cgi-bin/generate_names.py'
get_data_cgi  = '/cgi-bin/generate_data.py'

def send_to_server(url, post_data=None):
    if post_data:
        page = urlopen(url, urlencode(post_data))
    else:
        page = urlopen(url)
    return(page.read().decode("utf8"))

app = android.Android()

def status_update(msg, how_long=2):
    app.makeToast(msg)
    time.sleep(how_long)

status_update(hello_msg)

athletes = sorted(json.loads(send_to_server(web_server + get_names_cgi)))

athlete_names = [ath[0] for ath in athletes]
 
app.dialogCreateAlert(list_title)
app.dialogSetSingleChoiceItems(athlete_names)
app.dialogSetPositiveButtonText('Select')
app.dialogSetNegativeButtonText('Quit')
app.dialogShow()
resp = app.dialogGetResponse().result

if resp['which'] in ('positive'):
    selected_athlete = app.dialogGetSelectedItems().result[0]
    which_athlete = athletes[selected_athlete][1]

    athlete = json.loads(send_to_server(web_server + get_data_cgi,
                                    {'which_athlete': which_athlete}))


    athlete_title = athlete['Name'] + ' (' + athlete['DOB'] + '), top 3 times:'
    app.dialogCreateAlert(athlete_title)
    app.dialogSetItems(athlete['top3'])
    app.dialogSetPositiveButtonText('OK')
    # Need to add another button to add a timing value.
    app.dialogSetNegativeButtonText('Add Time')
    app.dialogShow()
    resp = app.dialogGetResponse().result

    if resp['which'] in ('positive'):
        pass
    elif resp['which'] in ('negative'):

        timing_title  = 'Enter a new time'
        timing_msg    = 'Provide a new timing value ' + athlete['Name'] + ': '
        add_time_cgi  = '/cgi-bin/add_timing_data.py'
        
        resp = app.dialogGetInput(timing_title, timing_msg).result
        if resp is not None:
            new_time = resp
            send_to_server(web_server + add_time_cgi,
                               {'Time': new_time,
                                'Athlete': which_athlete})
        

status_update(quit_msg)
