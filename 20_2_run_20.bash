#######################
## Created by Cue Hyunkyu Lee
## Date Jan 28 2018
##

pval=$1 
bash 20_0_generate_1000G_LD_pruned_plinkformat.bash autoimmune $pval /home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/04_result
bash 20_0_generate_1000G_LD_pruned_plinkformat.bash pgc_cross $pval /home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/04_result
#bash 20_0_generate_1000G_LD_pruned_plinkformat.bash pgc_cross_naomi $pval /home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/04_result
