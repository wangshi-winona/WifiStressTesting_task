#! /usr/bin/python
import fcntl
import struct
import os
import inspect
curPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
def getId():
	file = open(curPath+'/../id.txt','r')
	return file.read().strip()

