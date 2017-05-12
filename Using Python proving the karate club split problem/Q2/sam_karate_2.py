from igraph import *
#visual_style = {}
#with open('karate.GraphML','r') as my_data :
#	data=my_data.read()
data=Graph.Read_GraphML('karate.GraphML') #reading graphml data into variable data
#print data
data.vs["label"]=data.vs["name"] #giving names to all the nodes
layout = data.layout("grid_fr") #providing "grid_fr" layout for the graph
plot(data, 'group2.png', layout = layout) #plotting initial graph 
length =len(data.clusters())
count=0
flag1=0
flag = 0
#print length

while length <5 :
	layout = data.layout("grid_fr")
	if (length == 3):
		flag=flag +1
		plot(data, 'output2.png', layout = layout)
		if flag == 4 :
			print data.clusters()
		count1=count
	elif(length == 4) :
		count2=count
		flag1=flag1+1
		plot(data, 'output3.png', layout = layout)
		if flag1 == 5 :
			print data.clusters()
	find_eb= data.edge_betweenness()
	#print find_eb
	#max_eb=max(find_eb)
	#print max_eb
	#a=xrange(len(find_eb))
	#print a
	#key = find_eb.__getitem__
	#print key
	maximum_node = max(xrange(len(find_eb)), key = find_eb.__getitem__) 
	#print maximum_node
	count=count+1

	data.delete_edges(maximum_node)
	length =len(data.clusters())
plot(data, 'output4.png', layout = layout)
print data.clusters()
print "Number of edges deleted for getting 3 clusters are : ",+count1
print "Number of edsge deleted for getting 4 clusters are : ",+count2
print "Number of edges deleted for getting 5 clusters are : ",+count 


