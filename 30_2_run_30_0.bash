#!/bin/bash
input=$1
vep_argv=$2

bash 30_0_summarizing_vep_results.bash $1 ~/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/09_VEP/ ~/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/04_result/ ~/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/codes /home/cuelee/ensembl-vep/vep $2
#bash 73_0_summarizing_vep_results.bash RE3p,LRp,LSp adsf ~/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/04_result/ ~/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/codes
#bash 73_0_summarizing_vep_results.bash RE3p,RE2p,LSp adsf ~/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/04_result/ ~/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/codes
