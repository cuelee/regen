########################3
## Created by Cue Hyunkyu Lee
## Dated May 24 2018
##

## import modules
import os
import sys
import scipy.stats

## define definitions
def getp(azscore):
	if(azscore == "NA"):
		return "NA";
	ap = str(scipy.stats.distributions.chi2.sf(float(azscore)**2, df=1, loc=0, scale=1));
	return(ap);

def distance(x,y):
        fx=float(x);
        fy=float(y);
        if fx >= fy: 
                result = fx - fy
        else:
                result = fy - fx
        return result

## get arguments 
print("\n\n\n\n The current script is :{}".format(sys.argv[0]));
print(" The number of the arguments is:{}".format(len(sys.argv)));
#print(" The arguments are:\n{}".format("\n".join(sys.argv[1:])));
var_name=sys.argv[1];
var_chr=int(sys.argv[2]);
var_bp=int(sys.argv[3]);
var_range=int(sys.argv[4]);
base_dir=sys.argv[5];
omv_dir=sys.argv[6];
code_dir=sys.argv[7];
RE3in_path=sys.argv[8];
RE3des_path=sys.argv[9];
autoimmune_list=sys.argv[10];
RE2des_path=sys.argv[11];
LSdes_path=sys.argv[12];
cur_i=str(sys.argv[13]);


## set outputs
base_out=var_name
forest_out = os.path.join(base_dir,cur_i+"_"+base_out+".frp"); ## frp means FoRest Plot
linkedp_out = os.path.join(omv_dir,cur_i+"_"+base_out+".lpo"); ## lpo means Linked P Out

frn=False;
## Search BP and CHR
with open(RE3des_path,"r") as fin:
	for line in fin:
		if (frn == False):
			col_des=line.split();
			des_snpind=col_des.index("SNP");
			des_chrind=col_des.index("CHR");
			des_bpind=col_des.index("BP");
			des_pind=col_des.index("RE3p");
			frn=True;
			continue
		splitted=line.split();
		cur_bp=int(splitted[des_bpind]);
		cur_chr=int(splitted[des_chrind]);
		if(cur_chr!=var_chr):
			continue
		cur_snp=splitted[des_snpind];
		if(var_name==cur_snp):
			print("CUR_SNP: {}, CUR_BP: {} VEP_BP:{}".format(cur_snp,str(cur_bp),str(var_bp)));
			if(cur_chr==var_chr):
				hg38_bp=cur_bp;
				print(hg38_bp);
			else:
				quit("FATAL error");

## read_RE3input Z score
print("\n Start reading RE3_description file....");
frn = False;
des_data=[];
des_snps=[];
nlist=0;
with open(RE3des_path,"r") as fin:
	for line in fin:
		if (frn == False):
			col_des=line.split();
			des_snpind=col_des.index("SNP");
			des_chrind=col_des.index("CHR");
			des_bpind=col_des.index("BP");
			des_pind=col_des.index("RE3p");
			frn=True;
			continue
		splitted=line.split();
		cur_bp=int(splitted[des_bpind]);
		cur_chr=int(splitted[des_chrind]);
		if(cur_chr!=var_chr):
			continue
		dist=float(distance(cur_bp,hg38_bp));
		if (dist < var_range):
			des_data.append(splitted);
			des_snps.append(splitted[des_snpind]);
			nlist=nlist+1;
			#break  ##  I added this temporarily

print("\n Read RE3_description file. {} variants are dist < {}".format(nlist,var_range));	
print(" Done..");

## read_RE2input 
print("\n Start reading REw_description file....");
frn = False;
RE2_data=[];
RE2_snps=[];
with open(RE2des_path,"r") as fin:
        for line in fin:
                if (frn == False):
                        col_des=line.split();
                        RE2_snpind=col_des.index("SNP");
                        RE2_chrind=col_des.index("CHR");
                        RE2_bpind=col_des.index("BP");
                        RE2_pind=col_des.index("RE2p");
                        frn=True;
                        continue
                splitted=line.split();
                cur_bp=int(splitted[RE2_bpind]);
                cur_chr=int(splitted[RE2_chrind]);
                if(cur_chr!=var_chr):
                        continue
                dist=float(distance(cur_bp,hg38_bp));
                if (dist < var_range):
                        RE2_data.append(splitted);
                        RE2_snps.append(splitted[RE2_snpind]);
                        #break  ##  I added this temporarily

print(" Done..");

## read_RE2input 
print("\n Start reading LS_description file....");
frn = False;
LS_data=[];
LS_snps=[];
with open(LSdes_path,"r") as fin:
        for line in fin:
                if (frn == False):
                        col_des=line.split();
                        LS_snpind=col_des.index("SNP");
                        LS_chrind=col_des.index("CHR");
                        LS_bpind=col_des.index("BP");
                        LS_pind=col_des.index("LSp");
                        frn=True;
                        continue
                splitted=line.split();
                cur_bp=int(splitted[LS_bpind]);
                cur_chr=int(splitted[LS_chrind]);
                if(cur_chr!=var_chr):
                        continue
                dist=float(distance(cur_bp,hg38_bp));
                if (dist < var_range):
                        LS_data.append(splitted);
                        LS_snps.append(splitted[LS_snpind]);
                        #break  ##  I added this temporarily

print(" Done..");


## Read desease list file
disease_list=[];
with open(autoimmune_list,"r") as fin:
	for line in fin:
		disease_list.append(line.split()[0]);

print(disease_list)	
print("\n\n Read disease list file...Done"); 

fn = 0;
varin = [];
plist=[];
## Read and compare RE3in file
print("Start reading REgeneral input file...."); 
with open(RE3in_path,"r") as fin, open(linkedp_out,"w") as flpo:
	for line in fin:
		splitted=line.split();
		cur_snp=splitted[0];
		if(cur_snp in des_snps):
			des_ind=des_snps.index(cur_snp)
			RE2_ind=RE2_snps.index(cur_snp)
			LS_ind=LS_snps.index(cur_snp)
			cur_bp=des_data[des_ind][des_bpind]
			cur_chr=des_data[des_ind][des_chrind]
			cur_RE3p=des_data[des_ind][des_pind]
			cur_RE2p=RE2_data[RE2_ind][RE2_pind]
			cur_LSp=LS_data[LS_ind][LS_pind]
			
			fn = fn+1;
			apvec=[getp(azscore) for azscore in splitted[1:]];
			print(" ".join(map(str,[cur_snp]+[cur_chr]+[cur_bp]+apvec+[cur_RE3p]+[cur_RE2p]+[cur_LSp])),file=flpo);
			plist.append(apvec);
			if(cur_snp == var_name):
				varin=splitted;	
		if(fn==nlist):
			print("Stop reading REgeneral input file: Found all variants");
			break
	
print("\n Finish reading RE3_input file. {}/{} variants found".format(fn,nlist));
with open(forest_out,"w") as fout:
	print(" ".join(map(str,varin)),file=fout);
