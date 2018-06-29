######################
## Created by Cue Hynkyu Lee
## June 4 2018

## import modules
import os
import sys

## get arguments
reg_file=sys.argv[1];
re2_file=sys.argv[2];

n=0;
nre2=0;
with open(reg_file,"r") as fin, open(re2_file,"w") as fout:
	frn = False
	for line in fin:
		splitted=line.strip().split();
		cur_snp=splitted[0];
		cur_zs=splitted[1:];
		new_zs=[];
		nonna=0;
		for i in range(len(cur_zs)):
			if(cur_zs[i] != "NA"):
				nonna=nonna+1
				new_zs.append(cur_zs[i]);
				new_zs.append("1");
			elif(cur_zs[i] == "NA"):
				new_zs.append(cur_zs[i]);
				new_zs.append("NA");
		if(nonna>1):
			new_line=list([cur_snp]+new_zs);
			print(" ".join(map(str,new_line)),file=fout);
			nre2=nre2+1;
		n=n+1;

print("The number of lines in REg_input:{}".format(n));
print("The number of lines in RE2_input:{}".format(nre2));
