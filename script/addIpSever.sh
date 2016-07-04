#! /bin/bash
server=$1
port=$2
ssh-keyscan -p $port $server >> ~/.ssh/known_hosts
