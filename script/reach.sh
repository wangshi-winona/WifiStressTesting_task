#! /bin/bash
task=$1
line=$(head -n 1 ${PWD}'/../id.txt')
echo ${line}": "${task}
