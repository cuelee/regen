#!/bin/bash
group=$1
cores=$2

data_dir="/media/cuelee/cue_workspace/Cue_sumstats/CTG_CNCR/analysis"
result_dir="/media/cuelee/cue_workspace/Cue_sumstats/CTG_CNCR/result"
REgcode_dir="/home/cuelee/Dropbox/Bogdan/RE3_code/code"

reginput_dir="$data_dir/05_reGinput"
RECor_dir="$result_dir/02_corrMats/$group.RECor"
GenCor_dir="$result_dir/02_corrMats/$group.GenCor"
temp_dir="$reginput_dir/temp"

rm -r $temp_dir

output_dir="$result_dir/03_assoc_result"
mkdir -p $output_dir
mkdir -p $temp_dir


nl_vec=($(wc -l $reginput_dir/$group.zsa))

module load python/python3.6.5
python3.6 11_1_inputsep.py $reginput_dir $group $cores $nl_vec $REgcode_dir $RECor_dir $GenCor_dir

#cat $temp_dir/inputs.txt | parallel --colsep ' ' python {1} {2} {3} {4}





####ETCS

#Rscript $REgcode_dir/LS.R $reginput_dir/$group.zsa $output_dir/$group.lsss $corr_dir/neuroticism/neuroticism.GenCor $corr_dir/neuroticism/neuroticism.RECor

#Rscript $REgcode_dir/RE3.R $reginput_dir/neuroticism.zsa $output_dir/neuroticism.ress $corr_dir/neuroticism/neuroticism.GenCor $corr_dir/neuroticism/neuroticism.RECor


#cat argv.txt | parallel --colsep ' ' python {1} {2}
#parallel --jobs 2 -m --header : Rscript {f1} {f2} {f3} ::: f1 count.R ::: f2 100000000 200000000 ::: f3 A B


