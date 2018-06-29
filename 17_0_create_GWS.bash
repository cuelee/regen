#!/bin/bash

group=$1
pval=$2
base_dir=$3
gthres=$4
ntest=$5
lcorr="$3/$1.$2.lcorr"
#lcorr="$3/$1.$2"
out="$3/$1_GWS.$2"
code_dir="/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/codes"

module load python/python3.6.5
python3 $code_dir/17_1_run_analysis.py $1 $2 $3 $lcorr $out $4 $5
