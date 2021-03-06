#!/bin/bash
	
result_dir="/media/cuelee/cue_workspace/Cue_sumstats/CTG_CNCR/result"
outname="neuroticism"
group="$result_dir/01_input/$outname"

bash /home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/codes/01_create_folders.bash $group 
bash /home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/codes/02_0_intercept_extractor.sh $group 
bash /home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/codes/03_0_run_LDSC_cor.bash $group
bash /home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/codes/04_0_create_corMat.bash $group $outname
bash /home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/codes/05_0_meta_analysis.bash $group
bash /home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/codes/06_0_intercept_extractor.bash $group $outname 
