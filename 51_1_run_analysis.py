######################
## Created by Cue Hynkyu Lee
## June 4 2018

## import modules
import os
import sys
import math


## define definitions 
def CELIAC_2010(cvar):
	cur_file="/media/cuelee/cue_workspace/Pasaniuc_sumstats/Nov2017_Huwenbo/sum_stats_immune/CELIAC_2010.txt";
	frn = False;
	with open(cur_file,"r") as fin:
		for line in fin:
			if (frn == False):
				frn=True;
				col = line.split();
				or_ind = col.index("OR");
				p_ind = col.index("P");
				a1_ind = col.index("A1");
				a2_ind = col.index("A2");
				snp_ind = col.index("SNP");
				chr_ind = col.index("CHR");
				bp_ind = col.index("BP");
				z_ind = col.index("Z");
				continue
			splitted=line.strip().split();	
			cur_var = splitted[snp_ind];
			if (cvar == cur_var):
				cur_a1 = splitted[a1_ind];
				cur_a2 = splitted[a2_ind];
				cur_chr = splitted[chr_ind];
				cur_bp = splitted[bp_ind];

				cur_or = float(splitted[or_ind]);
				cur_lor = math.log(cur_or);
				cur_z = float(splitted[z_ind]);
				cur_se = cur_lor/cur_z;
				cur_uci = cur_lor + 1.96*cur_se
				cur_lci = cur_lor - 1.96*cur_se
				cur_v = cur_se**2
				return(cur_var,cur_chr,cur_bp,cur_a1,cur_a2,cur_lor,cur_v);
		print("NA induced {}:{}".format(cvar,cur_file))
		return(["NA"]*7)

def MS_2011(cvar):
	cur_file="/media/cuelee/cue_workspace/Pasaniuc_sumstats/Nov2017_Huwenbo/sum_stats_immune/MS_2011.txt";
	frn = False;
	with open(cur_file,"r") as fin:
		for line in fin:
			if (frn == False):
				frn=True;
				col = line.split();
				or_ind = col.index("OR");
				p_ind = col.index("P");
				a1_ind = col.index("A1");
				a2_ind = col.index("A2");
				snp_ind = col.index("SNP");
				chr_ind = col.index("CHR");
				bp_ind = col.index("BP");
				z_ind = col.index("Z");
				continue
			splitted=line.strip().split();	
			cur_var = splitted[snp_ind];
			if (cvar == cur_var):
				cur_a1 = splitted[a1_ind];
				cur_a2 = splitted[a2_ind];
				cur_chr = splitted[chr_ind];
				cur_bp = splitted[bp_ind];

				cur_or = float(splitted[or_ind]);
				cur_lor = math.log(cur_or);
				cur_z = float(splitted[z_ind]);
				cur_se = cur_lor/cur_z;
				cur_uci = cur_lor + 1.96*cur_se
				cur_lci = cur_lor - 1.96*cur_se
				cur_v = cur_se**2
				return(cur_var,cur_chr,cur_bp,cur_a1,cur_a2,cur_lor,cur_v);
		print("NAN induced {}:{}".format(cvar,cur_file))
		return(["NA"]*7)

def PBC_2015(cvar):
	cur_file="/media/cuelee/cue_workspace/Pasaniuc_sumstats/Nov2017_Huwenbo/sum_stats_immune/PBC_2015.txt";
	frn = False;
	with open(cur_file,"r") as fin:
		for line in fin:
			if (frn == False):
				frn=True;
				col = line.strip().split();
				or_ind = col.index("OR");
				p_ind = col.index("P");
				a1_ind = col.index("A1");
				a2_ind = col.index("A2");
				snp_ind = col.index("SNP");
				chr_ind = col.index("CHR");
				bp_ind = col.index("BP");
				z_ind = col.index("Z");
				continue
			splitted=line.strip().split();	
			cur_var = splitted[snp_ind];
			if (cvar == cur_var):
				cur_a1 = splitted[a1_ind];
				cur_a2 = splitted[a2_ind];
				cur_chr = splitted[chr_ind];
				cur_bp = splitted[bp_ind];
				
				cur_or = float(splitted[or_ind]);
				cur_lor = math.log(cur_or);
				cur_z = float(splitted[z_ind]);
				cur_se = cur_lor/cur_z;
				cur_uci = cur_lor + 1.96*cur_se
				cur_lci = cur_lor - 1.96*cur_se
				cur_v = cur_se**2
				return(cur_var,cur_chr,cur_bp,cur_a1,cur_a2,cur_lor,cur_v);
				cur_v = cur_se**2
				print(cur_var,cur_chr,cur_bp,cur_a1,cur_a2,cur_lor,cur_v);
		print("NAN induced {}:{}".format(cvar,cur_file))
		return(["NA"]*7)

def RA_EURO_2014(cvar):
	raw_file="/media/cuelee/cue_workspace/Pasaniuc_sumstats/description/0_Raw/RA_EURO_2014/RA_EURO_2014.txt";
	cur_file="/media/cuelee/cue_workspace/Pasaniuc_sumstats/Nov2017_Huwenbo/sum_stats_immune/RA_EURO_2014.txt";
	## step 1 find se_beta
	frn = False;
	with open(raw_file,"r") as fin:
		for line in fin:
			if(frn == False):
				frn = True;
				col = line.strip().split();
				snp_ind = col.index("SNPID")
				lci_ind = col.index("OR_95%CIlow")
				uci_ind = col.index("OR_95%CIup")	
			splitted=line.strip().split();
			cur_var = splitted[snp_ind];
			if(cvar == cur_var):
				cur_lci = float(splitted[lci_ind]);
				cur_uci = float(splitted[uci_ind]);
				cur_llci = math.log(cur_lci)
				cur_luci = math.log(cur_uci)
				cur_se=(cur_luci-cur_llci)/(2*1.96)
				del snp_ind
				del lci_ind
				del uci_ind
				del cur_lci
				del cur_uci
				del cur_llci
				del cur_luci
				break

	frn = False;
	with open(cur_file,"r") as fin:
		for line in fin:
			if (frn == False):
				frn=True;
				col = line.strip().split();
				p_ind = col.index("P");
				a1_ind = col.index("A1");
				a2_ind = col.index("A2");
				snp_ind = col.index("SNP");
				chr_ind = col.index("CHR");
				bp_ind = col.index("BP");
				z_ind = col.index("Z");
				continue
			splitted=line.strip().split();	
			cur_var = splitted[snp_ind];
			if (cvar == cur_var):
				cur_a1 = splitted[a1_ind];
				cur_a2 = splitted[a2_ind];
				cur_chr = splitted[chr_ind];
				cur_bp = splitted[bp_ind];
				
				cur_z = float(splitted[z_ind]);
				cur_lor = cur_z * cur_se
				cur_uci = cur_lor + 1.96*cur_se
				cur_lci = cur_lor - 1.96*cur_se
				cur_v = cur_se**2
				return(cur_var,cur_chr,cur_bp,cur_a1,cur_a2,cur_lor,cur_v);
		print("NAN induced {}:{}".format(cvar,cur_file))
		return(["NA"]*7)

def SLE_2015(cvar):
	cur_file="/media/cuelee/cue_workspace/Pasaniuc_sumstats/Nov2017_Huwenbo/sum_stats_immune/SLE_2015.txt";
	frn = False;
	with open(cur_file,"r") as fin:
		for line in fin:
			if (frn == False):
				frn=True;
				col = line.strip().split();
				or_ind = col.index("OR");
				p_ind = col.index("P");
				a1_ind = col.index("A1");
				a2_ind = col.index("A2");
				snp_ind = col.index("SNP");
				chr_ind = col.index("CHR");
				bp_ind = col.index("BP");
				z_ind = col.index("Z");
				continue
			splitted=line.strip().split();	
			cur_var = splitted[snp_ind];
			if (cvar == cur_var):
				cur_a1 = splitted[a1_ind];
				cur_a2 = splitted[a2_ind];
				cur_chr = splitted[chr_ind];
				cur_bp = splitted[bp_ind];

				cur_or = float(splitted[or_ind]);
				cur_lor = math.log(cur_or);
				cur_z = float(splitted[z_ind]);
				cur_se = cur_lor/cur_z;
				cur_uci = cur_lor + 1.96*cur_se
				cur_lci = cur_lor - 1.96*cur_se
				cur_v = cur_se**2
				return(cur_var,cur_chr,cur_bp,cur_a1,cur_a2,cur_lor,cur_v);
		print("NAN induced {}:{}".format(cvar,cur_file))
		return(["NA"]*7)



def CROHNS_2015(cvar):
	cur_file="/media/cuelee/cue_workspace/Pasaniuc_sumstats/Nov2017_Huwenbo/sum_stats_immune/CROHNS_2015.txt";
	frn = False;
	with open(cur_file,"r") as fin:
		for line in fin:
			if (frn == False):
				frn=True;
				col = line.strip().split();
				or_ind = col.index("OR");
				a1_ind = col.index("A1");
				a2_ind = col.index("A2");
				snp_ind = col.index("SNP");
				chr_ind = col.index("CHR");
				bp_ind = col.index("BP");
				se_ind = col.index("SE");
				continue
			splitted=line.strip().split();	
			cur_var = splitted[snp_ind];
			if (cvar == cur_var):
				cur_a1 = splitted[a1_ind];
				cur_a2 = splitted[a2_ind];
				cur_chr = splitted[chr_ind];
				cur_bp = splitted[bp_ind];

				cur_or = float(splitted[or_ind]);
				cur_lor = math.log(cur_or);
				cur_se = float(splitted[se_ind]);
				cur_uci = cur_lor + 1.96*cur_se
				cur_lci = cur_lor - 1.96*cur_se
				cur_v = cur_se**2
				return(cur_var,cur_chr,cur_bp,cur_a1,cur_a2,cur_lor,cur_v);
		print("NAN induced {}:{}".format(cvar,cur_file))
		return(["NA"]*7)

def UC_2015(cvar):
	cur_file="/media/cuelee/cue_workspace/Pasaniuc_sumstats/Nov2017_Huwenbo/sum_stats_immune/UC_2015.txt";
	frn = False;
	with open(cur_file,"r") as fin:
		for line in fin:
			if (frn == False):
				frn=True;
				col = line.strip().split();
				or_ind = col.index("OR");
				a1_ind = col.index("A1");
				a2_ind = col.index("A2");
				snp_ind = col.index("SNP");
				chr_ind = col.index("CHR");
				bp_ind = col.index("BP");
				se_ind = col.index("SE");
				continue
			splitted=line.strip().split();	
			cur_var = splitted[snp_ind];
			if (cvar == cur_var):
				cur_a1 = splitted[a1_ind];
				cur_a2 = splitted[a2_ind];
				cur_chr = splitted[chr_ind];
				cur_bp = splitted[bp_ind];

				cur_or = float(splitted[or_ind]);
				cur_lor = math.log(cur_or);
				cur_se = float(splitted[se_ind]);
				cur_uci = cur_lor + 1.96*cur_se
				cur_lci = cur_lor - 1.96*cur_se
				cur_v = cur_se**2
				return(cur_var,cur_chr,cur_bp,cur_a1,cur_a2,cur_lor,cur_v);
		print("NAN induced {}:{}".format(cvar,cur_file))
		return(["NA"]*7)

## get arguments
test_var=sys.argv[1]
test_chr=sys.argv[2]
test_bp=sys.argv[3]
meta_in=sys.argv[4]

result=[];
result.append(CELIAC_2010(test_var))
result.append(CROHNS_2015(test_var))
result.append(MS_2011(test_var))
result.append(PBC_2015(test_var))
result.append(RA_EURO_2014(test_var))
result.append(SLE_2015(test_var))
result.append(UC_2015(test_var))

with open(meta_in,"w") as fout:
	fplot_line = [];
	fplot_line.append(test_var);
	fplot_line.append(test_chr+":"+test_bp);
	a1_list=[];
	a2_list=[];
	#print(test_var,test_chr,test_bp)
	for line in result:
	#	print(line)
		if(	str(line[0])!="NA" 
			and str(test_var) == str(line[0])
			and int(test_chr) == int(line[1])
			#and int(test_bp) == int(line[2])
		):
			a1_list.append(str(line[3]));
			a2_list.append(str(line[4]));
			
			fplot_line.append(line[5]);
			fplot_line.append(line[6]);
		else:
			fplot_line.append(line[5]);
			fplot_line.append(line[6]);
	if(len(set(a1_list)) == 1 and len(set(a2_list)) ==1):
		print(" ".join(map(str,fplot_line)),file=fout);
	else:
		print(a1_list)
		print(a2_list)
		quit("FATAL ERROR")
	
