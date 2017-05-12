import tweepy
import json
import time

output_file = open("followers.json", "w")

ACCESS_TOKEN = '118623489-QsSuqItzx8cnReRHI67ylffqpOPNs7z4Qp8hcOiI'  # Variables that contains the user credentials to access Twitter API 
ACCESS_SECRET = 'PAPovgDO6QPy9QV8BbllM8p2MGWrcLLD8pesMHjXxTEMl'
CONSUMER_KEY = 'wxSZ8GSC7aRC7dAsM3m7UqgIg'
CONSUMER_SECRET = 'HuauQk780HuKWyQky9e4J6QM1DlwVxHXuvrLbgHGWhkmRXlvE4'


count = 0

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)   #Authentication is handled by the tweepy.AuthHandler class
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

elements={}
edge_elements ={}
count =0
output_file.write('{\n "nodes": [\n')
#try:
api = tweepy.API(auth) # Construct the API instance
elements['screen_name']="dineshpaladhi"
elements['name']="dinesh"
elements['image_url']="https://github.com/favicon.ico"
elements['id']=0
output_file.write(json.dumps(elements)+',\n')
for user in tweepy.Cursor(api.followers, screen_name="dineshpaladhi").items():
	count=count+1
	elements['screen_name']=user.screen_name
	elements['name']=user.name
	elements['id']=count
	elements['image_url']=user.profile_image_url_https
	output_file.write(json.dumps(elements)+',\n')
output_file.write('],\n')
output_file.write('"links": [\n')
count=0
for user in tweepy.Cursor(api.followers, screen_name="dineshpaladhi").items():
	count=count+1
	edge_elements['source']= count
	edge_elements['target']=0 
	output_file.write(json.dumps(edge_elements)+',\n')
output_file.write(']\n}')

















