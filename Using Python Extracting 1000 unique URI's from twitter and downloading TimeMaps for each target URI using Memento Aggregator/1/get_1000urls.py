# I have queried subway,walmart,trump,McDonalds,Old Dominion
import urllib
import json
import tweepy
import sys
import time

ACCESS_TOKEN = '118623489-QsSuqItzx8cnReRHI67ylffqpOPNs7z4Qp8hcOiI'  # Variables that contains the user credentials to access Twitter API 
ACCESS_SECRET = 'PAPovgDO6QPy9QV8BbllM8p2MGWrcLLD8pesMHjXxTEMl'
CONSUMER_KEY = 'wxSZ8GSC7aRC7dAsM3m7UqgIg'
CONSUMER_SECRET = 'HuauQk780HuKWyQky9e4J6QM1DlwVxHXuvrLbgHGWhkmRXlvE4'
i=0

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)   #Authentication is handled by the tweepy.AuthHandler class
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)


api = tweepy.API(auth) # Construct the API instance

var=sys.argv[1] 							#Takes input from command prompt
list_of_urls=set()  			#declaring url list as set to avoid duplicate url's
output_file=open('my_json_data','a')				#
Final_results = tweepy.Cursor(api.search,q=var).items()
while True:
	try:
		status = Final_results.next()
		element=status._json
		one_element={} #  below code is to write data into json format
		
		i=i+1
		for url in element['entities']['urls']: # to get url's from each tweet
			if len(list_of_urls) == 1000:  #url count
				break
			else:
				response=urllib.urlopen(url['url'])
				final_url=response.url
				print response.getcode()
				print final_url
				print len(list_of_urls)
				if response.getcode()==200: #checking where status code is 200 or not
					if final_url in list_of_urls:
						break
					else:
						one_element['tweet_id'] = element['id_str']  #storing tweet id and date of creation of it in json file
						one_element['date_of_creation'] = element['user']['created_at']
						list_of_urls.add(final_url)
						one_element['url']=final_url
						output_file.write(json.dumps(one_element)+'\n') #adding each element into json file
						
		if len(list_of_urls) == 1000:  #url count
			break	
	except tweepy.TweepError :
		time.sleep(60 * 1)
        continue
print len(list_of_urls)
