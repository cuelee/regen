#!/bin/bash

input=$1
output=$2
basedir=$3
codedir=$4
veppath=$5
vepargv=$6

module load python/python3.6.5
python3 $4/30_1_run_analysis.py $1 $2 $3 $5 $6

