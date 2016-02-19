
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

> Pagerank <-- c(0,0,0,0.6,0.6,0.6,0.6,0.6,0.6,0.7)
> 
> TFIDF <-- c(0.0045,0.0067,0.0075,0.0082,0.0082,0.015,0.0352,0.0449,0.1167,0.3606)
> 
> cor.test(TFIDF,Pagerank, method = "kendall", alternative = "greater")

        Kendall's rank correlation tau

data:  TFIDF and Pagerank
z = 2.8088, p-value = 0.002486
alternative hypothesis: true tau is greater than 0
sample estimates:
      tau 
0.7833495 

Warning message:
In cor.test.default(TFIDF, Pagerank, method = "kendall", alternative = "greater") :
  Cannot compute exact p-value with ties
> 
