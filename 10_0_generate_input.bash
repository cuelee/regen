#!/bin/bash

#######################3
## Created by Cue Hyunkyu Lee
## Date Dec 1 2017
##

## set parameters
work_dir="/media/cuelee/cue_workspace/Project/RE3_CHL/01work_ldsc/analysis/01_ldsc_cors/cue-work"
input_dir="/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/02_inputs"
output_dir="/media/cuelee/cue_workspace/Project/RE3_CHL/01work_ldsc/analysis/01_ldsc_cors/RE3_input"
software_dir="/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/codes"
h3snp_file="/media/cuelee/cue_workspace/software/ldsc/ldfile/eur_w_ld_chr/w_hm3.snplist"

set_name=$1

cur_input=$input_dir/$set_name.rst

traits_str=""
while read -r trait
do
	traits_str=$(echo $traits_str $trait)
done < $cur_input
read -a traits <<< "$traits_str"

module load python/python3.6.5
python3 $software_dir/10_1_generate_input.py $work_dir $output_dir/$set_name.zsa $h3snp_file $output_dir/$set_name.info ${traits[@]} ## zsa stands for Z scores array

