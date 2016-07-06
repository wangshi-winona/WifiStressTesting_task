# /usr/bin/python
from selenium import webdriver
from pyvirtualdisplay import Display
import time
import sys
import json
import os
import inspect
from getId import getId
from datetime import datetime
from upload import http_post
display = Display(visible=0, size=(800,600))
display.start()

serverIp= sys.argv[1]
video=sys.argv[2]
eid=sys.argv[3]
location=sys.argv[4]
curPath=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
url="http://"+serverIp+"/video.html?video="+video
json_file=curPath+"/../log/video/"+str(int(time.time()))+".json"
log_file=curPath+"/../log/video/video_log"
with open (log_file,'a') as logfile:
	logfile.write("server: "+serverIp)
	logfile.write("video: "+video)
	logfile.write("jsonfile: "+json_file)
print getId() + ": launching driver (ts-"+str(int(time.time()))+")"
try:
	driver = webdriver.Firefox()
	print getId() + ": launched driver (ts-"+str(int(time.time()))+")"
except:
	print getId() + ": fail to launch driver"
	try:
		driver.close()
	finally:
		xdisplay.popen.terminate()
else:
	try:
		count = 0
		id=getId()
		dataobj={'piid':id,'eid':eid,'location':location,'type':'video','data':[],'timeStamp':str(int(time.time()))}
		print getId()+": streaming "+video
		logfile=open(log_file,'a')
		driver.get(url)
		while (buffer > '1' and count < 1800):
			bufferString = driver.find_element_by_id("buffer").get_attribute("innerHTML")
			ts=str(int(time.time()))
			tempArr=bufferString.split(' ')
			current=tempArr[0]
			bufferEnd=tempArr[1]
			buffer=tempArr[2]
			#print ts + "," + current + "," + bufferEnd + "," + buffer
			dataobj['data'].append({'timeStamp':ts,'current':current,'bufferEnd':bufferEnd,'buffer':buffer})
			logfile.write(ts+" current "+current+", bufferEnd "+bufferEnd+", buffer "+buffer+"\n")
			count = count +1
			time.sleep(1)
		logfile.close()
		delay = driver.find_element_by_id("delay").get_attribute("innerHTML")
		duration = driver.find_element_by_id("duration").get_attribute("innerHTML")
		print id+": video streaming ended"
		print id+": startDelay-" + delay + " duration-" + duration
		with open(log_file,'a') as logfile:
			logfile.write("id-"+id+" start delay-" + delay + " duration-" + duration+"\n")
		dataobj['startDelay']=delay
		dataobj['duration']=duration
		#print json.dumps(dataobj)
		with open(json_file,'wb') as outfile:
			json.dump(dataobj, outfile,indent=4)
		resp=http_post(json_file,'video')
		print getId()+": Server: "+resp
	except Exception as e:
		print getId() + ": video error "
		print str(e)
	finally:
		driver.close()
		display.popen.terminate()


