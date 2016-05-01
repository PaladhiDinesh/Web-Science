import json

input=open('blogdata.txt','r')
output=open('rowassign','w')
flag=0
row=[]
for i in input:
	flag=flag+1
	if flag >1:
		dictionary={}
		i=i.strip()
		drow=i.split('\t')
		name=drow[0]
		drow.pop(0)
		rowassign=drow
		print name
		print rowassign
		dictionary[name]=rowassign #assigning each row vector to a blog
		row.append(dictionary)
output.write(json.dumps(row))		