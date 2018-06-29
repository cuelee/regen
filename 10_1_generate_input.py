#####################
## Created by Cue Hyunkyu Lee
## Date Dec 1 2017
##

## import modules
import os
import sys


print("\n\nThe script name is: {} ".format(sys.argv[0]))
print("Number of arguments is: {} ".format(len(sys.argv)),"\n\n")

## set parameters
work_dir = sys.argv[1]
outfile = sys.argv[2]
h3snp_file = sys.argv[3]
snpinfo_file = sys.argv[4]
traits = sys.argv[5:]

print(work_dir)
print(outfile)
print(traits)

## read Hapmap 3 data index
h3snp_data=[]
h3snp_list=[]
h3snp_fin = open(h3snp_file,"r")
frn = False
for line in h3snp_fin:
	if (frn==False):
		frn=True
		cur_colnames=line.split()
		cur_h3snpind = cur_colnames.index("SNP")
		print("The file {} has SNP index of: {}".format("H3SNP",cur_h3snpind))
		continue
	split_line=line.split()
	h3snp_data.append(split_line)
	h3snp_list.append(split_line[cur_h3snpind])	

h3snp_fin.close()

## create the connections of the trait.intSimple files
myFiles = [open(work_dir+"/"+traits[i]+".intSimple","r") for i in range(len(traits))]

## define data (prob use a huge memory)
data_array=[]
snp_array=[]
colnames_array=[]
for i in range(len(traits)):
	cur_data=[]
	cur_snps=[]
	cur_colnames=[]
	frn = False
	for line in myFiles[i]:
		if (frn==False):
			frn=True
			cur_colnames=line.split()
			cur_snpind = cur_colnames.index("SNP")
			print("The {}th file has SNP index of: {}".format(i+1,cur_snpind))
			continue
		split_line = line.split()
		cur_data.append(split_line)	
		cur_snps.append(split_line[cur_snpind])	

	data_array.append(cur_data)
	snp_array.append(cur_snps)
	colnames_array.append(cur_colnames)
	

print("The number of data lists : {} ".format(len(data_array)))
print(len(colnames_array))
print(colnames_array)
	
for i in range(len(traits)):
	myFiles[i].close()
	print("The length of the {}th array: {}".format(i+1,len(data_array[i])))
	print("The length of the {}th snp list: {}".format(i+1,len(snp_array[i])))

del cur_data
del cur_snps
del cur_snpind
del myFiles

data_h3list=[]
snp_h3list=[]
## create index_dictionary to find overlapping snps between hapmap3 snps and data
for i in range(len(traits)):
	cur_snps=[]
	cur_data=[]
	ind_dict = dict((k,i) for i,k in enumerate(snp_array[i]))
	inter = set(snp_array[i]).intersection(h3snp_list)
	indices = [ ind_dict[snp] for snp in inter ] 
	cur_data = [ data_array[i][ind] for ind in indices]
	cur_snps = [ snp_array[i][ind] for ind in indices]
	data_h3list.append(cur_data)
	snp_h3list.append(cur_snps)

for i in range(len(traits)):
	print("The length of the {}th array: {}".format(i+1,len(data_h3list[i])))
	print("The length of the {}th snp list: {}".format(i+1,len(snp_h3list[i])))


del data_array
del cur_snps
del cur_data
del ind_dict
del inter
del indices

snp_dict=[]
z_inds = []
A1_inds = []
A2_inds = []
## create snp_dict
for i in range(len(traits)):
	cur_ind_dict = dict((k,i) for i,k in enumerate(snp_h3list[i]))
	snp_dict.append(cur_ind_dict)
	z_inds.append(colnames_array[i].index("Z"))
	A1_inds.append(colnames_array[i].index("A1"))
	A2_inds.append(colnames_array[i].index("A2"))
del cur_ind_dict 

## create snpinfo file
outinfo = open(snpinfo_file,"w")
print("SNP A1 A2",file=outinfo)

with open(outfile,"w") as outf:
	## main 
	cur_zs = ["NA"]*len(traits)
	for i in range(len(h3snp_list)):
		if (h3snp_list[i]==h3snp_data[i][cur_h3snpind]):
			cur_snp = h3snp_list[i]
			numNA = 0	
			## check index
			cur_A1 = 0
			cue_A2 = 0
			for j in range(len(traits)):
				if cur_snp in snp_dict[j]:
					cur_index = snp_dict[j][cur_snp]
					cur_A1 = data_h3list[j][cur_index][A1_inds[j]]
					cur_A2 = data_h3list[j][cur_index][A2_inds[j]]
				else:
					continue

			for j in range(len(traits)):
				if cur_snp in snp_dict[j]:
					cur_index = snp_dict[j][cur_snp]
					if (cur_A1 == data_h3list[j][cur_index][A1_inds[j]] and cur_A2 == data_h3list[j][cur_index][A2_inds[j]]):
						
						cur_z = data_h3list[j][cur_index][z_inds[j]]
					elif (cur_A1 == data_h3list[j][cur_index][A2_inds[j]] and cur_A2 == data_h3list[j][cur_index][A1_inds[j]]):
						print("CHECK the variant:{}".format(cur_snp));
						cur_z = str(-float(data_h3list[j][cur_index][z_inds[j]]))
					else:
						print("ERROR!!")
						print(data_h3list[j][cur_index])
						print(h3snp_data[i])
						quit()
						
					cur_zs[j] = cur_z
				else:	
					cur_zs[j] = "NA"
					numNA = numNA+1
					continue
			if (numNA < len(traits)):
				print(cur_snp+" "+" ".join(map(str,cur_zs)),file=outf)
				print(cur_snp+" "+cur_A1+" "+cur_A2,file=outinfo)
			else:
				continue
			continue	
		else:
			print("h3 indice ERROR")	


## close snp_info file
outinfo.close()
