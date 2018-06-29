#################
## Created by Cue Hyunkyu Lee
## Date Jan 29 2018
##

## import modules 
import sys
import os

## get input arguments
group = sys.argv[1]
pval = sys.argv[2]
base_dir = sys.argv[3]
ocat_file = sys.argv[4]
gws_file = sys.argv[5]
out_exact = sys.argv[6]
out_ld = sys.argv[7]
out_novel = sys.argv[8]

print("\n\nCurrent group: {} pval: {}".format(group,pval));

def file_len(fname):
	with open(fname) as f:
		for i, l in enumerate(f):
			pass
	return i 

## read ocat
vec_class = [];
data_items = [];
frn = False;
with open(ocat_file,"r") as fin:
	for line in fin:
		if (frn == False):
			frn = True;
			cur_col = line.split();
			continue
		splitted=line.strip().split(":");
		vec_class.append(splitted[0]);
		data_items.append(splitted[1].split("-")[0]);
		continue

vec_classname = ["exact","LD","Novel"]
n_vec = [0]*3;
dict_class = dict((j,i) for (i,j) in enumerate(vec_classname));
print("\n The length of vec_class : {}".format(len(vec_class)));
print(" The length of data_items : {}".format(len(data_items)));

exact_vec = [];
ld_vec = [];
novel_vec = [];
for nl in range(len(vec_class)):
	ind = dict_class[vec_class[nl]]
	if(ind == 0):
		exact_vec.append(data_items[nl]);
	if(ind == 1):
		ld_vec.append(data_items[nl]);
	if(ind == 2):
		novel_vec.append(data_items[nl]);
	n_vec[ind] = n_vec[ind] + 1;

print(vec_classname)
	
print((n_vec))
print(sum(n_vec))

print("\n Complete reading ocat file\n")

## read hg38 file
gws_snps = [];
gws_data = [];
frn = False;
with open(gws_file,"r") as fin:
	for line in fin:
		if (frn == False):
			frn = True;
			gws_col = line.strip(); 
			cur_col = line.split();
			snp_ind = cur_col.index("SNP")
			continue
		splitted = line.split();
		gws_snps.append(splitted[snp_ind]);
		gws_data.append(splitted);
		continue

dict_gws = dict((j,i) for (i,j) in enumerate(gws_snps));

## all snps in novel_vec should exist in dict_gws
with open(out_exact, "w") as fout:
	cur_snp_vec = exact_vec
#	cate = "exact"
	print(gws_col,file = fout);
	for i in range(len(cur_snp_vec)):
		if cur_snp_vec[i] in gws_snps:
			ind = dict_gws[cur_snp_vec[i]]
			print(" ".join(map(str,gws_data[ind])),file = fout);
		else:
			quit("FATAL ERROR")
#space = " "
#os.system("bash /home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/codes/23_0_find_GWAShits.bash "+group+space+pval+space+cate+space+base_dir)
## all snps in novel_vec should exist in dict_gws
with open(out_ld, "w") as fout:
	cur_snp_vec = ld_vec
#	cate = "ld"
	print(gws_col,file = fout);
	for i in range(len(cur_snp_vec)):
		if cur_snp_vec[i] in gws_snps:
			ind = dict_gws[cur_snp_vec[i]]
			print(" ".join(map(str,gws_data[ind])),file = fout);
		else:
			quit("FATAL ERROR")

#space = " "
#os.system("bash /home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/codes/23_0_find_GWAShits.bash "+group+space+pval+space+cate+space+base_dir)
## all snps in novel_vec should exist in dict_gws
with open(out_novel, "w") as fout:
	cur_snp_vec = novel_vec
#	cate = "novel"
	print(gws_col,file = fout);
	for i in range(len(cur_snp_vec)):
		if cur_snp_vec[i] in gws_snps:
			ind = dict_gws[cur_snp_vec[i]]
			print(" ".join(map(str,gws_data[ind])),file = fout);
		else:
			quit("FATAL ERROR")

#space = " "
#os.system("bash /home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/codes/23_0_find_GWAShits.bash "+group+space+pval+space+cate+space+base_dir)


print("\nNexact:{}, Nld:{}, Nnovel:{}".format(file_len(out_exact),file_len(out_ld),file_len(out_novel)))
print("\nDone.\n")	
