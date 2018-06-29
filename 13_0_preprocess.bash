#!/bin/bash

#######################
## Created by Cue Hyunkyu Lee
## Date Dec 02 2017
##

## set parameters
h3snp_dir="/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/05_analysis"
code_dir="/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/codes"
input_name=$1
output_name=$2
pvalue_name=$3
outfile_name=$4

module load python/python3.6.5
python3 $code_dir/13_1_preprocess.py $h3snp_dir $input_name $output_name $pvalue_name $outfile_name
