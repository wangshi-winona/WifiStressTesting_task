#! /bin/bash
# add ip server to known host file
curPath=$(cd "$(dirname "$0")";pwd)
source ${curPath}/../connection.conf
ssh-keyscan -p ${ipServerSshPort} ${ipServerIp} >> ~/.ssh/known_hosts
