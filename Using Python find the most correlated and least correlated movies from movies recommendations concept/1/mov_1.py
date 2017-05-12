import json
import re
from math import sqrt

def getData():
	# ratingDataFile = open("ratingData.json","w")
	# ratingData ={}
	# for line in open('u.data'):
		# (user, movieid, rating, ts) = line.split('\t')
		# ratingData['user'] = user.strip()
		# ratingData['movieid'] = movieid.strip()
		# ratingData['rating'] = rating.strip()
		# # ratingData['ts'] = ts.strip()
		# ratingDataFile.write(json.dumps(ratingData)+",\n")

	# moviesDataFile = open("movieData.json","w")
	# movies = {}
	# for line in open('u.item'):
		# movie_id = line.split('|')[0:1][0]
		# movie_name = line.split('|')[1:2][0]
		# movies['movie_id'] = re.sub(r'[^\x00-\x7F]',' ', movie_id)
		# movies['movie_name'] = re.sub(r'[^\x00-\x7F]',' ', movie_name)
		# moviesDataFile.write(json.dumps(movies) + ',\n')	
	
	
	userDataFile = open("u_data.json","w")
	UserData = {}
	for line in open('u.user'):
		UserData['user_id'] = line.split('|')[0]
		userDetails = {}
		userDetails['age'] = line.split('|')[1]
		userDetails['occupation'] = line.split('|')[3]
		userDetails['gender'] = line.split('|')[2]
		UserData['user_details']= userDetails
		ratingDataFile = open("ratingData.json","r")
		ratingData = json.load(ratingDataFile)
		movieDetails_list = []
		for user1 in ratingData:
			r_id = user1['user']
			if UserData['user_id'] == r_id:
				movieDetails= {}
				movieDetails['movie_id'] = user1['movieid']
				movieDetails['movie_rating'] = user1['rating']
				moviesDataFile = open("movieData.json","r")
				movieData = json.load(moviesDataFile)
				for user2 in movieData:
					movie_id = user2['movie_id']
					if user1['movieid'] == movie_id:
						movieDetails['movie_name'] = user2['movie_name']
						break
				moviesDataFile.close()
				movieDetails_list.append(movieDetails)
		ratingDataFile.close()
		UserData['movie_details']= movieDetails_list
		userDataFile.write(json.dumps(UserData) + ',\n')
	
def getsimilarusers() :
	output_1= open("similarusers.json",'w')
	input_file=open("u_data.json",'r')
	input_data=json.load(input_file)
	for line in input_data :
		if(line['user_details']['gender']=='M' and line['user_details']['age']=='23' and line['user_details']['occupation']=='student') :	
			output_1.write(json.dumps(line) + ',\n')
			#print line['user_id']
def gettopbot3() :
	input_file=open("similarusers.json",'r')
	input_data=json.load(input_file)
	tcount=1
	bcount=1
	
	for line in input_data :
		print "User :"+line['user_id']
		print '\n'
		print "Top 3 favourite films are "
		for film in line['movie_details'] :
			
			if(tcount <= 3):
				if (film['movie_rating'] =='5'):
					tcount +=1
					
					print film['movie_name']+','+film['movie_rating']		
		for film in line['movie_details'] :
			
			if(tcount <= 3):
				if (film['movie_rating'] =='4'):
					tcount +=1
					
					print film['movie_name']+','+film['movie_rating']
		print '\n'
		print "Bottom 3 least favourite films are "
		for film in line['movie_details'] :
			
			if(bcount <= 3):
				if (film['movie_rating'] =='1'):
					bcount +=1
					
					print film['movie_name']+','+film['movie_rating']
		for film in line['movie_details'] :
			
			if(bcount <= 3):
				if (film['movie_rating'] =='2'):
					bcount +=1
					
					print film['movie_name']+','+film['movie_rating']
		print '\n'
		tcount=1
		bcount=1
		#135,391,706
#706 is my substitute user because I like all the movies highly rated by him and I don't like his least rated movies except Fargo	
	
#getsimilarusers()
gettopbot3()
#getData()	