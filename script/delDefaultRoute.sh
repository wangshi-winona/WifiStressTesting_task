#! /bin/bash
curPath=$(cd "$(dirname "$0")";pwd)
source ${curPath}/../connection.conf
/sbin/route del -net 0.0.0.0 netmask 0.0.0.0 gw $router
/sbin/route del -net 0.0.0.0 netmask 0.0.0.0 gw $router
