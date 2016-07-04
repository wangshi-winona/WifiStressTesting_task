#! /usr/bin/python
import fcntl
import struct

def getId():
	file = open('/home/pi/task/id.txt','r')
	return file.read().strip()

