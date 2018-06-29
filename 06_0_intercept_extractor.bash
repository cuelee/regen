#!/bin/bash

#################
## Created by Cue Hyunkyu Lee
## Date Nov 28 2017
##

## set parameters
meta_dir="/media/cuelee/cue_workspace/Project/RE3_CHL/01work_ldsc/analysis/01_ldsc_cors/meta-work"
input_dir=$1.rst
outname=$2
str_intercept="Intercept:"
code_dir="/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/codes"
ldsc_dir="/media/cuelee/cue_workspace/software/ldsc"
work_dir="/media/cuelee/cue_workspace/Project/RE3_CHL/01work_ldsc/analysis/01_ldsc_cors/cue-work"
cor_dir="/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/03_CorMat"

module load python/python3.6.5

## main function
traits_str=""
correlation_str=""
for filename in "${input_dir}"
do
		
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
#						python3 ${code_dir}/06_1_LS_intercept.py ${ldsc_dir} ${meta_dir} ${work_dir} ${traits[$i]} ${traits[$j]} $cur_intercept

					fi
				done < "${meta_dir}/${cur_pair}_ldsc.log"
			#break
			done		
		#break
		done

done

read -a intercepts <<< "$intercept_str"
python3 ${code_dir}/06_2_intercept_matrix.py ${cor_dir}/${outname}.RECor ${#traits[@]} ${intercepts[@]}

