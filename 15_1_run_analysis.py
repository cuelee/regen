###########################
## Cue Hyunkyu Lee
## Date Feb 1 2018
##

## import modules 
import os
import sys
import scipy.stats

## get parameters
inputf=sys.argv[1]
outputf=sys.argv[2]
corr=float(sys.argv[3])
pval=sys.argv[4]

## read input
frn = False;
data = [];
with open(inputf,"r") as fin, open(outputf,"w") as fout:
	for line in fin:
		if (frn == False):
			frn = True;
			print(line.strip(),file = fout);
			cur_col = line.split();
			p_ind = cur_col.index(pval);
			continue
		splitted = line.split();
		cur_p = float(splitted[p_ind])
		cur_chisq = scipy.stats.chi2.isf(cur_p,1) 
		new_chisq = min(cur_chisq * corr,1420)
		splitted[p_ind] = str(scipy.stats.distributions.chi2.sf(new_chisq,df=1,loc=0,scale=1))
		print(" ".join(map(str,splitted)),file = fout);


		
