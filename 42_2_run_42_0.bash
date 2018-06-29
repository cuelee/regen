code_dir="/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/codes"
base_dir="/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/13_novel_analysis"
omv_dir="$base_dir/novel_1M_variants"
RE3in_path="/media/cuelee/cue_workspace/Project/RE3_CHL/01work_ldsc/analysis/01_ldsc_cors/RE3_input/autoimmune.zsa"
RE3des_path="/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/04_result/autoimmune.RE3p.lcorr.hg38"
RE2des_path="/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/04_result/autoimmune.RE2p.lcorr.hg38"
LSdes_path="/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/04_result/autoimmune.LSp.lcorr.hg38"
range=1500000
var_name=$1
var_chr=$2
var_bp=$3
cur_i=$4
autoimmune_list="/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/02_inputs/autoimmune.rst"


bash 42_0_find_1M_vars.bash $var_name $var_chr $var_bp $base_dir $omv_dir $code_dir $RE3in_path $range $RE3des_path $autoimmune_list $RE2des_path $LSdes_path $cur_i
