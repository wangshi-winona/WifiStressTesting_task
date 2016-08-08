#! /usr/bin/python
# trtcp
# read the object/target from the list and call runtrtcp.py
import sys
import linecache
from runtrtcp import runtrtcp
import os
import inspect
import time
import sched
schedule=sched.scheduler(time.time,time.sleep)
numOfObj=int(sys.argv[1])
N=sys.argv[2]
r=sys.argv[3]
eid=sys.argv[4]
location=sys.argv[5]
curPath=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
obj_file=curPath+'/testObj.txt'
lines=linecache.getlines(obj_file)
for i in range(0,numOfObj):
	schedule.enter(i*10,0,runtrtcp,(N,r,lines[i].strip(),eid,location))
schedule.run()	
