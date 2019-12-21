import datetime
import time
tm = datetime.datetime(2017, 7, 8, 8, 27, 0)
while datetime.datetime.now() < tm:
    time.sleep(1)
print('Done')