#! /usr/bin/python
import fcntl
import struct
import os
curPath = os.getcwd()
def getId():
	file = open(curPath+'/../id.txt','r')
	return file.read().strip()

