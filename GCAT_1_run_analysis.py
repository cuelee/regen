######################
## Created by Cue Hyunkyu Lee
## Date Jan 17 2018
##

## import modules
import sys
import re
import os

## Read input arguments 
print("The current code is: {}".format(sys.argv[0]));
print("The number of arguments is: {}".format(len(sys.argv)));
code_dir = sys.argv[1];
catalog_file = sys.argv[2];
catalog_snp_file = os.path.join(os.path.dirname(catalog_file),"snp_list_test.txt")
## datas : catalog, vep, 
## Why Vep ? : Since it has closed gene info

## Read GWAS catalog 
print("\nStart reading catalog data")
catalog_data = [];
snps = [];
merges = [];
curids = [];
frn = False;
n = 0;
with open(catalog_file,"r") as fin:
	for line in fin:
		if(frn == False):
			frn = True;
			splitted = line.strip().split("\t");
			catalog_col = splitted;

			cat_snpind = catalog_col.index("SNPS");
			cat_merind = catalog_col.index("MERGED");
			cat_curind = catalog_col.index("SNP_ID_CURRENT");
			cat_chrind = catalog_col.index("CHR_ID");
			cat_posind = catalog_col.index("CHR_POS");
			cat_geneind = catalog_col.index("REPORTED GENE(S)");
			cat_mapped_gene = catalog_col.index("MAPPED_GENE");
			cat_pind = catalog_col.index("P-VALUE");
			print(catalog_col)
			continue
		splitted = line.strip().split("\t");
		catalog_data.append(splitted);
		n = n + 1 
	print("The total number of lines: {}".format(n))
	print("\nComplete reading catalog_data");

## set indice

data_snps = [];
out_data = []

for i in range(len(catalog_data)):
	cur_snps = re.split('; | x ', catalog_data[i][cat_snpind]);
	cur_merged = catalog_data[i][cat_merind];
	if (cur_merged == 1):
		cur_snps = catalog_data[i][cat_merind];
	
	for cur_snp in cur_snps:
		if (cur_snp[0]=="r" and cur_snp[1] == "s"):
			data_snps.append(cur_snp);
			continue
		continue	

snp_set=list(set(data_snps))
with open(catalog_snp_file,"w") as fout:
	for cur_snp in snp_set:
		print(cur_snp, file = fout);
		continue
