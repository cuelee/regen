#!/bin/bash


curchr=$1
curbp=$2
catsnp_listf=$3
codedir=$4
noveldir=$5
distthre=$6

## run module environments
module load python/python3.6.5
python3 ${4}80_1_run_analysis.py $1 $2 $3 $5 $6

