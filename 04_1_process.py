print("### /created by Cue Hyunkyu Lee ")
print("### Nov 21 2017 ")

## import 
import os, time
import sys
import numpy as np
import math

cur_time = time.strftime("%a, %d %b %y %H:%M:%S", time.localtime());

print(" Cue Hyunyku Lee: {}".format(sys.argv[0].split("/")[-1]));
print(" Job started at: {}".format(cur_time)); 

output_file= sys.argv[1]
main_argv = sys.argv[2:]
print("output: {}".format(output_file));

## define parameters
n_argv = len(main_argv);
print("n_argv:", n_argv);

corMat=np.zeros((n_argv,n_argv));
np.fill_diagonal(corMat,1);

k= len(main_argv)-1;
j=0;
for cur_file in main_argv[:-1]:
	cur_colVec=[0]*k;
	with open(cur_file,"r") as fin:

		for aline in fin: 
			if "Summary of Genetic Correlation Results" in aline:
				colnames=fin.readline().split();
				for iter in range(k):
					cur_data=fin.readline().split();
					cur_colVec[iter]=cur_data[2];
				corMat[j,j+1:n_argv]=cur_colVec;
				corMat[j+1:n_argv,j]=cur_colVec;
	
	k=k-1;
	j=j+1;

print(corMat);

np.savetxt(fname=output_file,X=corMat,fmt='%1.5f',delimiter=' ',newline='\n',header='',footer='',comments='#')


