#!/bin/bash

###########################
## Created by Cue Hyunkyu Lee
## Date Jan 26 2018
## 

## set parameters
group=$1
pvalue_name=$2
result_dir=$3 
code=$0
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
gwfile=${result_dir}/${group}_GWS.${pvalue_name}.pruned_hg38
tg_path="/media/cuelee/cue_workspace/1000G/work/raw_ped"
plink_path="/media/cuelee/cue_workspace/software/plink_linux_x86_64/plink"
catsnp_list="/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/10_GWAScatalog/catalogIn1000G.txt"

echo "Current inputs are:"
echo "		GWAS_GWSfile: ${gwfile}"
echo "		1000G_path: ${tg_path}"
echo "		Plink_path: ${plink_path}"

module load python/python3.6.5
python3 $DIR/21_1_run_analysis.py $group $pvalue_name $result_dir $gwfile $tg_path $plink_path $catsnp_list 
