import os
directory=os.listdir('/home/dpaladhi/Webscience/cs532-s16/Assignment 10/4/1/processed_htmldata')	
def getSize(filename):
    st = os.stat(filename)
    return st.st_size
	
output=open("processed_data_size.txt","w")	

for line in directory:

	if(line=="processed_data_size.txt"):
		print "yes"
	elif(line=="get_file_size.py"):
		print "yes"
	else:
		size=getSize(line)
		print line,size
		output.write(str(size)+'\n')	