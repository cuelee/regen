#!/bin/bash

var_name=$1
var_chr=$2
var_bp=$3
base_dir=$4
omv_dir=$5
code_dir=$6
RE3in_path=$7
var_range=$8
RE3des_path=$9
autoimmune_list=${10}
RE2des_path=${11}
LSdes_path=${12}
cur_i=${13}

module load python/python3.6.5
python3 $code_dir/42_1_run_analysis.py $1 $2 $3 $8 $4 $5 $6 $7 $9 ${10} ${11} ${12} ${13}

