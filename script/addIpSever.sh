#! /bin/bash
source ${PWD}/../connection.conf
ssh-keyscan -p ${serverSshPort} ${serverIp} >> ~/.ssh/known_hosts
