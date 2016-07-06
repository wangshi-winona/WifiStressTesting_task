#! /usr/bin/python
import subprocess
import json
import csv
import time
import sys
import linecache
import io
import os
import inspect
from random import randint
from getId import getId
from upload import http_post
interval=sys.argv[1]
repeat=sys.argv[2]
eid=sys.argv[3]
location=sys.argv[4]
curPath=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
link_file=curPath+"/links.txt"
json_file=curPath+"/../log/web/"+str(int(time.time()))+'.json'
log_file=curPath+"/../log/web/web_log"
def bash_command(cmd):
	proc=subprocess.Popen(['/bin/bash','-c', cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	return proc

dataobj={'type':'web','piid':getId(),'eid':eid,'location':location,'timeStamp':str(int(time.time())),'interval':interval,'repeat':repeat,'data':[]}

with open(link_file,'r') as f:
	link_num= sum(1 for _ in f)
resultStr=''
for i in range(0,int(repeat)):
	try:
		nthLine=randint(1,link_num)
		rand_link=linecache.getline(link_file,nthLine)
		#print nthLine
		cmd=bash_command('phantomjs '+curPath+'/../js/loadtime.js '+rand_link)
		out, err = cmd.communicate()
		print getId()+": browse "+str(i+1)
		with open(log_file,'a') as logfile:
			logfile.write(out)
		resultArr=out.strip().split(',')
		dataobj['data'].append({'timeStamp':str(resultArr[0]),'link':resultArr[1],'loadtime':resultArr[2]})
		time.sleep(float(interval))
	except:
		continue
with open(json_file,'wb') as outfile:
	json.dump(dataobj,outfile,indent=4) 
resp=http_post(json_file,'web')
print getId()+": Server: "+resp
