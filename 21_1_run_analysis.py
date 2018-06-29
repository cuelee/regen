###########################
## Created by Cue Hyunkyu Lee
## Date Jan 27 2018
## 

## import modules 
import sys
import os

## get input arguments 
print("The current code is :{}".format(sys.argv[0]));
print("The number of argument is:{}".format(len(sys.argv)));

group = sys.argv[1];
pval_name = sys.argv[2];
result_dir = sys.argv[3];
gwfile = sys.argv[4];
tg_dir = sys.argv[5];
plink_path = sys.argv[6];
catsnp_file = sys.argv[7];

output = os.path.join(result_dir,group+"_GWS_"+pval_name);
output_file = output + ".cat";
temp_dir = os.path.join(tg_dir,pval_name);
temp_list = os.path.join(temp_dir,"temp_file.txt");

run_find =  True;

## read data
## read gwfile
data_gw = [];
gw_snps = [];
gw_pvalue = [];
frn = False;
n=0;
with open(gwfile,"r") as fin:
	for line in fin:
		if (frn == False):
			frn = True;
			cur_col = line.split();
			snp_ind = cur_col.index("SNP");
			p_ind = cur_col.index(pval_name);
			continue
		splitted = line.split();
		data_gw.append(splitted);
		gw_snps.append(splitted[snp_ind]);
		gw_pvalue.append(splitted[p_ind]);
		n = n + 1; 
		continue

print("The number of lines in GW_file is :{}".format(n));
gw_cols = cur_col;

## read snp_list.txt 
data_csnp = [];
cat_snps = [];
n=0;
frn = False;
with open(catsnp_file,"r") as fin:
	for line in fin:
		if (frn == False):
			frn = True;
			cur_col = line.split();
			snp_ind = cur_col.index("SNP");	
			continue
		splitted=line.split(); 
		data_csnp.append(splitted);
		cat_snps.append(splitted[snp_ind]);
		n = n + 1;
		continue

print("The number of lines in csnp_file is :{}".format(n));
csnp_cols = cur_col;

## find intersection
existed = list(set(gw_snps).intersection(cat_snps))
exist_dict = dict((j,i) for (i,j) in enumerate(existed))
print(" The number of snps overlap between GW and csnp is:{}".format(len(existed)));

#quit()

gw_chri = gw_cols.index("CHR");
gw_snpi = gw_cols.index("SNP");
csnp_chri = csnp_cols.index("CHR");
csnp_snpi = csnp_cols.index("SNP");

## find snp_set for each chromosome
found = [0]*22;
chr_list = []
for i in range(22):
	achr = i + 1;
	snp_set = [];
	gwsnp_list = [];
	for nline in range(len(data_gw)):
		if (str(data_gw[nline][gw_chri])==str(achr)):
			snp_set.append(str(data_gw[nline][gw_snpi]));
			gwsnp_list.append(str(data_gw[nline][gw_snpi]));
			continue
		continue
	for nline in range(len(data_csnp)):
		if (str(data_csnp[nline][csnp_chri])==str(achr)):
			snp_set.append(str(data_csnp[nline][csnp_snpi]));
			continue
		continue
	snp_list = list(set(snp_set))
	found[i] = len(gwsnp_list);
	chr_list.append(gwsnp_list)	
	with open(temp_list,"w") as flist:
		for asnp in snp_list:
			print(asnp, file = flist);
			continue	

	if(found[i] > 0 and run_find == True):
		## 1. find set of snps in the same chromosome
		plink_inf = os.path.join(tg_dir,"Phase3_EUR_chr"+str(achr));
		plink_outf = os.path.join(temp_dir,"Phase3_EUR_"+pval_name+"_chr"+str(achr));
		plink_file = " --file " + plink_inf;
		plink_extract = " --extract " + temp_list;
		plink_r2 = " --r2 square";
		plink_out = " --make-bed --out " + plink_outf;
		os.system(plink_path + plink_file + plink_extract + plink_r2 + plink_out);

## create dicts
gw_dict = dict((j,i) for (i,j) in enumerate(gw_snps));
cat_dict = dict((j,i) for (i,j) in enumerate(cat_snps));


## find ld > 0.5 between all snps in gw_snps and cat_snps
with open(output_file, "w") as fout:
	print("gwSNP-catSNPs",file = fout);
	iter = 1;
		
	## for loop
	for i in range(22):
		if(len(chr_list[i]) > 0):
			## Set current LD file and map file
			min_plink = os.path.join( temp_dir, "Phase3_EUR_" + pval_name + "_chr" + str(i+1));
			min_ldfile = min_plink + ".ld";
			min_mapfile = min_plink + ".bim";
			
			## Read data
			ld_data = [];
			with open(min_ldfile, "r") as fin:
				for line in fin:
					splitted = line.split();
					ld_data.append(splitted);
					continue

			ld_vars = [];
			with open(min_mapfile, "r") as fin:
				for line in fin:
					splitted = line.split();
					ld_vars.append(splitted[1]);
					continue	
			
			ldvar_dict = dict((j,i) for (i,j) in enumerate(ld_vars));
			
		for asnp in chr_list[i]:
			cur_index = gw_dict[asnp];
			cur_chr = data_gw[cur_index][gw_chri];
			cur_snp = data_gw[cur_index][gw_snpi];

			## check if the snp is existed in the plink format	
			if (cur_snp in ld_vars):
				ld_list = [];
				print("Current snp: {} ({}/{})".format(cur_snp,iter, len(gw_snps)));

				## check if the GWAS catalog found the snp
				if (cur_snp in gw_snps and cur_snp in cat_snps):
					print("exact:{}".format(cur_snp),file = fout);	
				else:
					cur_ldrow = ldvar_dict[cur_snp];
					for avar_ind in range(len(ld_vars)):
						if (ld_vars[avar_ind] in cat_snps and str(ld_data[cur_ldrow][avar_ind]) != "nan" and float(ld_data[cur_ldrow][avar_ind]) >= 0.5):
							ld_list.append(ld_vars[avar_ind]);
					if (len(ld_list) > 0):
						print("LD:{}-{}".format(cur_snp,",".join(map(str,ld_list))) , file = fout);
					else: 
						print("Novel:{}".format(cur_snp),file = fout);
			else:
				print("NotIn1000G:{}".format(cur_snp));	

			iter = iter + 1;
		

