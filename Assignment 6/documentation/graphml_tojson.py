import sys
import json
from bs4 import BeautifulSoup

input_file = open('karate.GraphML','r')
output_file = open('karate.json','w')

soup_data=BeautifulSoup(input_file)
#print soup_data
elements={}
edge_elements={}
output_file.write('{\n "nodes": [\n')
for node in soup_data.find_all('node'):
	node_data=dict(node.attrs)
	#print node_data
	id=node_data['id']
	id_val=int(id.strip('n'))
	#print id
	#print id_val
	faction,name = node.find_all('data')
	faction_val=faction.contents
	name_val=name.contents
	elements['id']=id_val
	elements['faction']=int(faction_val[0])
	elements['name']=str(name_val[0])
	#print count
	output_file.write(json.dumps(elements)+',\n')
	if(id_val == 33):
		output_file.write('],\n')
		break
output_file.write('"links": [\n')
for edge in soup_data.find_all('edge'):
	edge_data=dict(edge.attrs)
	edge_src=edge_data['source']
	edge_src_Val=int(edge_src.strip('n'))
	edge_target=edge_data['target']
	edge_target_Val=int(edge_target.strip('n'))
	weight = edge.find('data')
	weight_val=int(weight.contents[0])
	edge_elements['source']=edge_src_Val
	edge_elements['target']=edge_target_Val
	edge_elements['weight']=weight_val
	output_file.write(json.dumps(edge_elements)+',\n')
	if(edge_src_Val == 32):
		output_file.write(']\n}')
		break
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	