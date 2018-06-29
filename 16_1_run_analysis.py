################################
## Cue Hyunkyu Lee
## Date May 11 2018
##

## import modules 
import os
import sys

## print command argvs
print("The location of the script is: {}".format(sys.argv[0]));
print("The number of the arguments is: {}".format(len(sys.argv)));
print("{}".format(sys.argv));

## get parameters
LSf=sys.argv[1];
RE2f=sys.argv[2];
RE3f=sys.argv[3];
base_dir=sys.argv[4];
outfile_LR=sys.argv[5];
#outfile_LRG=sys.argv[6];

## sanity check #1 lines
lines_vec=[];
for data in (LSf,RE2f,RE3f):
	num_lines = sum(1 for line in open(data,"r"));
	lines_vec.append(num_lines);
	print("cur #line :{}".format(num_lines))
if(all([int(lines_vec[0])==element for element in lines_vec])):
	nline=lines_vec[0];
	del lines_vec
	del num_lines
else:
	quit("ERROR")
print("\n\nThe line numbers of the input files are the same: {}\n\n".format(nline));


fli=False;
with open(LSf,"r") as fls, open(RE2f,"r") as fre, open(RE3f,"r") as freg, open(outfile_LR,"w") as flr: #, open(outfile_LRG,"w") as flrg:
	for i in range(nline):
		if (fli==False):
			fli=True;
			titles=[fls.readline().split(),fre.readline().split(),freg.readline().split()]
			print(all(titles[0][:-1]==avec[:-1] for avec in titles));
			snp_ind=titles[0].index("SNP");
			col_names=titles[0][:-1];
			lr_col=list(col_names)
			#lrg_col=list(col_names)
			lr_col.append("LRp")
			#lrg_col.append("LRGp")
			print(" ".join(map(str,lr_col)),file=flr);
			#print(" ".join(map(str,lrg_col)),file=flrg);
			continue;
		lls=fls.readline().split();
		lre=fre.readline().split();
		lreg=freg.readline().split();
		if(all(lls[:-1] == avec for avec in [lre[:-1],lreg[:-1]])):
			lr_min=(min(float(lls[-1]),float(lreg[-1])));
			#lrg_min=(min(float(lls[-1]),float(lre[-1]),float(lreg[-1])));
			lr_line=lls[:-1];
			#lrg_line=lls[:-1];
			lr_line.append(str(lr_min));
			#lrg_line.append(str(lrg_min));
			print(" ".join(map(str,lr_line)),file=flr);
			#print(" ".join(map(str,lrg_line)),file=flrg);
			continue;
		else:
			quit("Found data inconsistency");



