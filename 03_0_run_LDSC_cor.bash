#!/bin/bash

## define parameters
input_dir="$1.rst"
pprev_file="$1.pprev"
sprev_file="$1.sprev"
output_dir="/media/cuelee/cue_workspace/Project/RE3_CHL/01work_ldsc/analysis/01_ldsc_cors/cue-work"

i=0
while IFS='' read -r line || [[ -n "$line" ]]; do
        pprevs[i]=$line;
        i=$(expr $i + 1)
done < $pprev_file
echo ${pprevs[@]}

i=0
while IFS='' read -r line || [[ -n "$line" ]]; do
        sprevs[i]=$line;
        i=$(expr $i + 1)
done < $sprev_file
echo ${sprevs[@]}


## need use anaconda env
source /home/cuelee/anaconda2/bin/activate ldsc

for filename in "${input_dir}"
do
	
i=0
echo "Input:" $filename
	
	## set list_array
	while read -r trait
	do
	
		list_array[i]=$output_dir/$trait".intCorrected.sumstats.gz"
		i=$(expr $i + 1) 
	done < "$filename"

	seq_array=($(seq 0 1 $(expr $i - 2)))

	#echo $list_array
	for index in ${seq_array[@]}
	do
		cur_set=("${list_array[@]:$index}")
		ldsc_input=$(echo ${cur_set[@]} | tr ' ' ,)
		cur_pprev_set=("${pprevs[@]:$index}")
		pprev_input=$(echo ${cur_pprev_set[@]} | tr ' ' ,)
		cur_sprev_set=("${sprevs[@]:$index}")
		sprev_input=$(echo ${cur_sprev_set[@]} | tr ' ' ,)
		
		## run LDSC
		/media/cuelee/cue_workspace/software/ldsc/ldsc.py --rg $ldsc_input --ref-ld-chr /media/cuelee/cue_workspace/software/ldsc/ldfile/eur_w_ld_chr/ --w-ld-chr /media/cuelee/cue_workspace/software/ldsc/ldfile/eur_w_ld_chr/ --pop-prev $pprev_input --samp-prev $sprev_input --out ${list_array[$index]}_ldscor

		
	done
	
done
 
