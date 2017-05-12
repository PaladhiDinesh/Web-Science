
R version 3.2.3 (2015-12-10) -- "Wooden Christmas-Tree"
Copyright (C) 2015 The R Foundation for Statistical Computing
Platform: i386-w64-mingw32/i386 (32-bit)

R is free software and comes with ABSOLUTELY NO WARRANTY.
You are welcome to redistribute it under certain conditions.
Type 'license()' or 'licence()' for distribution details.

  Natural language support but running in an English locale

R is a collaborative project with many contributors.
Type 'contributors()' for more information and
'citation()' on how to cite R or R packages in publications.

Type 'demo()' for some demos, 'help()' for on-line help, or
'help.start()' for an HTML browser interface to help.
Type 'q()' to quit R.

> hist_mementos = scan("only_count.csv")
Read 1000 items
> hist(hist_mementos,xlab= "Number of Mementos" , ylab= "Number of URI's",main ="Histogram of momento/URI's",ylim=c(0,800),las=1,col=3)
> hist(hist_mementos,xlab= "Number of Mementos" , ylab= "Number of URI's",main ="Histogram of momento/URI's",xlim=c(0,150),ylim=c(0,200),las=1,breaks=100000,col=3)
> 
