#/bin/bash

#inflation corrected files lcorr files 
group=$1
base_dir=$2
code_dir="/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/codes"

#define lcorr paths
LSlcorr=$base_dir$group.LSp.lcorr;
RE2lcorr=$base_dir$group.RE2p.lcorr;
RE3lcorr=$base_dir$group.RE3p.lcorr;
outfile_LR=$base_dir$group.LRp.lcorr;
#outfile_LRG=$base_dir$group.LRGp.lcorr;

## run main analysis
module load python/python3.6.5;
python3 $code_dir/16_1_run_analysis.py $LSlcorr $RE2lcorr $RE3lcorr $base_dir $outfile_LR #$outfile_LRG
