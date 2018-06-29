####################
## Created by Cue Hyunkyu Lee
## Date Jan 17 2018
##

## import modules 
import sys

## get sys.argv
print("The current code is: {}".format(sys.argv[0]));
print("The number of arguments are: {}".format(len(sys.argv)));
file_name=sys.argv[1]
out_dir=sys.argv[2]
cur_lifted=out_dir+"/"+file_name+".bed.txt"
out_file=out_dir+"/"+file_name+".hg38"
cur_file=out_dir+"/"+file_name

## read datas
old_data= [];
old_snp_list = [];
frn = False;
with open(cur_file,"r") as fin:
	for aline in fin:
		if (frn == False):
			frn=True;
			new_col = aline.strip();
			old_col = aline.split();
			snpind = old_col.index("SNP");
			chrind = old_col.index("CHR");
			continue
		splitted = aline.split();
		old_data.append(splitted[3:]);
		old_snp_list.append(splitted[snpind]);
		continue
old_snp_dict = dict((k,i) for i,k in enumerate(old_snp_list))

snps = [];
bps = [];
chrs = [];
with open(cur_lifted,"r") as fin:
	for aline in fin:
		splitted = aline.split();
		snps.append(splitted[3]);
		bps.append(splitted[1]);
		chrs.append(splitted[0]);
#		chrs.append(splitted[0].split("chr")[1].split("_KI")[0]);
		continue

with open(out_file,"w") as fout:
	print(new_col,file = fout);
	for i in range(len(snps)):
		cur_ind = old_snp_dict[snps[i]];
		newline = [snps[i],chrs[i],bps[i],old_data[cur_ind][0],old_data[cur_ind][1],old_data[cur_ind][2]];
		print(" ".join(map(str,newline)),file=fout);


		

		

