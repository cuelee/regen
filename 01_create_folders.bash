#!bin/bash

raw_dir="/media/cuelee/cue_workspace/Cue_sumstats/CTG_CNCR/1_processed"
data_dir="/media/cuelee/cue_workspace/Cue_sumstats/CTG_CNCR/analysis"
rawldsc_dir="$data_dir/01_raw_ldsc"


input_dir="$1.rst"

echo ${input_dir}
#we only do analysis on autoimmune set


#create a data-analysis folder
mkdir -p $rawldsc_dir

for filename in "${input_dir}"
do

echo $name

	while read -r line 
	do
		cp $raw_dir/$line* $rawldsc_dir/
	done < "$filename"

done

