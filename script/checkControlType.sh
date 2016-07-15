#! /bin/bash
curPath=$(cd "$(dirname "$0")";pwd)
source ${curPath}/../connection.conf
if ${controlUsingWireless}; then
	${curPath}/../py/reg_pi.py
else
	${curPath}/delDefaultRoute.sh
fi
