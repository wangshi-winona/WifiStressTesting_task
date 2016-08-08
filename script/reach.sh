#! /bin/bash
# used to echo message back to control station when control station connect to pi
task=$1
curPath=$(cd "$(dirname "$0")";pwd)
line=$(head -n 1 ${curPath}'/../id.txt')
echo ${line}": "${task}
