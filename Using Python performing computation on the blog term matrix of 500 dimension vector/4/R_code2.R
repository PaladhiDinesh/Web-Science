data = scan("raw_result.txt")
plot(data,xlab="Number of URI's",ylab="Difference in bytes between New and Old Raw data",main="Differences in bytes for raw data for 1000 URI's",xlim=c(0,1000),col="blue",type="l")
