## this code is designed to be run using python3.6.2

import os, time
import sys
import numpy as np
import math
import scipy.stats

cur_time=time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime());
print("\n Cue Hyunkyu Lee : {}".format(sys.argv[0].split("/")[-1]));
print(" Job started at : {}".format(cur_time));

## get input arguments 
trait_name=sys.argv[1]
data_dir=sys.argv[2]
intercept=float(sys.argv[3])

## set paths
file_name=trait_name+".txt"
in_file_name=file_name
out_file_name=trait_name+".intCorrected"
input_dir=data_dir+"/01_raw_ldsc" 
output_dir=data_dir+"/02_intcorr"
cur_file = os.path.join(input_dir,in_file_name)
out_file = os.path.join(output_dir,out_file_name)

## check sanity of intercept value
if (intercept>2 or intercept<0):
	sys.exit("The value of intercept is below 0 or greater than 2")

## int correct is necessary only when the value is greater than 1 
if (intercept>1):
	## read a sumstat_data
	with open(cur_file,"r") as fin:
		
		col_names=fin.readline().split()
		Z_index=col_names.index("Z")
		P_index=col_names.index("P")
		fout=open(out_file,"w")
		print(' '.join(col_names),file=fout) 

		for aline in fin:
			line_list=aline.split()
			float_Z=float(line_list[Z_index])
			updated_Z=float_Z/math.sqrt(intercept)
			line_list[Z_index]=str(updated_Z)
			line_list[P_index]=str(scipy.stats.distributions.chi2.sf(float(line_list[Z_index])**2,df=1,loc=0,scale=1))
			if (float(line_list[P_index]) > 1 or float(line_list[P_index])<=0):
				print(line_list)
			print(" ".join(map(str, line_list)),file=fout)
		fout.close()
else:
	os.system("cp " + cur_file + " " + out_file)    

cur_time = time.strftime("%a, %d %b %Y %H:%M:%S",time.localtime()); 
print("\n Job finished at : {}".format(cur_time));
