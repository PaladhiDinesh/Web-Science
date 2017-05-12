import re
import urllib2
import json
import sys

def getmementos(url):
	mem_prefix = 'http://mementoproxy.cs.odu.edu/aggr/timemap/link/1/' + url   #memento aggregator is concatenated with the url for which mementos should be found out
	try: 
		response = urllib2.urlopen(mem_prefix)
		time_map = response.read()
	except urllib2.HTTPError:
		time_map = None
	return time_map

find_memento = re.compile(r'rel.*?=.*?"memento".*?')  # To find memento using regular expression
my_urls = open('my_json_data','r+')  #This file contains 1000 urls their tweets,tweet ids and created dates
output_file = open('mem_and_links.json','a')  # This file stores number of mementos for each url
output_file2 = open('only_count.csv','a')
output_file_carbon = open('mem_grt0.json','a')  
one_element={}
count_of_mems = [] #array is created to store count 
for line in my_urls.readlines(): #reads line by line
	each_line = json.loads(line) 
	url = each_line['url']
	memento_data = getmementos(url)

	#print memento_data
	if memento_data == 'Null':
		count = 0
		one_element['num_of_mems'] = count
		one_element['url'] = url
		output_file.write(json.dumps(one_element)+'\n') #adding each element into json file
		#print count,"   ",url
	else:
		count = len(find_memento.findall(str(memento_data))) #forms an array where "memento"" is found and finds the length of that array
		# a=find_memento.findall(str(memento_data))
		# print a
		one_element['num_of_mems'] = count
		one_element['url'] = url
		output_file.write(json.dumps(one_element)+'\n') #adding each element into json file
		output_file2.write("%s\n" % (count))
		if one_element['num_of_mems'] != 0:
			output_file_carbon.write(json.dumps(one_element)+'\n') # for getting urls and mementos for mementos > 0
		#output_file2.write('\r\n')
		#print count,"   ",url
output_file.close()		
output_file2.close()	
output_file_carbon.close()	


