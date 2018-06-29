#!/bin/bash

group=$1
pval=$2
base_dir=$3
corr=$4
input_f=$3/$1.$2
newinput_f=$3/$1.$2.lcorr
code_dir="/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/codes"

#mv $input_f $newinput_f

module load python/python3.6.5
python3 $code_dir/15_1_run_analysis.py $input_f $newinput_f $corr $pval
