#!/bin/bash

#######################3
## Created by Cue Hyunkyu Lee
## Date Dec 1 2017
##

## set parameters
result_dir="/media/cuelee/cue_workspace/Cue_sumstats/CTG_CNCR/result"
data_dir="/media/cuelee/cue_workspace/Cue_sumstats/CTG_CNCR/analysis"
work_dir="$data_dir/02_intcorr"
input_dir="$result_dir/01_input"
output_dir="$data_dir/05_reGinput"
code_dir="/media/cuelee/cue_workspace/Cue_sumstats/CTG_CNCR/codes"
h3snp_file="/media/cuelee/cue_workspace/Pasaniuc_sumstats/Nov2017_Huwenbo/1000G_SNP_CHR_BP_A1_A2.txt"

mkdir -p $output_dir

set_name=$1

cur_input=$input_dir/$set_name.rst

traits_str=""
while read -r trait
do
	traits_str=$(echo $traits_str $trait)
done < $cur_input
read -a traits <<< "$traits_str"

module load python/python3.6.5
python3 $code_dir/10_1_generate_input.py $work_dir $output_dir/$set_name.zsa $h3snp_file $output_dir/$set_name.info ${traits[@]} ## zsa stands for Z scores array

