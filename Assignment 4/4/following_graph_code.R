
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

> tmp <- read.csv("following_count.csv")
> following_count <- tmp[,2]
> barplot(following_count,main="Twitter followers and their followers count",xlab="Followers sorted by number of followers they have",ylab="Count of Followers",ylim=c(0,1000))
> arrows(x0=match(c(186),following_count)+12, y0=700, x1=match(c(186), following_count)+12, y1=150, length=0.07, lwd=1.5, col='blue')
> text(x=match(c(186), following_count),pos=4, y=730, labels="dineshpaladhi", col='blue')
> 
