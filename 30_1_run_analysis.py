##########################3
## Created by Cue Hyunkyu lee
## Date 2018 05 18
## 


## import modules 
import sys
import os

## define definitions 
def run_analysis(inputfs,atype,agroup,outputdir,basedir,vep_on):
	## generate all inputfs
	data = [];
	ubar = "_";
	gws = "GWS";
	dot = ".";
	snp_ind = 0;
	chr_ind = 1;
	bp_ind = 2;
	for ainput in inputfs:
		cur_name = agroup + ubar + gws + ubar + ainput + dot + atype;
		cur_file = os.path.join(basedir,cur_name);
		cur_data,snp_ind,chr_ind,bp_ind = read_file(cur_file);
		data.append(cur_data);

	unique_vec=[];
	unique_data=[];
	for i in range(len(data)):
		for j in range(len(data[i])):
			if data[i][j][snp_ind] not in unique_vec:
				unique_vec.append(data[i][j][snp_ind]);
				unique_data.append(data[i][j]);
	del unique_vec;
	unique_data = sorted(unique_data,key = lambda x: (int(x[1]),int(x[2])));
	unique_snps = [unique_data[i][snp_ind] for i in range(len(unique_data))];
	print(len(unique_snps));
	## write vep input	
	vep_out = outputdir + agroup + ubar + gws + ubar + atype;
	vep_index = vep_out + ".index";
	vep_in = vep_out + ".vin";
	write_output(vep_in,unique_snps,1);

	vep_run = veppath + " --format id --no_headers --force_overwrite --cache --assembly GRCh38 --pick --symbol --dont_skip -i "+ vep_in + " -o " + vep_out;
	if vep_on == True:
		os.system(vep_run);
	else:
		print("# of unique_snps in {}: {}".format(cur_name,len(unique_snps)));
		return(0)
	
	## variant indexing
	ind_vars = var_indexing(data, unique_snps, inputfs, snp_ind);

	## write identification
	iden_out = outputdir + agroup + ubar + gws + ubar + atype + ".iden";
	ind_out = [[unique_snps[i],ind_vars[i]] for i in range(len(ind_vars))]
	write_output(iden_out,ind_out,2); 

	## add ind_var to vep_out
	adding_indvars(ind_out,unique_snps,vep_out,vep_index);

def adding_indvars(ind_out,unique_snps,vep_out,vep_index):
	iv_dict = dict((j,i) for (i,j) in enumerate(unique_snps))
		
	## read vep_out and write vep_index
	fvep = open (vep_out, "r");
	fvm = open(vep_index, "w");
	for line in fvep:
		cur_line=line.split();
		cur_line.append(ind_out[iv_dict[cur_line[0]]][1]);
		fvm.write(" ".join(map(str,cur_line))+"\n");

def var_indexing(data, target, inputfs, snp_ind):
	index_vec = [[]]*len(target);
	out_vec = [];
	target_dict = dict((j,i) for (i,j) in enumerate(target));
	for i in range(len(data)):
		cur_in=[data[i][k][snp_ind] for k in range(len(data[i]))];
		for j in range(len(cur_in)):
			find=target_dict[cur_in[j]];
			index_vec[find] = index_vec[find]+[inputfs[i]];
	for i in range(len(index_vec)):
		out_vec.append(",".join(index_vec[i]))
	return(out_vec);

def write_output(fname,odat,dim):
	fout = open(fname,"w");
	for i in range(len(odat)):
		if dim == 1:
			fout.write(odat[i]+"\n");
		if dim > 1:
			fout.write(" ".join(map(str,odat[i]))+"\n");	

def read_file(file_path):
	cur_data = [];
	fin = open(file_path,"r")
	frn = False;
	for line in fin:
		if frn == False:
			frn = True;
			col = line.split();
			snp_ind = col.index("SNP");
			chr_ind = col.index("CHR");
			bp_ind = col.index("BP");
			continue
		cur_data.append(line.split());
	return(cur_data,snp_ind,chr_ind,bp_ind)

## get input arguments 
print("The current code name is :{}".format(sys.argv[0]));
print("The number of arguments is :{}".format(len(sys.argv)));

vep_on = False;
inputfs=sys.argv[1].split(",");
outputdir=sys.argv[2];
basedir=sys.argv[3];
veppath=sys.argv[4];
vep_argv=sys.argv[5];
if(vep_argv=="True"):
	vep_on = True;
## main code

print("Vep:{}".format(vep_on));
	
types=["novel","exact","ld"];
groups=["autoimmune","pgc_cross"];
for atype in types:
	for agroup in groups:
		run_analysis(inputfs,atype,agroup,outputdir,basedir,vep_on);

