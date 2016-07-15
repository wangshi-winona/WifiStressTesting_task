#! /usr/bin/python
import fcntl
import struct
import os
import inspect
curPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
def getDataServer():
	file = open(curPath+'/../dataServer.txt','r')
	return file.read().strip()

