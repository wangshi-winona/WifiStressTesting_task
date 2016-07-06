#! /bin/bash
task=$1
curPath=$(cd "$(dirname "$0")";pwd)
line=$(head -n 1 ${curPath}'/../id.txt')
echo ${line}": "${task}
