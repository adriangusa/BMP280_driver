#!/usr/bin/env python
import os
from datetime import datetime

temp = os.popen("/usr/local/bin/bmp280 | sed -n 1p | awk '{print $3}'").read()
#print "Temperature: ", temp

pressure = os.popen("/usr/local/bin/bmp280 | sed -n 2p | awk '{print $4}'").read()
#print "Pressure: ", pressure

current_date = datetime.utcnow()
#print "Date: ", current_date.isoformat()
id=current_date.strftime("%Y%m%d%H%M%S")
#print "ID: ",id

add_datapoint_cmd="curl -XPUT 'https://search-housepad-vqs646ktmrb3kkcxpowf7d7bn4.us-east-1.es.amazonaws.com/subtle/bmp280/"+id+"' -d '{\"temperature\": \""+temp+"\", \"pressure\": \""+pressure+"\", \"device\": \"bmp280\", \"timestamp\": \""+current_date.isoformat()+"\"}'"

add_datapoint_cmd=add_datapoint_cmd.replace("\n", "")

os.system(add_datapoint_cmd)
