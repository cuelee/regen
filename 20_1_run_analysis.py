###########################
## Created by Cue Hyunkyu Lee
## Date Jan 27 2018
## 

## import modules 
import sys
import os

## set definitions
def distance(x,y):
	fx=float(x);
	fy=float(y);
	if fx >= fy:
		result = fx - fy
	else:
		result = fy - fx
	return result

## get input arguments 
print("The current code is :{}".format(sys.argv[0]));
print("The number of argument is:{}".format(len(sys.argv)));

group = sys.argv[1];
pval_name = sys.argv[2];
result_dir = sys.argv[3];
gwfile = sys.argv[4];
tg_dir = sys.argv[5];
plink_path = sys.argv[6];
new_gwfile = sys.argv[7];
new_gwlog = new_gwfile+".log"


if(os.path.isfile(new_gwfile)):
	os.system("rm "+new_gwfile);

if(os.path.isfile(new_gwlog)):
	os.system("rm "+new_gwlog);

#catsnp_file = sys.argv[7];

temp_dir = os.path.join(tg_dir,pval_name);

## read data
## read gwfile
data_gw = [];
gw_snps = [];

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
		n = n + 1; 
		continue

print("the number of lines in gw_file is :{}".format(n));
gw_cols = cur_col;

fpout=open(new_gwfile,"a");
fpout.write(" ".join(map(str,gw_cols)));
fpout.close()

logout=open(new_gwlog,"a");
logout.write(" ".join(map(str,gw_cols)));
logout.close()

gw_chri = gw_cols.index("CHR");
gw_snpi = gw_cols.index("SNP");
gw_bpi = gw_cols.index("BP");
#csnp_chri = csnp_cols.index("CHR");
#csnp_snpi = csnp_cols.index("SNP");

## find snp_set for each chromosome
found = [0]*22;
#chr_list = []
for i in range(22):
	achr = i + 1;
	print(achr);
	snp_set = [];
	chr_snps = [];
	chr_gw_pvalue = [];
	chr_data_gw = []
	for nline in range(len(data_gw)):
		if (str(data_gw[nline][gw_chri])==str(achr)):
			chr_snps.append(str(data_gw[nline][gw_snpi]));
			chr_data_gw.append(data_gw[nline]);
			chr_gw_pvalue.append(float(data_gw[nline][p_ind]));
			continue
		continue

	found[i] = len(chr_snps);
#	chr_list.append(chr_snps)	

	temp_list = os.path.join(temp_dir,"Phase3_EUR_"+pval_name+"_chr"+str(achr)+".vars");
	with open(temp_list,"w") as flist:
		for asnp in chr_snps:
			print(asnp, file = flist);
			continue	

	gw_dict = dict((j,i) for (i,j) in enumerate(gw_snps));

	## open output
	fpout=open(new_gwfile,"a");
	logout=open(new_gwlog,"a");

	if(found[i] > 1 ):
		## 1. find set of snps in the same chromosome
		plink_inf = os.path.join(tg_dir,"Phase3_EUR_chr"+str(achr));
		plink_outf = os.path.join(temp_dir,"Phase3_EUR_"+pval_name+"_chr"+str(achr));
		plink_file = " --file " + plink_inf;
		plink_extract = " --extract " + temp_list;
		plink_r2 = " --r2 square";
		plink_out = " --make-bed --out " + plink_outf;
		os.system(plink_path + plink_file + plink_extract + plink_r2 + plink_out );
		plink_ldf = plink_outf + ".ld";	
		plink_ld_varf = plink_outf + ".bim";

		## 2. run data clumping
		truevec=[True]*len(chr_snps);
		p_list=list(chr_gw_pvalue);

		## Read the LD file 
		ld_vars = [];
		with open(plink_ld_varf,"r") as fvar:
			for aline in fvar:	
				splitted_line = aline.split();
				ld_vars.append(splitted_line[1]);


		ld_data = [];
		with open(plink_ldf,"r") as fld:
			for aline in fld:
				splitted_line = aline.split();
				ld_data.append(splitted_line);		

		## sanity check	
		for asnp in chr_snps:
			if asnp not in ld_vars:
				print("{} is not in LDfile".format(asnp));
				cur_ind = chr_snps.index(asnp)
				truevec[cur_ind]=False;
				p_list[cur_ind]=1;
				continue
	
		## Run analysis
		cur_p_list = list(p_list);
		while (sum(truevec) > 0):
			cur_min_p = min(cur_p_list)
			print(cur_min_p);
			cur_index = p_list.index(cur_min_p);
			cur_chr = int(chr_data_gw[cur_index][gw_chri]);
			cur_bp = int(chr_data_gw[cur_index][gw_bpi]);
			cur_var = chr_data_gw[cur_index][gw_snpi];
				
			if cur_var not in ld_vars:
				quit("FATAL ERROR: Check LD file");

			cur_ld_ind = ld_vars.index(cur_var);
			for nvar in range(len(ld_vars)):
				nvar_ind = chr_snps.index(ld_vars[nvar])
				nvar_bp = int(chr_data_gw[nvar_ind][gw_bpi]);
				cur_ld_ind=ld_vars.index(cur_var)
				nvar_ld = float(ld_data[cur_ld_ind][nvar]);	
				if(distance(nvar_bp,cur_bp) < 10000000 and nvar_ld > 0.1):
					
					print("Found LD:{}-{} :: {}".format(cur_var,ld_vars[nvar],nvar_ld),file=logout);	
					if(chr_data_gw[nvar_ind][gw_snpi] == ld_vars[nvar]):
						truevec[nvar_ind]=False;
						p_list[nvar_ind]=1
					else:
						quit("FATAL ERROR!: not matching");
				del nvar_ind;
				continue;
			
			print("This variants will be saved:{}".format(cur_var));
			fpout.write("\n")
			fpout.write(" ".join(map(str,chr_data_gw[cur_index])));
			truevec[cur_index]=False;
			p_list[cur_index]=1;
			cur_p_list = list([i for indx,i in enumerate(p_list) if truevec[indx] == True]);
	elif(found[i]==1):
		print("This variants will be saved:{}".format(chr_data_gw[0][gw_snpi]));
		fpout.write("\n")
		fpout.write(" ".join(map(str,chr_data_gw[0])));

			
	fpout.close()
