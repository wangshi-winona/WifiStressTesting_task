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
#add_links('raspberry pi')
#add_links('stress testing')
#add_links('fedora')
