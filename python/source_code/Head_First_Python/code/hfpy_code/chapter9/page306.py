
import android

from urllib import urlencode
from urllib2 import urlopen

server_title  = 'Which server should I use?'
server_msg    = "Please confirm the server address/name to use for your athlete's timing data:"

timing_title  = 'Enter data'
timing_msg    = 'Provide a new timing value:'

web_server    = 'http://192.168.1.33:8080'

add_time_cgi  = '/cgi-bin/add_timing_data.py'

app = android.Android()

def send_to_server(url, post_data=None):
    if post_data:
        page = urlopen(url, urlencode(post_data))
    else:
        page = urlopen(url)
    return(page.read().decode("utf8"))

resp = app.dialogGetInput(server_title, server_msg, web_server).result

if resp is not None:
    web_server = resp
    resp = app.dialogGetInput(timing_title, timing_msg).result
    if resp is not None:
        new_time = resp
        send_to_server(web_server + add_time_cgi, {'TimingValue': new_time})
