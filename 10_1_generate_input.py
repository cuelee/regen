#####################
## Created by Cue Hyunkyu Lee
## Date Dec 1 2017
##

## import modules
import os, time
import sys


print(" Cue Hyunkyu Lee: {}".format(sys.argv[0].split("/")[-1]));
cur_time = time.strftime("%a, %d %b %Y %H:%M:%S",time.localtime());
print(" Job started at: {}".format(cur_time));

## set parameters
work_dir = sys.argv[1]
outfile = sys.argv[2]
tgsnp_file = sys.argv[3]
snpinfo_file = sys.argv[4]
traits = sys.argv[5:]

## read Hapmap 3 data index
tgsnp_data=[]
tgsnp_list=[]
tgsnp_fin = open(tgsnp_file,"r")
frn = False
for line in tgsnp_fin:
	if (frn==False):
		frn=True
		cur_colnames=line.split()
		tgsnpi = cur_colnames.index("SNP")
		print("The file {} has SNP index of: {}".format("1000G",tgsnpi))
		continue
	split_line=line.split()
	tgsnp_data.append(split_line)
	tgsnp_list.append(split_line[tgsnpi])	

tgsnp_fin.close()

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

tgd_list=[]
snp_tgd_list=[]
## create index_dictionary to find overlapping snps between hapmap3 snps and data
for i in range(len(traits)):
	cur_snps=[]
	cur_data=[]
	ind_dict = dict((k,i) for i,k in enumerate(snp_array[i]))
	inter = set(snp_array[i]).intersection(tgsnp_list)
	indices = [ ind_dict[snp] for snp in inter ] 
	cur_data = [ data_array[i][ind] for ind in indices]
	cur_snps = [ snp_array[i][ind] for ind in indices]
	tgd_list.append(cur_data)
	snp_tgd_list.append(cur_snps)

for i in range(len(traits)):
	print("The length of the {}th array: {}".format(i+1,len(tgd_list[i])))
	print("The length of the {}th snp list: {}".format(i+1,len(snp_tgd_list[i])))


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
	cur_ind_dict = dict((k,i) for i,k in enumerate(snp_tgd_list[i]))
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
	for i in range(len(tgsnp_list)):
		if (tgsnp_list[i]==tgsnp_data[i][tgsnpi]):
			cur_snp = tgsnp_list[i]
			numNA = 0	
			## check index
			cur_A1 = 0
			cue_A2 = 0
			for j in range(len(traits)):
				if cur_snp in snp_dict[j]:
					cur_index = snp_dict[j][cur_snp]
					cur_A1 = tgd_list[j][cur_index][A1_inds[j]]
					cur_A2 = tgd_list[j][cur_index][A2_inds[j]]
				else:
					continue

			for j in range(len(traits)):
				if cur_snp in snp_dict[j]:
					cur_index = snp_dict[j][cur_snp]
					if (cur_A1 == tgd_list[j][cur_index][A1_inds[j]] and cur_A2 == tgd_list[j][cur_index][A2_inds[j]]):
						
						cur_z = tgd_list[j][cur_index][z_inds[j]]
					elif (cur_A1 == tgd_list[j][cur_index][A2_inds[j]] and cur_A2 == tgd_list[j][cur_index][A1_inds[j]]):
						print("CHECK the variant:{}".format(cur_snp));
						cur_z = str(-float(tgd_list[j][cur_index][z_inds[j]]))
					else:
						print("ERROR!!")
						print(tgd_list[j][cur_index])
						print(tgsnp_data[i])
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
			print("1000G indice ERROR")	


## close snp_info file
outinfo.close()

cur_time = time.strftime("%a, %d %b %Y %H:%M:%S",time.localtime());
print(" Job finished at: {}".format(cur_time));
