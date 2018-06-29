#!/bin/bash

# set parameters
input_dir="$1.rst"
pprev_file="$1.pprev"
sprev_file="$1.sprev"
summarydata_dir="/media/cuelee/cue_workspace/Project/RE3_CHL/01work_ldsc/analysis/01_ldsc_cors/data"
str_intercept="Intercept:"
software_dir="/media/cuelee/cue_workspace/software/ldsc"
work_dir="/media/cuelee/cue_workspace/Project/RE3_CHL/01work_ldsc/analysis/01_ldsc_cors/cue-work"

source /home/cuelee/anaconda2/bin/activate ldsc

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


# read a group IDs
list_array=""
## use dir_spe="*" if you want to test all groups in the directory 


# run analysis 
# we first define the sub_groups which denote the disease in a same category
for filename in "${input_dir}"
do

echo "Input:" $filename
	
	i=0
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
			echo "Cur_intercept: $cur_intercept"
		fi

		done < "${summarydata_dir}/${trait}.txt_ldsc.log"


	module load python/python3.6.5
	## run python to correct Z scores
	python3 /home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/codes/02_1_chisq-intercept_correction.py $trait $cur_intercept		

	## run munge.py
	$software_dir/munge_sumstats.py --sumstats $work_dir/${trait}.intCorrected --out $work_dir/${trait}.intCorrected --info INFO --a1 A1 --a2 A2 --snp SNP --ignore BETA,SE,OR --N-col N --N-cas-col N_CASE --N-con-col N_CONTROL --signed-sumstats Z,0 --merge-allele $software_dir/ldfile/eur_w_ld_chr/w_hm3.snplist
		
	## run ldsc
	$software_dir/ldsc.py --h2 $work_dir/${trait}.intCorrected.sumstats.gz --ref-ld-chr $software_dir/ldfile/eur_w_ld_chr/ --w-ld-chr $software_dir/ldfile/eur_w_ld_chr/ --pop-prev ${pprevs[$i]} --samp-prev ${sprevs[$i]} --out $work_dir/${trait}_ldsc 

	i=$(expr $i + 1)
	echo $trait ${pprevs[$i]} ${spprevs[$i]}

	done < "$filename"


done 

