all:
	pdflatex main.tex 
	bibtex main.aux
	pdflatex main.tex 
	pdflatex main.tex 
	mv main.pdf dinesh-A2.pdf

clean:
	rm -v *.aux *.log *.toc *.bbl *.out
	

