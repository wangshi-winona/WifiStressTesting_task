#! /bin/bash
curPath=$(cd "$(dirname "$0")";pwd)
source ${curPath}/../connection.conf
#echo $curPath
#echo $router
sleep 3
route del -net 0.0.0.0 netmask 0.0.0.0 gw $router
