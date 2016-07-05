import urllib
import urllib2
import json
from getId import getId

def http_post(filePath,type):
	try:
		if type=='web':
			url='http://158.132.255.20:12480/data/web'
		elif type=='video':
			url='http://158.132.255.20:12480/data/video'
		elif type =='trtcp':	
			url='http://158.132.255.20:12480/data/trtcp'
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
