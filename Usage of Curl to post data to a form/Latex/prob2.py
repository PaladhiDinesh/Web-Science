import urllib2
import requests
import sys
from bs4 import BeautifulSoup


def valid_url(url):   #Function to eliminate href's which are not url's 
    try:
        urllib2.urlopen(url) 
        return True
    except Exception, e:
        return False

url = urllib2.urlopen(sys.argv[1]).read()  #Reads the entire data from the url given in the command prompt
soup = BeautifulSoup(url)
all_links= soup.find_all('a',href=True) # getting only anchor tag data
print "link","  ","Content length","   ","Response Code"  # Supportive text
for line in soup.find_all('a'):
		hrefLink = line.get('href') 
		if valid_url(hrefLink) : #Calling the function defined above
			response=urllib2.urlopen(hrefLink)
			link_header=response.headers
			type=link_header["Content-type"]
			if type=="application/pdf":  #Checking whether the file is pdf or not
				print hrefLink,"   ", link_header["content-length"],"  ",response.getcode()
