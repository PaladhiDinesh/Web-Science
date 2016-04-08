import clusters
blog,words,data=clusters.readfile('blogdata.txt')
variable = clusters.hcluster(data)

# print ASCII dendrogram
clusters.printclust(variable, labels=blog)

# save JPEG dendrogram
clusters.drawdendrogram(variable, blog, jpeg='clusterblog.jpg')