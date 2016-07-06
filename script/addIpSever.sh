#! /bin/bash
curPath=$(cd "$(dirname "$0")";pwd)
source ${curPath}/../connection.conf
ssh-keyscan -p ${serverSshPort} ${serverIp} >> ~/.ssh/known_hosts
