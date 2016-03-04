from igraph import *
#visual_style = {}
#with open('karate.GraphML','r') as my_data :
#	data=my_data.read()
data=Graph.Read_GraphML('karate.GraphML') #reading graphml data into variable data
#print data
data.vs["label"]=data.vs["name"] #giving names to all the nodes
layout = data.layout("grid_fr") #providing "grid_fr" layout for the graph
color = {1: "green", 2: "orange"}
plot(data, 'group1.png', layout = layout, vertex_color = [color[fact] for fact  in data.vs["Faction"]]) #plotting initial graph 
length =len(data.clusters())
count=0
#print length
while length <2 :
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
layout = data.layout("grid_fr") #providing "grid_fr" layout for the graph
print "Number of edges deleted for getting 2 clusters are : ",+count 
print data.clusters()
plot(data, 'output1.png', layout = layout)
