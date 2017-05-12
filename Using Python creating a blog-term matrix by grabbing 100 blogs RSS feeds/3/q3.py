
import clusters
blog,words,data=clusters.readfile('blogdata.txt')

print "For k=5"
kclust=clusters.kcluster(data, k=5)
for i in range(0,5):
	print "-----Blognames in centroid"+' '+str(i+1)+'-------'
	for r in kclust[i]:
		print blog[r]
	print '\n'
print "For k=10"
kclust=clusters.kcluster(data, k=10)
for i in range(0,10):
	print "-----Blognames in centroid"+' '+str(i+1)+'-------'
	for r in kclust[i]:
		print blog[r]
	print '\n'

print "For k=20"
kclust=clusters.kcluster(data, k=20)
for i in range(0,20):
	print "-----Blognames in centroid"+' '+str(i+1)+'-------'
	for r in kclust[i]:
		print blog[r]
	print '\n'
