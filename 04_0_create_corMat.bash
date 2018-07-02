#!/bin/bash

## define parameters
input_dir=$1.rst
outname=$2
data_dir="/media/cuelee/cue_workspace/Cue_sumstats/CTG_CNCR/analysis"
result_dir="/media/cuelee/cue_workspace/Cue_sumstats/CTG_CNCR/result"
output_dir="$data_dir/03_genetic_corr"
corMat_dir="$result_dir/02_corrMats"

mkdir -p $corMat_dir

for filename in "${input_dir}"
do

	i=0
	echo "Input:" $filename

	## set list_array
	while read -r trait
	do
	
	list_array[i]=$output_dir/$trait".intCorrected.sumstats.gz_ldscor.log"
	i=$(expr $i + 1)	

	done < "$filename"
	
	module load python/python3.6.5 
	python3 04_1_process.py ${corMat_dir}/${outname}.GenCor ${list_array[@]}
	

done

	
	
