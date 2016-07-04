#! /bin/bash
task=$1
line=$(head -n 1 '/home/pi/task/id.txt')
echo ${line}": "${task}
