data = scan("difference_new-old.csv")
plot(data,xlab="Number of URI's",ylab="Difference in bytes between New and Old Raw data",main="Differences in the number of Mementos for Old and New data for 1000 URI's",xlim=c(0,1000),ylim=c(-2,20),col="blue",type="l")
