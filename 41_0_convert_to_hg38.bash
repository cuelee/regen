#!/bin/bash

##########################
## Created by Cue Hyunkyu Lee
## Date Jan 17 2018
##

## get inputs 
file_name=$1;
result_dir="/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/04_result";
code_dir="/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/codes"

## run analysis
module load python/python3.6.5
python3 $code_dir/41_1_run_analysis.py $file_name $result_dir
