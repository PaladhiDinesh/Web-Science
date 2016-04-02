#!/usr/local/bin/python
import sys
import recommendations

if __name__ == '__main__':
    fav_moviename   = "Die Hard (1988)"
    hate_moviename = "Kazaam (1996)"
    prefs = recommendations.loadMovieLens()
    itemPrefs = recommendations.transformPrefs(prefs)
    fav_results   = recommendations.topMatches(itemPrefs,fav_moviename,2000)
    hate_results   = recommendations.topMatches(itemPrefs,hate_moviename,2000)
    
print "Most 5 correlated for my top favourite movie"
for i in fav_results[0:5]:
	print i[0],i[1]
print '\n'
print "Least 5 correlated for my top favourite movie"    
fav_results.reverse()
for i in fav_results[0:5]:
	print i[0],i[1]
print '\n'        
print "Most 5 correlated for my least favourite movie"
for i in hate_results[0:5]:
	print i[0],i[1]
print '\n'
print "Least 5 correlated for my least favourite movie"    
hate_results.reverse()
for i in hate_results[0:5]:
	print i[0],i[1]
        
