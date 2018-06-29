#!/bin/bash

#########################
## Created by Cue Hyunkyu Lee
## Date Jan 31 2018
##

group=$1
pval=$2
base_dir=$3
code_dir="/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/codes"

module load python/python3.6.5
python3 $code_dir/22_1_run_analysis.py $1 $2 $3 $3/$1_GWS_$2.cat $3/$1_GWS.$2.pruned_hg38 $3/$1_GWS_$2.exact $3/$1_GWS_$2.ld $3/$1_GWS_$2.novel
