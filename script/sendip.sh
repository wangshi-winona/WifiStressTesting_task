#! /bin/bash
# send id and ip to ip server
# called by reg_pi.py
# only used in wireless control
curPath=$(cd "$(dirname "$0")";pwd)
source ${curPath}/../connection.conf
id=$1
ip=$2
sshpass -p ${ipServerPwd} ssh ${ipServerHostName}@${ipServerIp} -p ${ipServerSshPort} ${ipServerIpPath}/reg.py $id $ip
