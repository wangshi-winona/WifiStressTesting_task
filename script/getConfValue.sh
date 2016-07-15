#! /bin/bash
curPath=$(cd "$(dirname "$0")";pwd)
source ${curPath}/../connection.conf
#echo $curPath
field=$1
echo ${!field}
