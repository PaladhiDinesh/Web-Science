input1=open("raw_data_size.txt","r")
input2=open("raw_data_size_old.txt","r")
input3=open("processed_data_size.txt","r")
input4=open("processed_data_size_old.txt","r")
output_raw=open("raw_result.txt","w")
output_processed=open("processed_result.txt","w")

array1=[]
array2=[]
array3=[]
array4=[]
raw_result=[]
processed_result=[]


for line in input1:
	array1.append(int(line))	
	
for line in input2:
	array2.append(int(line))	
for line in input3:
	array3.append(int(line))	
	
for line in input4:
	array4.append(int(line))	
		
raw_result = [new - old for new, old in zip(array1, array2)]	
processed_result = [new - old for new, old in zip(array3, array4)]	

for value in raw_result:
	output_raw.write(str(value)+'\n')
	
for value in processed_result:
	output_processed.write(str(value)+'\n')
	
# for i,j in array1,array2:
	# value=i-j
# raw_result=value
# print raw_result
	
# for k,l in array3,array4:
	# value1=k-l
# processed_result=value1
# print processed_result		
	
	# for line1 in input2:
		# value=int(line)-int(line1)
		# output_raw.write(str(value)+'\n')
		
# for line2 in input3:
	# for line3 in input4:
		# value1=int(line2)-int(line3)
		# output_processed.write(str(value1)+'\n')
		