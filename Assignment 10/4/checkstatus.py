import json
import requests

input= open("my_json_data.json","r")
output=open("status_codes.json","w")
dictionary={}
for uri in input.readlines():
	each_line = json.loads(uri) 
	url = each_line['url']
	try:
		status=requests.get(url)
		print status.status_code
		if status.status_code in dictionary:
			dictionary[status.status_code] +=1
		else:
			dictionary[status.status_code] =1
	except Exception, e:
		print e
		continue
output.write(json.dumps(dictionary))
output.close()