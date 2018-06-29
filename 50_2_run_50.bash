#!/bin/bash

reg_pathin="/media/cuelee/cue_workspace/Project/RE3_CHL/01work_ldsc/analysis/01_ldsc_cors/RE3_input/autoimmune.zsa"
re2_pathin="/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/14_metasoft_test/autoimmune.mti"
re2_out="/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/14_metasoft_test/autoimmune.mto"
code_dir="/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/codes"

bash 50_0_RE2_val.bash $reg_pathin $re2_pathin $re2_out $code_dir

