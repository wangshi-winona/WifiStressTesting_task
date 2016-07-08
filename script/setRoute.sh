#! /bin/bash
#curPath=$(cd "$(dirname "$0")";pwd)
#source ${curPath}/../connection.conf
#echo $curPath
#echo $router
/sbin/route del -net 0.0.0.0 netmask 0.0.0.0 gw $1
/sbin/route del -net 0.0.0.0 netmask 0.0.0.0 gw $1
