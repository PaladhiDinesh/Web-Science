
R version 3.1.2 (2014-10-31) -- "Pumpkin Helmet"
Copyright (C) 2014 The R Foundation for Statistical Computing
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

> tmp <- read.csv("frnds_count.csv")
> num_frnds <- tmp[,2]
> my_position <- (num_frnds==154)
> barplot(num_frnds,main="Facebook friends and their number of friends",xlab="Friends sorted by increasing number of friends",ylab="Count of Friends",ylim=c(0,4000))
> arrows(x0=match(c(154),num_frnds)+12, y0=(max(num_frnds) - 80), x1=match(c(154), num_frnds)+12, y1=200, length=0.07, lwd=1.5, col='blue')
> text(x=match(c(154), num_frnds)+12, y=(max(num_frnds))+200, labels="Michael nelson", col='blue')
> text(x=match(c(154), num_frnds)+12, y=(max(num_frnds))+200, labels="Michael nelson", col='blue')
