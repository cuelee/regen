## import modules 
import os, time
import sys
import numpy as np
import scipy.stats

sourcerun="/bin/bash -c 'source /home/cuelee/anaconda2/activate ldsc; ";
print(" Cue Hyunkyu Lee: {}.".format(sys.argv[0].split("/")[-1]));
cur_time = time.strftime("%a, %d %b %Y %H:%M:%S",time.localtime());
print(" Job started at: {}".format(cur_time));

def LS_z(betas, stders, cor):
	bes = list(map(float,betas))
	C = np.matrix(cor, dtype=float)
	stds_np = np.matrix( np.diag( list(map(float,stders)) ) )
	
	V = stds_np.dot(C).dot(stds_np)
	Vinv = np.linalg.inv(V)
	ones = np.matrix(list(map(float,[1]*len(bes))))
	
	newv = 1 / (ones.dot(Vinv).dot(ones.transpose()))
	newx = np.matrix(ones).dot(Vinv).dot(np.matrix(bes).transpose()) / (ones.dot(Vinv).dot(ones.transpose()))	
	newstd = np.sqrt(newv)
	newz = newx/newstd
	return(float(newz)) 


## Set parameters
ldsc_dir = sys.argv[1]
meta_dir = sys.argv[2]
work_dir = sys.argv[3]
trait1 = sys.argv[4]
trait2 = sys.argv[5]
cur_intercept = float(sys.argv[6])
cur_correlation = cur_intercept - 1
RSID = "SNP"
sumstat_ext = ".intSimple"

print("\n Current traits are: {} and {}".format(trait1,trait2))
## main
trait1_array = []
with open (work_dir+"/"+trait1+sumstat_ext,"r") as t1file:
	frn=False
	for line in t1file:
		if (frn==False):
			frn=True
			colnames1=line.split()
			continue
		split_line=line.split()
		trait1_array.append(split_line)
t1file.close()

trait2_array = []
with open (work_dir+"/"+trait2+sumstat_ext,"r") as t2file:
	frn=False
	for line in t2file:
		if (frn==False):
			frn=True
			colnames2=line.split()
			continue
		split_line=line.split()
		trait2_array.append(split_line)
t2file.close()

## get rsid lists 
rsid_t1 = []
rsid_t2 = []

rsid_ind = colnames1.index(RSID)
trait1_sorted = list(sorted(trait1_array, key=lambda x: x[rsid_ind]))
for line in trait1_sorted:
	rsid_t1.append(line[rsid_ind])

rsid_ind = colnames2.index(RSID)
trait2_sorted = list(sorted(trait2_array, key=lambda x: x[rsid_ind]))
for line in trait2_sorted:
	rsid_t2.append(line[rsid_ind])

## perform a sanity check of the RSID lists
if (len(rsid_t1)==len(set(rsid_t1)) and len(rsid_t2)==len(set(rsid_t2))):
	print("Both traits passed the sanity checks for the RSIDs")
else:
	sys.exit("It fails the sanity checks for the RSIDS")

## find the common snps
common_snps_list = list(set(rsid_t1).intersection(rsid_t2))
sorted_common_snps = list(sorted(common_snps_list))

trait1_common = []
ind = 0 
for line in trait1_sorted:
	if(line[0]==sorted_common_snps[ind]):
		trait1_common.append(line)
		if (ind < len(sorted_common_snps) - 1):
			ind = ind + 1

trait2_common = [] 
ind = 0 
for line in trait2_sorted:
	if(line[0]==sorted_common_snps[ind]):
		trait2_common.append(line)
		if (ind < len(sorted_common_snps) - 1):
			ind = ind + 1

## get rsid lists
rsid_t1 = []
rsid_t2 = []

rsid_ind = colnames1.index(RSID)
for line in trait1_common:
	rsid_t1.append(line[rsid_ind])
	

rsid_ind = colnames1.index(RSID)
for line in trait2_common:
	rsid_t2.append(line[rsid_ind])

## check the identity
if (rsid_t1 == rsid_t2 and rsid_t1 == sorted_common_snps):
	print("Found {} common snps".format(len(rsid_t1)))

## indexing and create
output_filename = meta_dir+"/"+trait1+"_"+trait2+".intCorrected"
print("Write the output_file {}_{}.intCorrected".format(trait1,trait2))
with open(output_filename,"w") as outf:
	c_ij=cur_correlation
	
	if (colnames1==colnames2):
		print(' '.join(colnames1),file=outf)
	else:
		sys.exit("Found inconsistency in column names")

	for aind in range(len(common_snps_list)):

		if (trait1_common[aind][0]==trait2_common[aind][0] and trait1_common[aind][1]==trait2_common[aind][1] and trait1_common[aind][2]==trait2_common[aind][2]):
			betas=[float(trait1_common[aind][4]),float(trait2_common[aind][4])]
			newN=int(round(float(trait1_common[aind][3]) + float(trait2_common[aind][3]),0))
			newZ=LS_z(betas=betas,stders=[1,1],cor=[[1,c_ij],[c_ij,1]])
			newP=scipy.stats.distributions.chi2.sf(float(newZ)**2,df=1,loc=0,scale=1)
			print( " ".join(map(str,trait1_common[aind][:3]))+" "+str(newN)+" "+str(newZ)+" "+str(newP) ,file=outf)
		elif (trait1_common[aind][0]==trait2_common[aind][0] and trait1_common[aind][1]==trait2_common[aind][2] and trait1_common[aind][2]==trait2_common[aind][1]):
			## if the risk and ref alleles are reversed 
			betas=[float(trait1_common[aind][4]),-float(trait2_common[aind][4])]
			newN=int(round(float(trait1_common[aind][3]) + float(trait2_common[aind][3]),0))
			newZ=LS_z(betas=betas,stders=[1,1],cor=[[1,c_ij],[c_ij,1]])
			newP=scipy.stats.distributions.chi2.sf(float(newZ)**2,df=1,loc=0,scale=1)
			print( " ".join(map(str,trait1_common[aind][:3]))+" "+str(newN)+" "+str(newZ)+" "+str(newP) ,file=outf)

		else:
			sys.exit("Something's going wrong during the analysis")
outf.close()

# run Munge_sumstats.py
munge_filepath=ldsc_dir+"/munge_sumstats.py "
merge_allele = "--merge-allele "+ldsc_dir+"/ldfile/eur_w_ld_chr/w_hm3.snplist "
input_munge = "--sumstats "+output_filename+" "
out_munge = "--out "+output_filename
command_argument_munge=munge_filepath+input_munge+merge_allele+out_munge
print(sourcerun+command_argument_munge"'")
os.system(sourcerun+command_argument_munge+"'")

## run ldsc.py
ldsc_filepath=ldsc_dir+"/ldsc.py "
ldsc_input="--h2 "+output_filename+".sumstats.gz "
ldsc_ref = "--ref-ld-chr "+ldsc_dir+"/ldfile/eur_w_ld_chr/ "
ldsc_w  = "--w-ld-chr "+ldsc_dir+"/ldfile/eur_w_ld_chr/ "
ldsc_output="--out "+output_filename+"_ldsc"
command_argument_ldsc=ldsc_filepath+ldsc_input+ldsc_ref+ldsc_w+ldsc_output
print(sourcerun+command_argument_ldsc+"'")
os.system(sourcerun+command_argument_ldsc+"'")


