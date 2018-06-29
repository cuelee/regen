#!/bin/bash

###################
## Created by Cue Hyunkyu Lee
## Updated by Jan 17 2018
## 

## Define parameters
catalog_dir="/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/10_GWAScatalog"
TG_dir="/media/cuelee/cue_workspace/1000G/work/raw_ped"
output_dir=$catalog_dir
code_dir="/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/codes"


## run python
module load python/python3.6.5
python3 $code_dir/41_1_run_analysis.py ${catalog_dir}/snp_list.txt ${TG_dir}/1000G_Phase3_RSID.txt 
