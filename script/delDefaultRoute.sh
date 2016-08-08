#! /bin/bash
# delete the default route of ethernet in routing table to prevent the user task using ethernet
# only used in ethernet control
curPath=$(cd "$(dirname "$0")";pwd)
source ${curPath}/../connection.conf
/sbin/route del -net 0.0.0.0 netmask 0.0.0.0 gw $router
/sbin/route del -net 0.0.0.0 netmask 0.0.0.0 gw $router
