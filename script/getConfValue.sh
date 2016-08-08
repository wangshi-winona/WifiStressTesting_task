#! /bin/bash
# echo the value of a certain variable in the configuration file
curPath=$(cd "$(dirname "$0")";pwd)
source ${curPath}/../connection.conf
#echo $curPath
field=$1
echo ${!field}
