## import modules 
import sys
import os, time 

cur_time = time.strftime("%a, %d %b %Y %H:%M:%S",time.localtime());
print("Cue Hyunkyu Lee: {}".format(sys.argv[0].split("/")[-1]));
print("Job started at: {}".format(cur_time));

reginput_dir = sys.argv[1];
group = sys.argv[2]
nc = int(sys.argv[3]);
nl = int(sys.argv[4]);
RECor_dir = sys.argv[6];
GenCor_dir = sys.argv[7];

print(sys.argv)

fargv = open(reginput_dir+'/temp/argv.txt','w');
fin = open(reginput_dir+'/'+group+'.zsa','r');
temp_inname=[reginput_dir+'/temp/'+group+'_'+str(i)+'.zsa' for i in range(nc)];
reg_outname=[reginput_dir+'/temp/'+group+'_'+str(i)+'.rsss' for i in range(nc)];
ls_outname=[reginput_dir+'/temp/'+group+'_'+str(i)+'.lsss' for i in range(nc)];
myFiles = [open(temp_inname[i],'w') for i in range(nc)];

reg_lines = ["{} {} {} {}".format(temp_inname[i],reg_outname[i],GenCor_dir, RECor_dir) for i in range(nc)];
for i in range(nc):
	print(reg_lines[i],file=fargv);

ls_lines = ["{} {} {} {}".format(temp_inname[i],ls_outname[i],GenCor_dir, RECor_dir) for i in range(nc)];
for i in range(nc):
	print(ls_lines[i],file=fargv);

fin.close();
fargv.close();
[myFiles[i].close() for i in range(nc)];


