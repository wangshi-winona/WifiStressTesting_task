#! /usr/bin/python
import subprocess
import time
import os
from getId import getId
from getIp import get_ip_address
curPath = os.getcwd()
def bash_command(cmd):
	proc=subprocess.Popen(['/bin/bash','-c',cmd],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	return proc
cmd=curPath+'/../script/sendip.sh '+getId()+' '+get_ip_address('wlan0')
proc=bash_command(cmd)
out, err=proc.communicate()
print out
