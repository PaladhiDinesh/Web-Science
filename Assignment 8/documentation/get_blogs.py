import requests


def get100blogurls():
	file_1 = open('100blogurls','w') 
	unique = set()
	while (len(unique) < 98) : 
		url="http://www.blogger.com/next-blog?navBar=true&blogID=3471633091411211117"
		gen=requests.get(url)
		final_url= gen.url.strip('?expref=next-blog/')
		unique.add(final_url)
		# print final_url
		# print count
		print len(unique)
	for element in unique :
		print element
		file_1.write(element+'\n')
		file_1.flush()
	file_1.write('http://f-measure.blogspot.com'+'\n')
	file_1.write('http://ws-dl.blogspot.com')

def getatomurls():
	input= open('100blogurls','r')
	output= open('100atomurls','w')
	for element in input :
		#print element
		
		add= "/feeds/posts/default?alt=rss"
		item= element.strip() + add
		output.write(item+'\n')
		# output.write('\n')
		print item 

#get100blogurls()
getatomurls()

	