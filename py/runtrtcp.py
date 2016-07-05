import subprocess
import sys
import csv
import json
import time
import os
from getId import getId
from upload import http_post
curPath = os.getcwd()
def bash_command(cmd):
	proc=subprocess.Popen(['/bin/bash','-c',cmd],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	return proc

def remove_last_line(s):
	return s[:s.rfind('\n')]

#N=sys.argv[1]
#r=sys.argv[2]
#obj=sys.argv[3]
#eid=sys.argv[4]
#location=sys.argv[5]

def runtrtcp(N,r,obj,eid,location):
	log_file=curPath+"/../log/trtcp/trtcp_log"
	id=getId()
	timeStamp=str(int(time.time()))
	dataobj={'piid':id,'eid':eid,'location':location,'type':'trtcp','timeStamp':timeStamp,'proberPerSec':N,'probeRate':r,'object':obj,'data':[]}
	json_file=curPath+'/../log/trtcp/'+timeStamp+'.json'
	cmd=bash_command('trtcp -l 0 -R -z 65535 -i wlan0 -S -N '+N+' -r '+r+' -O -C '+obj)
	out, err=cmd.communicate()
	print getId()+": trtcp object \""+obj+"\""
	with open(log_file,'a') as logfile:
		logfile.write(out)
	resultStr=remove_last_line(out.strip())
	#print resultStr
	fieldnames=('timeStamp','method','count','src','dst','size1','size2','recvSize1','recvSize2','ack','RTT1','RTT2','RTT3','TTL1','TTL2','TTL3','event')
	reader=csv.DictReader(resultStr.splitlines(),fieldnames)
	for row in reader:
		if not row['count']:
			continue
		dataobj['data'].append(row)
	with open(json_file,'wb') as outfile:
		json.dump(dataobj,outfile,indent=4)
	resp=http_post(json_file,'trtcp')
	print getId()+": Server: "+str(resp)
