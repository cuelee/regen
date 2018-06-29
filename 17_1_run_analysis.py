###################3
## Created by Cue Hyunkyu Lee
## Date Feb 01 2018
##

## import modules
import sys

group = sys.argv[1]
pval = sys.argv[2]
base_dir = sys.argv[3]
inputfile = sys.argv[4]
outfile = sys.argv[5]
gthres = float(sys.argv[6]);
ntest = float(sys.argv[7]);
mtc_gthres = float(gthres/ntest);

print("the genome-wide threshold pvalue for the test is:{}".format(mtc_gthres))
## read data
frn = False; 
with open(inputfile,"r") as fin, open(outfile,"w") as fout:
	for line in fin:
		if (frn == False):
			frn = True;
			print(line.strip(),file=fout);
			cur_col=line.split();
			pind = cur_col.index(pval);
			continue
		splitted = line.split()
		if (float(splitted[pind]) < mtc_gthres):
			print(" ".join(map(str,splitted)),file=fout);
		continue
