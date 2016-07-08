#! /usr/bin/python
import subprocess
def bash_command(cmd):
        proc=subprocess.Popen(['/bin/bash','-c', cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return proc
proc=bash_command('iwconfig wlan0 | grep -i quality')
out, err = proc.communicate()
qualityArr=out.strip().split('  ')
print qualityArr
