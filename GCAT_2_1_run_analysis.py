######################
## Created by Cue Hyunkyu Lee
## Date Jan 17 2018
##

## import modules
import sys
import os

## Read input arguments 
print("The current code is: {}".format(sys.argv[0]));
print("The number of arguments is: {}".format(len(sys.argv)));
snp_file = sys.argv[1];
catalog_dir = os.path.dirname(snp_file);
out_file = os.path.join(catalog_dir,"catalogIn1000G.txt");
tg_file = sys.argv[2];



## Read GWAS catalog snp file
print("\nStart reading snp file")
catalog_snps = [];
n = 0;
with open(snp_file,"r") as fin:
	for line in fin:
		splitted = line.strip();
		catalog_snps.append(splitted);
		n = n + 1;
	print("The total number of lines: {}".format(n));
	print("\nComplete reading snp file");

## set indice
catalog_dict = dict((j,i) for (i,j) in enumerate(catalog_snps));
found_vec = [False] * len(catalog_snps);

## Read VEP 	
print("\nStart reading tg data");
n = 0;
with open(tg_file,"r") as fin, open(out_file,"w") as fout:
	for line in fin:
		splitted = line.strip().split("\t");
		cur_snp=splitted[1];
		if ( cur_snp in catalog_dict ):
			print(" ".join(map(str,splitted)),file=fout);
			found_vec[catalog_dict[cur_snp]] = True;
			n = n + 1;
	print("The total number of founds: {}".format(n));
	print("\nComplete reading TG_data");

n=0;
for i in range(len(found_vec)):
	if(found_vec[i] == False):
		n=n+1;
print("n = {}".format(n))

