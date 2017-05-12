import json
import commands
import hashlib

file_1 = open('my_json_data.json','r') 
count = 0
for each_line in file_1.readlines():
	dumy_line=json.loads(each_line)
	url = dumy_line['url']
	hash = hashlib.md5(url.encode())
	final_hash = hash.hexdigest() 
	count = count +1
	file_name_1= "Raw"+'-'+str(count) + '-' + final_hash + '.txt'
	co_1 = 'curl -s -L ' + url + ' > ./Raw_Htmldata/' + file_name_1
	commands.getoutput(co_1)
	file_name_2= "processed"+'-'+str(count) + '-' + final_hash + '.txt' #Naming a file
	co_2 = 'lynx -dump -force_html ' + url + ' > ./processed_htmldata/' + file_name_2 #writes files into processed_htmldata folder
	commands.getoutput(co_2)
	#print url,' ',count,' ',file_name_1