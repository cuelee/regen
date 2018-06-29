names=c("/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/04_result/backup/autoimmune.RE3p.lcorr"
        ,"/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/04_result/backup/autoimmune.RE2p.lcorr"
        ,"/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/04_result/backup/autoimmune.LSp.lcorr"
        ,"/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/04_result/backup/pgc_cross.RE3p.lcorr"
        ,"/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/04_result/backup/pgc_cross.RE2p.lcorr"
        ,"/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/04_result/backup/pgc_cross.LSp.lcorr"
)

results = "/home/cuelee/Dropbox/Bogdan/Cue_Analysis/mainAnalysis/08_qqplot/result_lcorr.pdf"
library(grid) 
require(graphics)

alpha = median(rchisq(1000000,df=1,ncp = 0))

k = function(x,cur_pvalue){
  log_pvalue = -log(cur_pvalue,10);
  log_p <- -log(0.5*pchisq(x,df=1,ncp=0,lower.tail=F)+0.5*pchisq(x,df=2,ncp=0,lower.tail=F),10);
  return(log_p-log_pvalue)
}

d = function(cur_pvalue){
  ret <- uniroot(k,interval=c(0,1426),cur_pvalue=cur_pvalue,tol = 1e-15)$root
  return(ret)
}

k2 = function(x,cur_pvalue){
  log_pvalue = -log(cur_pvalue,10);
  log_p <- -log(pchisq(x,df=1,ncp=0,lower.tail=F),10);
  return(log_p-log_pvalue)
}

d2 = function(cur_pvalue){
  #if (cur_pvalue ==0){cur_pvalue = 1e-300}
  ret <- uniroot(k2,interval=c(0,1426),cur_pvalue=cur_pvalue,tol = 1e-15)$root
  return(ret)
}

pdf(file=results,width = 9, height = 4)
par(mfrow=c(2,3))

for (i in 1:length(names)){

data <- read.table(names[i],header = T)
cur_ps <- as.numeric(data[,6])

n = nrow(data)/2
observed = -log(cur_ps,10)

if(i%%3!=0){
expected= -log(c(pchisq(rchisq(n,df=1,ncp=0),df=1,ncp=0,lower.tail=F)
                 ,pchisq(rchisq(n,df=2,ncp=0),df=2,ncp=0,lower.tail=F)),10)
} else {expected= -log(pchisq(rchisq(2*n,df=1,ncp=0),df=1,ncp=0,lower.tail=F),10)}

par(mar = c(3,4,2.1,2.1))

qqplot(
     x=expected
   , y=observed
   , xlab=expression(paste("Expected (",-log[10], " p-value)"))
   , ylab=expression(paste("Observed (",-log[10], " p-value)"))
   ) 
abline(a=0,b=1, col = 2)


if(i%%3!=0){
  new_chi <- sapply(cur_ps,FUN=d2)
  cur_gc = median(new_chi) / 0.456
  } else {
  new_chi <- sapply(cur_ps,FUN=d2)
  cur_gc = median(new_chi) / 0.456}


mtext(bquote(lambda[GC] ~ '=' ~ .(round(cur_gc,3))),adj=0,cex=1.2)
print(names[i])
print(cur_gc)
}
dev.off()
