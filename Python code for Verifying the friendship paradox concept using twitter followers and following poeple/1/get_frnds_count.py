from xml.dom.minidom import parse
import csv

all_Data = parse("mln.graphml")
data_tags=all_Data.getElementsByTagName("data") #searching for data tags
csv_writer = csv.writer(open("frnds_count.csv", "wb"))
csv_writer1 = csv.writer(open("frnds_count_without_mln.csv", "wb"))
csv_writer.writerow(['Name','num_frnds'])
csv_writer1.writerow(['Name','num_frnds'])
count = 0
for nod in data_tags:
	 
	if nod.attributes['key'].value=='Label': #searching Label attributes and getting their value
		name = nod.childNodes[0].data
	if nod.attributes['key'].value=='friend_count': #searching friend_count attributes and getting their value
		frnd_count = nod.childNodes[0].data
		csv_writer.writerow([name,int(frnd_count)])
		csv_writer1.writerow([name,int(frnd_count)])
		count=count +1 # to count number of friends of mln
csv_writer.writerow(['Michael Nelson',count]) 