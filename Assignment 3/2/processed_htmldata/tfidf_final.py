import commands
import re
import math
import json
# def find_urls(URI_num):
	# URI_number1= URI_num
	# count =0
	# for each_line in file_2.readlines():
		# count=count+1
		# print count
		# if count == URI_number1:
			# print each_line
			# count =0
			# break
	# return each_line
file_1=open ('10_urls.txt','r')
file_2 = open('only urls.txt','r+') .readlines()
Tot_doc_Google= 47000000000.00
burger_in_google= 263000000.00 
temp_IDF= Tot_doc_Google/burger_in_google
t_IDF= math.log(temp_IDF)/math.log(2)
IDF= round(t_IDF,4) 
#print IDF
print "TFIDF",' ', "Rounded_TF",' ',"IDF",' ', "URI"
for f_name in file_1.readlines(): #To calculate TF and TFIDF
	#print f_name
	#print count
	count=0
	w_doc1= 'wc -w '+ f_name.strip()
	oc_doc1= 'grep -c ' + "burger " + f_name.strip()
	#print oc_doc1
	w_doc=commands.getoutput(w_doc1)
	want_word_count=commands.getoutput(oc_doc1)
	tot_word=w_doc.split(' ')[0]
	#print tot_word,' ',want_word_count 
	TF= float(want_word_count)/float(tot_word)
	Rounded_TF= round(TF,4)
	TFIDF= round(Rounded_TF*IDF,4)
	URI_find=f_name.split('-')
	URI_num=int(URI_find[1])
	i=0
	for each in file_2:
		count =count +1
		if URI_num==count:
			URI=each
			print TFIDF,' ', Rounded_TF,' ',IDF,' ',URI
			i=i+1
			break

	# for i in a:
		# print i
		# print count
		# if count == i:
			# print each
			# break

	#print URI_num
	#URI_1=find_urls(URI_num)
	#print URI_1
# print TF_array
# print TFIDF_array	
# print URI_array


