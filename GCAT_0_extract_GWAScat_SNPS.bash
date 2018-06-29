#!/bin/bash

###################
## Created by Cue Hyunkyu Lee
## Updated by Jan 17 2018
## 

## Define parameters
catalog_dir="/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/10_GWAScatalog"
output_dir=$catalog_dir
code_dir="/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/codes"


## run python
module load python/python3.6.2
python3 $code_dir/40_1_run_analysis.py ${code_dir} ${catalog_dir}/gwas_catalog_v1.0.1-associations_e91_r2018-01-01.tsv  
