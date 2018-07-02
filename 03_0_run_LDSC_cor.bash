#!/bin/bash

## define parameters
input_dir="$1.rst"
data_dir="/media/cuelee/cue_workspace/Cue_sumstats/CTG_CNCR/analysis"
intcorr_dir="$data_dir/02_intcorr"
output_dir="$data_dir/03_genetic_corr"
software_dir="/media/cuelee/cue_workspace/software/ldsc"

## mkdir
mkdir -p $output_dir

## Load ldsc python environment using anaconda
source /home/cuelee/anaconda2/bin/activate ldsc

for filename in "${input_dir}"
do
	
i=0
echo "Input:" $filename
	
	## set list_array
	while read -r trait
	do
	
		list_array_in[i]=$intcorr_dir/$trait".intCorrected.sumstats.gz"
		list_array_out[i]=$output_dir/$trait".intCorrected.sumstats.gz"
		i=$(expr $i + 1) 
	done < "$filename"

	seq_array=($(seq 0 1 $(expr $i - 2)))

	#echo $list_array
	for index in ${seq_array[@]}
	do
		cur_set=("${list_array_in[@]:$index}")
		ldsc_input=$(echo ${cur_set[@]} | tr ' ' ,)
		
		## run LDSC
		$software_dir/ldsc.py --rg $ldsc_input --ref-ld-chr $software_dir/ldfile/eur_w_ld_chr/ --w-ld-chr $software_dir/ldfile/eur_w_ld_chr/ --out ${list_array_out[$index]}_ldscor

		
	done
	
done
 
