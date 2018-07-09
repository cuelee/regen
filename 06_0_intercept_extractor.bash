#!/bin/bash

#################
## Created by Cue Hyunkyu Lee
## Date Nov 28 2017
##

## Load ldsc python environment using anaconda
source /home/cuelee/anaconda2/bin/activate ldsc

## set parameters
data_dir="/media/cuelee/cue_workspace/Cue_sumstats/CTG_CNCR/analysis"
result_dir="/media/cuelee/cue_workspace/Cue_sumstats/CTG_CNCR/result"
meta_dir="$data_dir/04_FE_inputs"
cor_dir="$result_dir/02_corrMats"
input_dir=$1.rst
outname=$2
str_intercept="Intercept:"
code_dir="/media/cuelee/cue_workspace/Cue_sumstats/CTG_CNCR/codes"
ldsc_dir="/media/cuelee/cue_workspace/software/ldsc"
work_dir="$data_dir/02_intcorr"

parallel_input="${code_dir}/06_3_run_06_1.txt"
rm $parallel_input
touch ${parallel_input};

module load python/python3.6.5

## main function
traits_str=""
correlation_str=""
filename="${input_dir}"
	
while read -r trait
do		
	traits_str=$(echo $traits_str $trait)
	i=$(expr $i + 1)
done < "$filename"

read -a traits <<< "$traits_str"
echo "Input traits are: " ${traits[@]}

is=($(seq 0 $(expr ${#traits[@]} - 2))) 
for i in ${is[@]}
do
	js=($(seq $(expr $i + 1) $(expr ${#traits[@]} - 1)))
	for j in ${js[@]}
	do
		cur_pair=${traits[$i]}_${traits[$j]}
		echo "The cur_traits is : " $cur_pair

		while read -r line 
		do	
			if echo "$line" | grep -q "$str_intercept"
			then
				read -a line2array <<< "$line"
		 		cur_intercept=${line2array[1]}
				echo "The Intercept of LDSC: " $cur_intercept
				intercept_str=$(echo $intercept_str $cur_intercept)
				echo "${code_dir}/06_1_LS_intercept.py ${meta_dir} ${work_dir} ${traits[$i]} ${traits[$j]} T $cur_intercept" >> $parallel_input
			fi
		done < "${meta_dir}/${cur_pair}_ldsc.log"

	done		
done

cat $parallel_input | parallel --jobs 7 --colsep ' ' python3 {1} {2} {3} {4} {5} {6} {7}
rm $parallel_input
exit
is=($(seq 0 $(expr ${#traits[@]} - 2))) 
for i in ${is[@]}
do
	js=($(seq $(expr $i + 1) $(expr ${#traits[@]} - 1)))
	for j in ${js[@]}
	do
		cur_pair=${traits[$i]}_${traits[$j]}
		echo "The cur_traits is : " $cur_pair

		output_filename="$meta_dir/${traits[$i]}_${traits[$j]}.intCorrected"
		$ldsc_dir/munge_sumstats.py --merge-allele $ldsc_dir/ldfile/eur_w_ld_chr/w_hm3.snplist --sumstats $output_filename --out $output_filename
		$ldsc_dir/ldsc.py --h2 $output_filename.sumstats.gz --ref-ld-chr $ldsc_dir/ldfile/eur_w_ld_chr/ --w-ld-chr $ldsc_dir/ldfile/eur_w_ld_chr/ --out $output_filename_ldsc 

	done		
done


read -a intercepts <<< "$intercept_str"
python3 ${code_dir}/06_2_intercept_matrix.py ${cor_dir}/${outname}.RECor ${#traits[@]} ${intercepts[@]}

