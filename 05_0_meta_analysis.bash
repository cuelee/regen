#!/bin/bash

## set parameters
input_dir="$1.rst"
data_dir="/media/cuelee/cue_workspace/Cue_sumstats/CTG_CNCR/analysis"
work_dir="$data_dir/02_intcorr"
meta_dir="$data_dir/04_FE_inputs"
ldsc_dir="/media/cuelee/cue_workspace/software/ldsc"
code_dir="/media/cuelee/cue_workspace/Cue_sumstats/CTG_CNCR/codes"

mkdir -p $meta_dir

cur_list=""
while read -r trait
do
	cur_list="${cur_list}${trait}"
	cur_list="${cur_list},"
done < $input_dir
cur_list=${cur_list%,}
echo $cur_list

module load python/python3.6.5

python3 $code_dir/05_1_data_preprocessing.py $work_dir ${cur_list}
python3 $code_dir/05_2_FE_framework.py $ldsc_dir $work_dir $meta_dir ${cur_list} 
module unload python/python3.6.5

exit

source /home/cuelee/anaconda2/bin/activate ldsc
i=0
while read -r trait
do
	traits[i]=$trait 
	i=$(expr $i + 1)
done < "$input_dir"
max=$i

i=0
j=0
i_span=($(seq 0 1 $(expr $max - 2)))

echo ${i_span[@]}
echo ${j_span[@]}

for i in ${i_span[@]}
do
	j_span=($(seq $(expr $i + 1) 1 $(expr $max - 1) ))
	i_trait=${traits[$i]}
	for j in ${j_span[@]}
	do
		j_trait=${traits[$j]}
		#echo $meta_dir/${i_trait}_${j_trait}.sumstats
		$ldsc_dir/munge_sumstats.py --merge-allele $ldsc_dir/ldfile/eur_w_ld_chr/w_hm3.snplist --sumstats $meta_dir/${i_trait}_${j_trait}.sumstats --out $meta_dir/${i_trait}_${j_trait}
		$ldsc_dir/ldsc.py --h2 $meta_dir/${i_trait}_${j_trait}.sumstats.gz --ref-ld-chr $ldsc_dir/ldfile/eur_w_ld_chr/ --w-ld-chr $ldsc_dir/ldfile/eur_w_ld_chr/ --out $meta_dir/${i_trait}_${j_trait}_ldsc
	done
done

