#! /bin/bash
id=$1
ip=$2
sshpass -p 'userpw' ssh user@158.132.255.20 -p 12422 sudo /home/user/videoStreamHttp/initializr/ip/reg.py $id $ip
