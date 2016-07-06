#! /bin/bash
source ${PWD}/../connection.conf
id=$1
ip=$2
sshpass -p 'userpw' ssh user@${serverIp} -p ${serverSshPort} sudo ${serverIpPath}/reg.py $id $ip
