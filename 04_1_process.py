print("### /created by Cue Hyunkyu Lee ")
print("### Nov 21 2017 ")

## import 
import os
import sys
import numpy as np
import math

print("The name of the script is: ", sys.argv[0])
print("Number of arguments: ",len(sys.argv))
#print("The arguments are: ", str(sys.argv[1:]))
main_argv = sys.argv[2:]
output_file= sys.argv[1]
print("output will be generated at: ",output_file)

## define parameters
n_argv = len(main_argv)
print("n_argv:", n_argv)

corMat=np.zeros((n_argv,n_argv))
np.fill_diagonal(corMat,1)

k= len(main_argv)-1
j=0
for cur_file in main_argv[:-1]:
	cur_colVec=[0]*k
	with open(cur_file,"r") as f:

		for aline in f: 
			if "Summary of Genetic Correlation Results" in aline:
				colnames=f.readline().split()
				for iter in range(k):
					cur_data=f.readline().split()
					cur_colVec[iter]=cur_data[2]
				corMat[j,j+1:n_argv]=cur_colVec
				corMat[j+1:n_argv,j]=cur_colVec
	
	k=k-1
	j=j+1

f.close()


print(corMat)

np.savetxt(fname=output_file,X=corMat,fmt='%1.5f',delimiter=' ',newline='\n',header='',footer='',comments='#')



