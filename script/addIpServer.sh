#! /bin/bash
curPath=$(cd "$(dirname "$0")";pwd)
source ${curPath}/../controlUsingWireless.conf
ssh-keyscan -p ${ipServerSshPort} ${ipServerIp} >> ~/.ssh/known_hosts
