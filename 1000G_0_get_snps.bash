#!/bin/bash
temp="file.temp"
base="/media/cuelee/storagedev_cue/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/04_result"
curname="autoimmune_GWS.LSp"
cut -f 1 -d " " ${base}/${curname}.hg38 > ${base}/${temp}
tail -n +2 ${base}/${temp} > ${base}/${curname}.vin
curname="autoimmune_GWS.RE2p"
cut -f 1 -d " " ${base}/${curname}.hg38 > ${base}/${temp}
tail -n +2 ${base}/${temp} > ${base}/${curname}.vin
curname="autoimmune_GWS.RE3p"
cut -f 1 -d " " ${base}/${curname}.hg38 > ${base}/${temp}
tail -n +2 ${base}/${temp} > ${base}/${curname}.vin
curname="pgc_cross_GWS.LSp"
cut -f 1 -d " " ${base}/${curname}.hg38 > ${base}/${temp}
tail -n +2 ${base}/${temp} > ${base}/${curname}.vin
curname="pgc_cross_GWS.RE2p"
cut -f 1 -d " " ${base}/${curname}.hg38 > ${base}/${temp}
tail -n +2 ${base}/${temp} > ${base}/${curname}.vin
curname="pgc_cross_GWS.RE3p"
cut -f 1 -d " " ${base}/${curname}.hg38 > ${base}/${temp}
tail -n +2 ${base}/${temp} > ${base}/${curname}.vin
curname="pgc_cross_naomi_GWS.LSp"
cut -f 1 -d " " ${base}/${curname}.hg38 > ${base}/${temp}
tail -n +2 ${base}/${temp} > ${base}/${curname}.vin
curname="pgc_cross_naomi_GWS.RE2p"
cut -f 1 -d " " ${base}/${curname}.hg38 > ${base}/${temp}
tail -n +2 ${base}/${temp} > ${base}/${curname}.vin
curname="pgc_cross_naomi_GWS.RE3p"
cut -f 1 -d " " ${base}/${curname}.hg38 > ${base}/${temp}
tail -n +2 ${base}/${temp} > ${base}/${curname}.vin
