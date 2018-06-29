## this code is designed to be run using python3.6.2

import os
import sys
import numpy as np
import math
import scipy.stats
print("\nInitiation....\n\n")

print("The name of the script is: ", sys.argv[0])
print("Number of arguments: ",len(sys.argv))
print("The arguments are: ", str(sys.argv[1:]))


trait_name=sys.argv[1]
intercept=float(sys.argv[2])
file_name=trait_name+".txt"
in_file_name=file_name
out_file_name=trait_name+".intCorrected"

input_dir="/media/cuelee/cue_workspace/Project/RE3_CHL/01work_ldsc/analysis/01_ldsc_cors/data" 
output_dir="/media/cuelee/cue_workspace/Project/RE3_CHL/01work_ldsc/analysis/01_ldsc_cors/cue-work"
cur_file = os.path.join(input_dir,in_file_name)
out_file = os.path.join(output_dir,out_file_name)

if (intercept>2 or intercept<0):
	sys.exit("The value of intercept is below 0 or greater than 2")
 
if (intercept>1):
	## read a sumstat_data
	with open(cur_file,"r") as f:
		
		col_names=f.readline().split()
		Z_index=col_names.index("Z")
		P_index=col_names.index("P")
		k=open(out_file,"w")
		print(' '.join(col_names),file=k) 

		for aline in f:
			line_list=aline.split()
			float_Z=float(line_list[Z_index])
			updated_Z=float_Z/math.sqrt(intercept)
			line_list[Z_index]=str(updated_Z)
			line_list[P_index]=str(scipy.stats.distributions.chi2.sf(float(line_list[Z_index])**2,df=1,loc=0,scale=1))
			if (float(line_list[P_index]) > 1 or float(line_list[P_index])<=0):
				print(line_list)
				#sys.exit("FATAL_ERROR")
			print(" ".join(map(str, line_list)),file=k)
		k.close()

	f.close()
else:
	os.system("cp " + cur_file + " " + out_file)    
 
quit()
		


