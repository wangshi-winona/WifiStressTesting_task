# /usr/bin/python
# video streaming
# use selenium to open the video playing webpage and get the application qos data
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
timeLimit=int(sys.argv[3])
eid=sys.argv[4]
location=sys.argv[5]
curPath=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
url="http://"+serverIp+"/video.html?video="+video
json_file=curPath+"/../log/video/"+str(int(time.time()))+".json"
log_file=curPath+"/../log/video/video_log"

with open (log_file,'ab') as logfile:#log the video data to local
	logfile.write("server: "+serverIp)
	logfile.write("video: "+video)
	logfile.write("jsonfile: "+json_file)
#output message to console
print getId() + ": launching driver (ts-"+str(int(time.time()))+")"
try:
	driver = webdriver.Firefox()#launch firefox driver
	print getId() + ": launched driver (ts-"+str(int(time.time()))+")"
except:
	print getId() + ": fail to launch driver"
	try:
		driver.close()
	finally:
		xdisplay.popen.terminate()
else:
	count = 0
	id=getId()
	dataobj={'piid':id,'eid':eid,'location':location,'type':'video','data':[],'timeStamp':str(int(time.time()))}
	print getId()+": streaming "+video
	logfile=open(log_file,'ab')
	try:
		driver.get(url)
		while (buffer > '1' and count < timeLimit):#looping to get buffer level, etc. until the video ended or timeout
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
		with open(log_file,'ab') as logfile:
			logfile.write("id-"+id+" start delay-" + delay + " duration-" + duration+"\n")
		dataobj['startDelay']=delay
		dataobj['duration']=duration
		#print json.dumps(dataobj)
		with open(json_file,'wb') as outfile:
			json.dump(dataobj, outfile,indent=4)
		try:
			resp=http_post(json_file,'video')
			print getId()+": Server: "+resp
		except:
			print getId()+": upload exception"
	except Exception as e:
		print getId() + ": video error "
		print getId() + ": error msg: " + str(e)
	finally:
		driver.close()
		display.popen.terminate()


