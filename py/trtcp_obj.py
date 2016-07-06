#! /usr/bin/python
import sys
import linecache
from runtrtcp import runtrtcp
import os
import inspect
numOfObj=int(sys.argv[1])
N=sys.argv[2]
r=sys.argv[3]
eid=sys.argv[4]
location=sys.argv[5]
curPath=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
obj_file=curPath+'/testObj.txt'
lines=linecache.getlines(obj_file)
for i in range(0,numOfObj):
	runtrtcp(N,r,lines[i].strip(),eid,location)
