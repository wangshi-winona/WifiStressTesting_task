#! /bin/bash
curPath=$(cd "$(dirname "$0")";pwd)
source ${curPath}/../controlUsingWireless.conf
id=$1
ip=$2
sshpass -p 'user' ssh user@${ipServerIp} -p ${ipServerSshPort} ${ipServerIpPath}/reg.py $id $ip
