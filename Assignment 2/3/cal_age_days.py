from datetime import datetime
import json


file_1=open('url_cdate.json','r')
output_file=open('age.csv','w')
file_2=open('mem_grt0.json','r')
output_file2=open('num_mems.csv','w')
		#file_2=open('mem_grt0.json','r')
		#one_element={}
today_date=datetime.now()
#print today_date
#print (today_date-datetime.timedelta(2016,02,8,20,46,40)).days
#print "hello"	
i=0

for each_line in file_1.readlines():
	dumy_line=json.loads(each_line)
	created_date = dumy_line['created_date']
	print created_date
	convert_date=datetime.strptime(created_date,"%Y-%m-%dT%H:%M:%S")
		#print convert_date
	age=(today_date - convert_date).days
		#print age
	#age_int=int(age)
	print age
	print i
	i=i+1
	output_file.write("%s\n" % (age))
for every_line in file_2.readlines():
	dumy_ev_line=json.loads(every_line)
	mems=dumy_ev_line['num_of_mems']
	output_file2.write("%s\n" % (mems))
	
		
output_file.close()
output_file2.close()
file_2.close()
file_1.close()