#! /usr/bin/python
# wifi quality
# grep the wlan0 interface information at intervals
import subprocess
import sys
import time
import json
import os
import inspect
import re
from upload import http_post
from getId import getId
interval=sys.argv[1]
repeat=sys.argv[2]
eid=sys.argv[3]
location=sys.argv[4]
piid=getId()
timeStamp=str(int(time.time()))
curPath=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
log_file=curPath+'/../log/quality/quality_log'
json_file=curPath+'/../log/quality/'+timeStamp+'.json'
def bash_command(cmd):
        proc=subprocess.Popen(['/bin/bash','-c', cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return proc

dataobj={'type':'quality', 'piid':piid, 'eid':eid, 'location':location, 'timeStamp':timeStamp, 'interval':interval, 'repeat': repeat, 'data':[]}
for i in range(0,int(repeat)):#repeat a certain number of times to grep the wifi info
	proc=bash_command('iwconfig wlan0 | grep -i quality')
	out, err = proc.communicate()
	ts=str(int(time.time()))
	qualityArr=re.split('\W+',out.strip())
	link=qualityArr[2]+'/'+qualityArr[3]
	signal=qualityArr[6]+'/'+qualityArr[7]
	noise=qualityArr[10]+'/'+qualityArr[11]
	#qualityArr=out.strip().split('  ')
	#link=qualityArr[0].split('=')[1]
	#signal=qualityArr[1].split('=')[1]
	#noise=qualityArr[2].split('=')[1]
	dataobj['data'].append({'timeStamp':ts, 'linkQuality':link, 'signal':signal, 'noise':noise})
	print getId()+": "+ts+" logging wifi quality"
	with open(log_file,'ab') as f:
		f.write(ts+' '+out.strip()+'\n')
	time.sleep(int(interval))
with open(json_file,'wb') as f:
	json.dump(dataobj,f,indent=4)
try:
	resp=http_post(json_file,'quality')
	print getId()+': Server: '+resp
except:
	print getId()+': upload exception'
