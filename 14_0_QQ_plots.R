names=c("/media/cuelee/cue_workspace/Cue_sumstats/CTG_CNCR/result/03_assoc_result/neuroticism.lsss"
)

results = "/media/cuelee/cue_workspace/Cue_sumstats/CTG_CNCR/result/04_qqplot/lsss.qqplot.png"
library(grid) 
require(graphics)

png(filename=results)
#par(mfrow=c(1,1))

for (i in 1:length(names)){

data <- read.table(names[i],header = T)
cur_ps <- as.numeric(data[,2])

n = nrow(data)/2
print(n)
observed = -log(cur_ps,10)

#if(i%%3!=0){
#expected= -log(c(pchisq(rchisq(n,df=1,ncp=0),df=1,ncp=0,lower.tail=F)
#                 ,pchisq(rchisq(n,df=2,ncp=0),df=2,ncp=0,lower.tail=F)),10)
#} else {expected= -log(pchisq(rchisq(2*n,df=1,ncp=0),df=1,ncp=0,lower.tail=F),10)}
expected= -log(pchisq(rchisq(2*n,df=1,ncp=0),df=1,ncp=0,lower.tail=F),10)

#par(mar = c(3,4,2.1,2.1))

qqplot(
     x=expected
   , y=observed
   , xlab=expression(paste("Expected (",-log[10], " p-value)"))
   , ylab=expression(paste("Observed (",-log[10], " p-value)"))
   ) 
abline(a=0,b=1, col = 2)


  estim_chi_vec <- qchisq(cur_ps, df = 1, ncp = 0, lower.tail=FALSE)
  lambdaGC = median(estim_chi_vec, na.rm = T ) / qchisq(0.5,1)


mtext(bquote(lambda[GC] ~ '=' ~ .(round(lambdaGC,3))),adj=0,cex=1.2)
print(names[i])
print(lambdaGC)
}
dev.off()
