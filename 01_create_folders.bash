#!bin/bash

base_dir="/media/cuelee/cue_workspace/Project/RE3_CHL/01work_ldsc"
data_dir="${base_dir}/analysis/01_ldsc_cors/data"


input_dir="$1.rst"

echo ${input_dir}
#we only do analysis on autoimmune set


#create a data-analysis folder
mkdir -p $data_dir

for filename in "${input_dir}"
do

echo $name

	while read -r line 
	do
		cp $base_dir/temp/$line* $data_dir/
	done < "$filename"

done

	
