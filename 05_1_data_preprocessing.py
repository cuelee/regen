###################
## Created by Cue Hyunkyu Lee
## Date Nov 27 2017
##

import os, time
import sys
import numpy as np
import scipy.stats

print(" Cue Hyunkyu Lee: {}".format(sys.argv[0].split("/")[-1]));
cur_time = time.strftime("%a, %d %b %Y %H:%M:%S",time.localtime());

work_dir=sys.argv[1]
files=sys.argv[2].split(",")

for filename in files:
	cur_input = work_dir+"/"+filename+".intCorrected"
	cur_trait = filename
	cur_output = work_dir+"/"+filename+".intSimple"
	extract_var = "SNP A1 A2 N Z P".split()
	new_colnames = "SNP A1 A2 N Z P"
	print("Current trait name : {}".format(cur_trait))
	print("The Input file : {}".format(cur_input))
	print("The output file : {}".format(cur_output))	

	with open(cur_input,"r") as fin:
		col_names = fin.readline().split()

		## step 1 remove some unnecesary columns
		col_ind=[col_names.index(extract_var[ind]) for ind in range(len(extract_var))]
		print(col_ind) ##
		fout=open(cur_output,"w")
		print(new_colnames,file=fout)
		for aline in fin:
			line_list = [aline.split()[j] for j in col_ind]
			print(" ".join(map(str, line_list)),file=fout)
		fout.close()
		
