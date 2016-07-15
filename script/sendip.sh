#! /bin/bash
curPath=$(cd "$(dirname "$0")";pwd)
source ${curPath}/../connection.conf
id=$1
ip=$2
sshpass -p ${ipServerPwd} ssh ${ipServerHostName}@${ipServerIp} -p ${ipServerSshPort} ${ipServerIpPath}/reg.py $id $ip
