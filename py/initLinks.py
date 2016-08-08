#! /usr/bin/python
import subprocess
import sys
import io
import os
import inspect
from getId import getId
from addLinks import add_links
curPath=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
link_file=curPath+"/links.txt"
with open(link_file,'wb') as f:
	f.truncate()
	print getId()+': Truncated links.txt'
add_links('wifi')
add_links('raspberry pi')
add_links('stress testing')
add_links('fedora')
add_links('computer networking')
add_links('polyu')
add_links('department of computing')
add_links('internet infrastructure')
add_links('network monitoring')
add_links('quality of service')
add_links('phantomjs')
add_links('selenium')
add_links('firefox')
add_links('ssh')
add_links('client server')

