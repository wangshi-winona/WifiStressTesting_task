#! /usr/bin/python
import urllib
import urllib2
import json
import subprocess
import os
import inspect
from getId import getId
curPath=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
def bash_command(cmd):
	proc=subprocess.Popen(['/bin/bash','-c',cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	return proc
cmd=bash_command(curPath+'/../script/getConfValue.sh dataServerIp')
out, err=cmd.communicate()
dataServerIp=out.strip()
cmd=bash_command(curPath+'/../script/getConfValue.sh dataServerPort')
out, err=cmd.communicate()
dataServerPort=out.strip()
base=url='http://'+dataServerIp+':'+dataServerPort

def http_post(filePath,type):
	try:
		if type=='web':
			url=base+'/data/web'
		elif type=='video':
			url=base+'/data/video'
		elif type =='trtcp':	
			url=base+'/data/trtcp'
		elif type =='quality':
			url=base+'/data/quality'
		else:
			return 'invalid type'
		with open(filePath,'r') as f:
			data=json.load(f)
		json_data=json.dumps(data)
		#print json_data
		print getId() + ": upload to " + url
		req=urllib2.Request(url)
		response=urllib2.urlopen(req,json_data)
		return response.read()
	except:
		print getId() + ": upload error"
