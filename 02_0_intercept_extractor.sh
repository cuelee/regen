#!/bin/bash

# set parameters
input_dir="$1.rst"
data_dir="/media/cuelee/cue_workspace/Cue_sumstats/CTG_CNCR/analysis"
summarydata_dir="$data_dir/01_raw_ldsc"
work_dir="$data_dir/02_intcorr"
str_intercept="Intercept:"
software_dir="/media/cuelee/cue_workspace/software/ldsc"
code_dir="/media/cuelee/cue_workspace/Cue_sumstats/CTG_CNCR/codes"

## Load LDSC python environment using anaconda
source /home/cuelee/anaconda2/bin/activate ldsc

# run analysis 
# we first define the sub_groups which denote the disease in a same category
for filename in "${input_dir}"
do

echo "Input:" $filename
	
	## run analysis to each test
	while read -r trait
	do
		echo $trait
		## This for loop can cath the strings delimited by a single space.
		#for line in $(cat ${summarydata_dir}/${trait}.af.aa.sumstats_CHL_ldsc.log)
		#do
		#echo $line
		#done
			
		## read intercept. 
		while read -r line
		do
		
		if echo "$line" | grep -q "$str_intercept"; then
			read -a line2array <<< "$line"
			cur_intercept="${line2array[1]}"
			echo
			echo "intercept for $trait: $cur_intercept"
		fi

		done < "${summarydata_dir}/${trait}.txt_ldsc.log"

	module load python/python3.6.5
	## run python to correct Z scores
	python3 $code_dir/02_1_chisq-intercept_correction.py $trait $data_dir $cur_intercept		

	## generate sumstats.txt.gz using munge.py
	$software_dir/munge_sumstats.py --sumstats $work_dir/${trait}.intCorrected --out $work_dir/${trait}.intCorrected --info INFO --a1 A1 --a2 A2 --snp SNP --ignore BETA,SE,OR --N-col N --signed-sumstats Z,0 --merge-allele $software_dir/ldfile/eur_w_ld_chr/w_hm3.snplist
		
	## validate ldsc intercept :== 1
	$software_dir/ldsc.py --h2 $work_dir/${trait}.intCorrected.sumstats.gz --ref-ld-chr $software_dir/ldfile/eur_w_ld_chr/ --w-ld-chr $software_dir/ldfile/eur_w_ld_chr/ --out $work_dir/${trait}_ldsc 

	done < "$filename"

done 
