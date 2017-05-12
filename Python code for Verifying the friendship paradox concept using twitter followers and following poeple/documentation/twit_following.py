import tweepy
import time
import csv

csv_writer = csv.writer(open("following_count.csv", "wb"))
csv_writer1 = csv.writer(open("following_count_without_me.csv", "wb"))
csv_writer.writerow(['Name','num_following'])
csv_writer1.writerow(['Name','num_following'])
ACCESS_TOKEN = '118623489-QsSuqItzx8cnReRHI67ylffqpOPNs7z4Qp8hcOiI'  # Variables that contains the user credentials to access Twitter API 
ACCESS_SECRET = 'PAPovgDO6QPy9QV8BbllM8p2MGWrcLLD8pesMHjXxTEMl'
CONSUMER_KEY = 'wxSZ8GSC7aRC7dAsM3m7UqgIg'
CONSUMER_SECRET = 'HuauQk780HuKWyQky9e4J6QM1DlwVxHXuvrLbgHGWhkmRXlvE4'
count = 0

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)   #Authentication is handled by the tweepy.AuthHandler class
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)


api = tweepy.API(auth) # Construct the API instance

for user in tweepy.Cursor(api.friends, screen_name="dineshpaladhi").items():
	csv_writer.writerow([user.screen_name,int(user.friends_count)])
	csv_writer1.writerow([user.screen_name,int(user.friends_count)])
	count=count +1 # to count number of friends of mln
csv_writer.writerow(['dineshpaladhi',count]) 
