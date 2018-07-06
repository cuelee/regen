## import modules 
import sys
import os, time 

print("Cue Hyunkyu Lee: {}".format(sys.argv[0].split("/")[-1]));
cur_time = time.strftime("%a, %d %b %Y %H:%M:%S",time.localtime());
print("Job started at: {}".format(cur_time));

reginput_dir = sys.argv[1];
group = sys.argv[2]
nc = int(sys.argv[3]);
nl = int(sys.argv[4]);
code_dir = sys.argv[5];
RECor_dir = sys.argv[6];
GenCor_dir = sys.argv[7];

fra = open(reginput_dir+'/temp/re_argv.txt','w');
fla = open(reginput_dir+'/temp/ls_argv.txt','w');
regcode_path = code_dir + "/RE3.R"
lscode_path = code_dir + "/LS.R"
fin = open(reginput_dir+'/'+group+'.zsa','r');
temp_inname=[reginput_dir+'/temp/'+group+'_'+str(i)+'.zsa' for i in range(nc)];
reg_outname=[reginput_dir+'/temp/'+group+'_'+str(i)+'.rsss' for i in range(nc)];
ls_outname=[reginput_dir+'/temp/'+group+'_'+str(i)+'.lsss' for i in range(nc)];
myFiles = [open(temp_inname[i],'w') for i in range(nc)];

nb = [int(nl/nc)]*nc 
for i in range(nc):
	if (sum(nb) != nl):
		nb[i] = nb[i]+1;

for i in range(nc):
	for j in range(nb[i]):
		line = fin.readline().strip();
		print(line, file = myFiles[i]);
		continue

if(len(fin.readline()) > 0): 
	quit("FATAL ERROR");

reg_lines = ["{} {} {} {} {}".format(regcode_path,temp_inname[i],reg_outname[i],GenCor_dir, RECor_dir) for i in range(nc)];
for i in range(nc):
	print(reg_lines[i],file=fra);

ls_lines = ["{} {} {} {} {}".format(lscode_path,temp_inname[i],ls_outname[i],GenCor_dir, RECor_dir) for i in range(nc)];
for i in range(nc):
	print(ls_lines[i],file=fla);

fin.close();
fra.close();
fla.close();
[myFiles[i].close() for i in range(nc)];


cur_time = time.strftime("%a, %d %b %Y %H:%M:%S",time.localtime());
print("Job finished at: {}".format(cur_time));
