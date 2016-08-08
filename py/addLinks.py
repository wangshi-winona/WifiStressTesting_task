#! /usr/bin/python
import subprocess
import sys
import io
import os
import inspect
from getId import getId
curPath=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
link_file=curPath+"/links.txt"
def bash_command(cmd):
	proc=subprocess.Popen(['/bin/bash','-c', cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	return proc
def add_links(keyword):	
	cmd=bash_command('phantomjs '+curPath+'/../js/getLinks.js '+keyword)
	out, err = cmd.communicate()
	print getId()+": Google Search '"+keyword+"'"
	with open(link_file,'a') as f:
		f.write(out.strip())
		f.write('\n')
	print "Added links for '"+keyword+"'"
	print out.strip()
	print err
