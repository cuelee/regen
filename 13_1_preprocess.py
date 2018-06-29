######################3
## Created by Cue Hyunkyu Lee
## Date Dec 2 2017
##

## import modules 
import os
import sys

## get input arguments
print("\n\nThe script name is: {} ".format(sys.argv[0]))
#print("Number of arguments is: {} ".format(len(sys.argv)),"\n\n")

## set parameters
h3snp_dir=sys.argv[1]
input_name = sys.argv[2]
output_name = sys.argv[3]
pvalue = sys.argv[4]
outfile_name = sys.argv[5]

h3snp_file=h3snp_dir+"/CEU.info"
input_file=input_name
result_file=output_name
outfile = outfile_name+"."+pvalue
#gwsfile = outfile_name +"_GWS."+pvalue

## read Hapmap 3 snp_info
h3snp_data=[]
h3snp_list=[]

h3snp_fin = open(h3snp_file,"r")
frn=False
for line in h3snp_fin:
	if (frn==False):
		frn=True
		cur_colnames=line.split()
		cur_h3snpind = cur_colnames.index("SNP")
		cur_h3bpind = cur_colnames.index("BP")
		cur_h3chrind = cur_colnames.index("CHR")
		print("The file {} has SNP index of: {}".format("H3SNP",cur_h3snpind))
		continue
	split_line=line.split()
	h3snp_data.append(split_line)
	h3snp_list.append(split_line[cur_h3snpind])

h3snp_fin.close()

## create the connections of the set.info file
finfo = open(input_file,"r")

## define data (prob use a huge memory)
info_data=[]
info_snps=[]
info_colnames=[]

frn = False
for line in finfo:
	if (frn==False):
		frn=True
		info_colnames=line.split()
		cur_snpind = info_colnames.index("SNP")
		info_A1ind = info_colnames.index("A1")
		info_A2ind = info_colnames.index("A2")
		print("The file has SNP index of: {}".format(cur_snpind))
	split_line = line.split()
	info_data.append(split_line)
	info_snps.append(split_line[cur_snpind])


## create the connections of the set.ress file
fress = open(result_file,"r")

## define data (prob use a huge memory
ress_data=[]
ress_snps=[]
ress_colnames=[]

frn = False
for line in fress:
	if (frn==False):
		frn=True
		ress_colnames=line.split()
		cur_snpind = ress_colnames.index("SNP")
		ress_pind = ress_colnames.index(pvalue)
		print("The file SNP index of: {}".format(cur_snpind))
	split_line = line.split()
	ress_data.append(split_line)
	ress_snps.append(split_line[cur_snpind])

del cur_snpind


if(ress_snps != info_snps):
	quit("the order of ress and info SNPs does not match")
else:
	print("The inputs pass the sanity checks")

finfo.close()
fress.close()

## create index_dictionary to find overlapping snps between hapmap3 snps and data
info_dict = dict((k,i) for i,k in enumerate(info_snps))
ress_dict = dict((k,i) for i,k in enumerate(ress_snps))

#outgws = open(gwsfile,"w")
print("\n\nGenerating outfile at {}".format(outfile))
#print("SNP CHR BP A1 A2 "+pvalue,file=outgws)
with open(outfile,"w") as outf:
	## main
	printin = ["0"]*6 # SNP, CHR, BP, A1, A2, RE3p
	print("SNP CHR BP A1 A2 "+pvalue,file=outf)
	
	for i in range(len(h3snp_list)):
		if (h3snp_list[i] == h3snp_data[i][cur_h3snpind]):
			cur_snp = h3snp_data[i][cur_h3snpind]
			cur_BP = h3snp_data[i][cur_h3bpind]
			cur_CHR = h3snp_data[i][cur_h3chrind].split("chr")[1]
			if (cur_snp in info_dict and int(cur_CHR) < 23):
				cur_index = info_dict[cur_snp]
				if (info_snps[cur_index]!=ress_snps[cur_index]):
					quit("FATAL ERROR: SNP does not matching")
				printin[0] = cur_snp
				printin[1] = cur_CHR
				printin[2] = cur_BP
				printin[3] = info_data[cur_index][info_A1ind]
				printin[4] = info_data[cur_index][info_A2ind]
				printin[5] = ress_data[cur_index][ress_pind]
				
				print(" ".join(map(str,printin)),file=outf)

#				if (float(printin[5]) <= 5*10**-8):
#					print(" ".join(map(str,printin)),file=outgws)
			else:
				continue
		else: 
			print("Found Problem")
#outgws.close()
