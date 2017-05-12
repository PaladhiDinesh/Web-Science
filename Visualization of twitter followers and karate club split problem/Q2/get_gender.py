import requests
import json 
input= open('followers.json','r')
output=open('gender_data.json','w')
each_line=json.load(input)
dict={}
for i in range(1,61):
	name= each_line["nodes"][i]["name"]

	name=name.partition(" ")
	fname=name[0]
	#print fname
	url="https://api.genderize.io/?name=" +fname
	gen=requests.get(url)
#	print type(gen)
	dict['gen_data']=gen.content
	#print gen_data
	#print type(gen_data)
	output.write(json.dumps(dict)+',\n')