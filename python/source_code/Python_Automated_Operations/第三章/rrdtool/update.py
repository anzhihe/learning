# -*- coding: utf-8 -*-
#!/usr/bin/python
import rrdtool
import time,psutil
 
total_input_traffic = psutil.net_io_counters()[1]
total_output_traffic = psutil.net_io_counters()[0]
starttime=int(time.time())

update=rrdtool.updatev('/home/test/rrdtool/Flow.rrd','%s:%s:%s' % (str(starttime),str(total_input_traffic),str(total_output_traffic)))
print update 
