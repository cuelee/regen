###################3
## Created by Cue Hyunkyu Lee
## Date Jan 17 2017
##

## import modules 
import sys
import os

## read input arguments 
print("The current code is:{}".format(sys.argv[0]));
print("The number of arguments are: {}".format(len(sys.argv)));
file_name = sys.argv[1]
output_dir = sys.argv[2]
cur_file = os.path.join(output_dir,file_name);
out_file = os.path.join(output_dir,"bedfolder",file_name+".bed");

## read current file
cur_data = [];
frn = False;
with open(cur_file,"r") as fin, open(out_file,"w") as fout:
	for aline in fin:
		if (frn == False):
			frn = True;
			splitted = aline.split();
			data_col = splitted;
			snpind = data_col.index("SNP");
			chrind = data_col.index("CHR");
			bpind = data_col.index("BP");
			continue
		splitted = aline.split();
		out=["chr"+splitted[chrind],splitted[bpind],str(int(splitted[bpind])+1),splitted[snpind]];
		print(" ".join(map(str,out)),file = fout);

