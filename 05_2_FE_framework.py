## import modules
import os, time
import sys
import numpy as np
import scipy.stats

print(" Cue Hyunkyu Lee: {}".format(sys.argv[0].split("/")[-1]));
cur_time = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime());
print(" Job started at: {}".format(cur_time));

def LS_z(betas, stders, cor):
        bes = list(map(float,betas))
        C = np.matrix(cor,dtype=float)
        stds_np = np.matrix( np.diag( list(map(float,stders)) ) )

        V = stds_np.dot(C).dot(stds_np)
        Vinv = np.linalg.inv(V)
        ones = np.matrix(list(map(float,[1]*len(bes))))

        newv = 1 / (ones.dot(Vinv).dot(ones.transpose()))
        newx = np.matrix(ones).dot(Vinv).dot(np.matrix(bes).transpose()) / (ones.dot(Vinv).dot(ones.transpose()))
        newstd = np.sqrt(newv)
        newz = newx/newstd
        return(float(newz)) 

## set parameters
ldsc_path = sys.argv[1]
out_dir = sys.argv[2]
meta_dir = sys.argv[3]
traits = sys.argv[4].split(",")
## Actually we don't need the pprevs and sprevs
#pprevs = sys.argv[5].split(",")
#sprevs = sys.argv[6].split(",")
RSID = "SNP"
trait_extension=".intSimple"
software_dir = ldsc_path
## 
print(traits)

for i in range(len(traits)-1):
	for j in range(i+1, len(traits),1):

		print("\nCurrent traits are: {} and {}".format(traits[i],traits[j]))
		## main
		trait1_array = []
		with open (out_dir+"/"+traits[i]+trait_extension,"r") as my_file:

			frn=False
			for line in my_file:
				if (frn==False):
					frn=True
					colnames1=line.split()
					continue
				split_line=line.split()
				trait1_array.append(split_line)

		my_file.close()

		trait2_array = []
		with open (out_dir+"/"+traits[j]+trait_extension,"r") as my_file:
			frn=False
			for line in my_file:
				if (frn==False):
					frn=True
					colnames2=line.split()
					continue
				split_line=line.split()
				trait2_array.append(split_line)

		my_file.close()

		## get rsid lists
		rsid_t1 =[] 
		rsid_t2 =[] 

		rsid_ind=colnames1.index(RSID)
		trait1_sorted = list(sorted(trait1_array, key=lambda x: x[rsid_ind]))
		for line in trait1_sorted:
			rsid_t1.append(line[rsid_ind])

		rsid_ind=colnames2.index(RSID)
		trait2_sorted = list(sorted(trait2_array, key=lambda x: x[rsid_ind]))
		for line in trait2_sorted:
			rsid_t2.append(line[rsid_ind])


		## find the common snps
		common_snps_list = list(set(rsid_t1).intersection(rsid_t2))
		sorted_common_snps = list(sorted(common_snps_list))

		## perform a sanity check of the RSID lists
		if (len(rsid_t1)==len(set(rsid_t1)) and len(rsid_t2)==len(set(rsid_t2))):
			print("Both traits passed the sanity checks for the RSIDs")
		else: 	
			sys.exit("ERROR in the sanity check")

		trait1_common = []
		ind = 0
		for line in trait1_sorted:
			if(line[0]==sorted_common_snps[ind]):
				trait1_common.append(line)
				if (ind < len(sorted_common_snps)-1): 
					ind=ind+1

		trait2_common = []
		ind = 0
		for line in trait2_sorted:
			if(line[0]==sorted_common_snps[ind]):
				trait2_common.append(line)
				if (ind < len(sorted_common_snps)-1):
					ind=ind+1


		## get rsid lists
		rsid_t1 =[] 
		rsid_t2 =[] 

		for line in trait1_common:
			rsid_t1.append(line[rsid_ind])

		for line in trait2_common:
			rsid_t2.append(line[rsid_ind])

		if(rsid_t1 == rsid_t2 and rsid_t1 == sorted_common_snps):
			print("Found {} of common snps".format(len(rsid_t1)))

		## indexing and created the combined summary stats
		output_filename = meta_dir+"/"+traits[i]+"_"+traits[j]+".sumstats"
		print("Write the output_file {}_{}.sumstats".format(traits[i],traits[j]))

		with open(output_filename,"w") as outf:


			if (colnames1==colnames2): 
				print(' '.join(colnames1),file=outf)
			else:
				sys.exit("Found inconsistency in column names")

			for aind in range(len(common_snps_list)):
					
				if (trait1_common[aind][0]==trait2_common[aind][0] and trait1_common[aind][1]==trait2_common[aind][1] and trait1_common[aind][2]==trait2_common[aind][2]):
					betas=[float(trait1_common[aind][4]),float(trait2_common[aind][4])]
					newN=int(round(float(trait1_common[aind][3]) + float(trait2_common[aind][3]),0))
					newZ=LS_z(betas=betas,stders=[1,1],cor=[[1,0],[0,1]])
					newP=scipy.stats.distributions.chi2.sf(float(newZ)**2,df=1,loc=0,scale=1)
					print( " ".join(map(str,trait1_common[aind][:3]))+" "+str(newN)+" "+str(newZ)+" "+str(newP) ,file=outf)

				elif (trait1_common[aind][0]==trait2_common[aind][0] and trait1_common[aind][1]==trait2_common[aind][2] and trait1_common[aind][2]==trait2_common[aind][1]):
					## if the risk and ref alleles are reversed 
					print("CHECK input");
					betas=[float(trait1_common[aind][4]),-float(trait2_common[aind][4])]
					newN=int(round(float(trait1_common[aind][3]) + float(trait2_common[aind][3]),0))
					newZ=LS_z(betas=betas,stders=[1,1],cor=[[1,0],[0,1]])
					newP=scipy.stats.distributions.chi2.sf(float(newZ)**2,df=1,loc=0,scale=1)
					print( " ".join(map(str,trait1_common[aind][:3]))+" "+str(newN)+" "+str(newZ)+" "+str(newP) ,file=outf)

				else:
					sys.exit("Something's going wrong during the analysis")
		outf.close()

cur_time = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime());
print(" Job finished at: {}".format(cur_time));
