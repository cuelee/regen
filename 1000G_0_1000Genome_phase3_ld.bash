#!/bin/bash

##################
## Created by Cue Hyunkyu Lee
## Date Jan 02 2018
##

x=1
#for i in $(seq 0 1 $x)
#do
#	echo "The code will be paused by system for $x day(s) to complete downloading 1000 genome VCF formats"
#	sleep ${x}d
#done

for i in $(seq 1 1 22)
do 
#	perl /media/cuelee/storagedev_cue/1000G/ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/browser/vcf_to_ped_converter/version_1.1/vcf_to_ped_convert.pl -vcf /media/cuelee/storagedev_cue/1000G/ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/ALL.chr${i}.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz -sample_panel_file /media/cuelee/storagedev_cue/1000G/phase1_integrated_calls.20101123.ALL.panel -region ${i}:1-250000000 -population GBR -population FIN -population CEU -population TSI -population IBS -output_ped /media/cuelee/storagedev_cue/1000G/work/raw_ped/ALL.chr${i}.phase3.ped -output_info /media/cuelee/storagedev_cue/1000G/work/raw_ped/ALL.chr${i}.phase3.info -base_format letter
	vcftools --gzvcf /media/cuelee/storagedev_cue/1000G/ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/ALL.chr${i}.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz --snps /media/cuelee/storagedev_cue/1000G/allsnps_Bogdan_1000G.txt --min-alleles 2 --max-alleles 2 --keep /media/cuelee/storagedev_cue/1000G/sid.EUR.txt --out /media/cuelee/storagedev_cue/1000G/work/raw_ped/Phase3_EUR_chr${i} --plink
done

