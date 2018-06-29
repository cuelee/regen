#!/bin/bash
re3input_path="/media/cuelee/cue_workspace/Project/RE3_CHL/01work_ldsc/analysis/01_ldsc_cors/RE3_input"
result_path="/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/04_result"


bash 13_0_preprocess.bash ${re3input_path}/autoimmune.info ${result_path}/autoimmune.ress RE3p ${result_path}/autoimmune
bash 13_0_preprocess.bash ${re3input_path}/pgc_cross.info ${result_path}/pgc_cross.ress RE3p ${result_path}/pgc_cross
bash 13_0_preprocess.bash ${re3input_path}/autoimmune.info ${result_path}/autoimmune.ress RE2p ${result_path}/autoimmune
bash 13_0_preprocess.bash ${re3input_path}/pgc_cross.info ${result_path}/pgc_cross.ress RE2p ${result_path}/pgc_cross
bash 13_0_preprocess.bash ${re3input_path}/autoimmune.info ${result_path}/autoimmune.lsss LSp ${result_path}/autoimmune
bash 13_0_preprocess.bash ${re3input_path}/pgc_cross.info ${result_path}/pgc_cross.lsss LSp ${result_path}/pgc_cross
