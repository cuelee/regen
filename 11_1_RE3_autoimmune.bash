data_dir="/media/cuelee/cue_workspace/Cue_sumstats/CTG_CNCR/analysis"
reginput_dir="$data_dir/05_reGinput"
result_dir="/media/cuelee/cue_workspace/Cue_sumstats/CTG_CNCR/analysis"
output_dir="$result_dir/03_assoc_result"
REgcode_dir="/home/cuelee/Dropbox/Bogdan/RE3_code/code"
corr_dir="$result_dir/02_corrMats"
mkdir -p $output_dir
Rscript $REgcode_dir/RE3.R $reginput_dir/05_reGinput/neuroticism.zsa $output_dir/neuroticism.ress $corr_dir/neuroticism/neuroticism.GenCor $corr_dir/neuroticism/neuroticism.RECor

Rscript $REgcode_dir/LS.R $reginput_dir/05_reGinput/neuroticism.zsa $output_dir/neuroticism.lsss $corr_dir/neuroticism/neuroticism.GenCor $corr_dir/neuroticism/neuroticism.RECor
