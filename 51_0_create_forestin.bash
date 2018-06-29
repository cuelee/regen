metasoft_dir="/media/cuelee/cue_workspace/software/MetaSoft"
forestpm_dir="/media/cuelee/cue_workspace/software/ForestPMPlot"
code_dir="/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/codes"
for_dir="/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/15_forest_plot"

study_name="/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/02_inputs/autoimmune.rst"
module load python/python3.6.5

i=1
## start main analysis
cvar="rs13405741" 
cchr="2"
cbp="110871950"
input=${for_dir}/${i}_${cvar}.txt
output=${for_dir}/${cvar}.pdf
i=$(expr $i + 1)
python3 $code_dir/51_1_run_analysis.py $cvar $cchr $cbp $input
#cvar="rs2546199"
#cchr="5"
#cbp="95972143"
#input=${for_dir}/${i}_${cvar}.txt
#output=${for_dir}/${cvar}.pdf
#i=$(expr $i + 1)
#python3 $code_dir/51_1_run_analysis.py $cvar $cchr $cbp $input
#cvar="rs7810237"
#cchr="7"
#cbp="13865026"
#input=${for_dir}/${i}_${cvar}.txt
#output=${for_dir}/${cvar}.pdf
#i=$(expr $i + 1)
#python3 $code_dir/51_1_run_analysis.py $cvar $cchr $cbp $input
#cvar="rs11832772"
#cchr="12"
#cbp="40752053"
#input=${for_dir}/${i}_${cvar}.txt
#output=${for_dir}/${cvar}.pdf
#i=$(expr $i + 1)
#python3 $code_dir/51_1_run_analysis.py $cvar $cchr $cbp $input
cvar="rs2114844"
cchr="12"
cbp="44285645"
input=${for_dir}/${i}_${cvar}.txt
output=${for_dir}/${cvar}.pdf
i=$(expr $i + 1)
python3 $code_dir/51_1_run_analysis.py $cvar $cchr $cbp $input
cvar="rs35776863"
cchr="17"
cbp="7264362"
input=${for_dir}/${i}_${cvar}.txt
output=${for_dir}/${cvar}.pdf
i=$(expr $i + 1)
python3 $code_dir/51_1_run_analysis.py $cvar $cchr $cbp $input
