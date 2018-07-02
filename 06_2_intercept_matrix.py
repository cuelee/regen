########################
## Created by Cue Hyunkyu Lee
## Date Nov 28 2017
##

## import 
import os, time
import numpy as np

output_file = sys.argv[1]
n_argv = int(sys.argv[2])
main_argv = list(map(float,sys.argv[3:]))
cors=[x-1 for x in main_argv]

print("output will be generated at: {}".format(output_file))

## define parameters
print("n_argv: {}".format(n_argv))
 
corMat = np.zeros((n_argv,n_argv))
np.fill_diagonal(corMat,1)

ind = 0
for i in range(n_argv - 1):
	for j in range( i+1 , n_argv,1):
		corMat[i,j] = cors[ind]
		corMat[j,i] = cors[ind] 
		ind = ind + 1

print(corMat)

np.savetxt(fname=output_file,X=corMat,fmt='%1.5f',delimiter=' ',newline='\n',header='',footer='',comments='#')

