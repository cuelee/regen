###################
## Created by Cue Hyunkyu Lee
## Dated by 2018 May 23
##


## set definitions
def distance(x,y):
        fx=float(x);
        fy=float(y);
        if fx >= fy: 
                result = fx - fy
        else:
                result = fy - fx
        return result


## import modules 
import os
import sys

print("The current script is:{}".format(sys.argv[0]));
print("The number of arguments is:{}".format(len(sys.argv)));
print("{}".format(sys.argv[1:]));
achr=int(sys.argv[1])
abp=int(sys.argv[2])
cat_file=sys.argv[3]
outfile=sys.argv[4]+str(achr)+"_"+str(abp)+".txt"
distthre=int(sys.argv[5])

## Read GWAS catalog 
print("\nStart reading catalog data")
catalog_data = [];
snps = [];
merges = [];
curids = []; 
frn = False; 
n = 0;
with open(cat_file,"r") as fin, open(outfile,"w") as fout:
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
			cat_mtind = catalog_col.index("MAPPED_TRAIT");
			cat_umtind = catalog_col.index("MAPPED_TRAIT_URI");
			colen = len(catalog_col);
			continue	
		splitted = line.strip().split("\t");
		cur_snp = splitted[cat_snpind];
		cur_merged = splitted[cat_merind];
		cur_newsnp = splitted[cat_curind];
		if (cur_merged == 1):
			cur_snp = cur_newsnp;

		if( splitted[cat_chrind] in [str(i+1) for i in range(22)]):
			cur_chr = int(splitted[cat_chrind]);
			cur_pos = int(splitted[cat_posind]);
		else:
			cur_chr = splitted[cat_chrind];
			cur_pos = splitted[cat_posind];
		cur_rgene = splitted[cat_geneind];
		cur_mgene = splitted[cat_mapped_gene];
		cur_p = splitted[cat_pind];
		cur_mt = splitted[cat_mtind];
		cur_umt = splitted[cat_umtind];
		dist = 0;

		if(achr == cur_chr):
			dist = distance(abp, cur_pos);
			if(dist < distthre):
				n=n+1
				print("SNP:{}, POS:{}:{}, RGENE:{}, MGENE:{}, P:{}, MAPPED_TRAIT:{}".format(cur_snp, cur_chr, cur_pos, cur_rgene, cur_mgene, cur_p, cur_mt),file = fout);
		catalog_data.append(splitted);


	print("The total number of lines: {}".format(n))
	print("\nComplete reading catalog_data");

