#!/bin/bash
base_dir=$1
#"/media/cuelee/storagedev_cue/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/04_result/"
sort -t " " -k2 -g ${base_dir}/autoimmune.ress > ${base_dir}/autoimmune.sorted
sort -t " " -k2 -g ${base_dir}/pgc_cross.ress > ${base_dir}/pgc_cross.sorted
#sort -t " " -k2 -g ${base_dir}/pgc_cross_naomi.ress > ${base_dir}/pgc_cross_naomi.sorted


sort -t " " -k2 -g ${base_dir}/autoimmune.lsss > ${base_dir}/autoimmune.lsss.sorted
sort -t " " -k2 -g ${base_dir}/pgc_cross.lsss > ${base_dir}/pgc_cross.lsss.sorted
#sort -t " " -k2 -g ${base_dir}/pgc_cross_naomi.lsss > ${base_dir}/pgc_cross_naomi.lsss.sorted
