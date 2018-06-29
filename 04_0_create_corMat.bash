#!/bin/bash

## define parameters
input_dir=$1.rst
outname=$2
output_dir="/media/cuelee/cue_workspace/Project/RE3_CHL/01work_ldsc/analysis/01_ldsc_cors/cue-work"
str_targetGC="Summary of Genetic Correlation Results"
corMat_dir="/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/03_CorMat/"

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
	python3 04_1_process.py ${corMat_dir}${outname}.GenCor ${list_array[@]}
	

done

	
	
