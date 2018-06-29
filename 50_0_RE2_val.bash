#!/bin/bash

REg_inpath=$1
RE2_inpath=$2
RE2_outpath=$3
code_dir=$4

echo $1 $2 $3 $4
module load python/python3.6.5

python3 $4/50_1_run_analysis.py $1 $2 $3 

