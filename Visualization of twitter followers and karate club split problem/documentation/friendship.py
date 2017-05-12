import tweepy
import json
ACCESS_TOKEN = '118623489-QsSuqItzx8cnReRHI67ylffqpOPNs7z4Qp8hcOiI'  # Variables that contains the user credentials to access Twitter API 
ACCESS_SECRET = 'PAPovgDO6QPy9QV8BbllM8p2MGWrcLLD8pesMHjXxTEMl'
CONSUMER_KEY = 'wxSZ8GSC7aRC7dAsM3m7UqgIg'
CONSUMER_SECRET = 'HuauQk780HuKWyQky9e4J6QM1DlwVxHXuvrLbgHGWhkmRXlvE4'



auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)   #Authentication is handled by the tweepy.AuthHandler class
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth) 

dict1={}
#f2 = open('f2.json','a') 
#f3= open ('trues.json','w')
f5=open('follower_links','r+')
def function():
	edge_elements ={}
	my_foll = open('followers.json','r')
	f1 = open('f1.json','w') 
	
	count=0
	# for user in tweepy.Cursor(api.followers, screen_name="dineshpaladhi").items():
		# count=count+1
	each_line = json.load(my_foll)
	dict={}
	
	for i in range(1,61):
		source_name= each_line["nodes"][i]["screen_name"]
		#print source_name
		for j in range(i,61):
		# try:
			target_name=each_line["nodes"][j+1]["screen_name"]
			dict['source']=source_name
			dict['target']=target_name
			f1.write(json.dumps(dict)+',\n')
			
			# print source_name+','+target_name
			
		
		
def func():
	a=open('f1.json','r')
	each_line1 = json.load(a)
	for user in each_line1:
		source_name=user["source"]
		target_name=user["target"]
		frndshp = api.show_friendship(source_screen_name=source_name, target_screen_name=target_name,count=180)
		# #print type(frndshp)
		#if (frndshp[0].following == True):
		dict1['source1']=frndshp[0].screen_name
		dict1['following']=frndshp[0].following
		dict1['target1']=frndshp[1].screen_name
		dict1['followed_by']=frndshp[0].followed_by
		f2.write(json.dumps(dict1)+',\n')
dict3={}		
def get_trues():
	f2 = open('f2.json','r') 
	each_line2 = json.load(f2)
	for user in each_line2:
		if(user["followed_by"]== True):
			dict3['source']=user["target1"]
			dict3['target']=user["source1"]
			f3.write(json.dumps(dict3)+',\n')
		if(user["following"]== True):
			dict3['source']=user["source1"]
			dict3['target']=user["target1"]
			f3.write(json.dumps(dict3)+',\n')
dict5={}
set=()
def getids():
	f4 = open('followers.json','r') 
	each_line4 = json.load(f4)
	f3 = open('trues.json','r') 
	each_line3 = json.load(f3)
	for user in each_line3:
		src_name=user['source']
		tar_name=user['target']
		#print src_name+','+tar_name
		for i in range(1,61):
			source_n= each_line4["nodes"][i]["screen_name"]
			# if(src_name==source_n):
				# dict5['source']=each_line4["nodes"][i]["id"]
				# f5.write(json.dumps(dict5)+',\n')
			if(tar_name==source_n):
				dict5['target']=each_line4["nodes"][i]["id"]
				f5.write(json.dumps(dict5)+',\n')
				
					
getids()			
#get_trues()
#function()
#func()
