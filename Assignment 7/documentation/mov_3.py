	
from math import sqrt

def sim_pearson(prefs,p1,p2):
  # Get the list of mutually rated items
  si={}
  for item in prefs[p1]: 
    if item in prefs[p2]: si[item]=1

  # if they are no ratings in common, return 0
  if len(si)==0: return 0

  # Sum calculations
  n=len(si)
  
  # Sums of all the preferences
  sum1=sum([int(prefs[p1][it]) for it in si])
  sum2=sum([int(prefs[p2][it]) for it in si])
  
  # Sums of the squares
  sum1Sq=sum([pow(int(prefs[p1][it]),2) for it in si])
  sum2Sq=sum([pow(int(prefs[p2][it]),2) for it in si])	
  
  # Sum of the products
  pSum=sum([int(prefs[p1][it])*int(prefs[p2][it]) for it in si])
  
  # Calculate r (Pearson score)
  num=pSum-(sum1*sum2/n)
  den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
  if den==0: return 0

  r=num/den

  return r
def getRecommendations(prefs,person,similarity=sim_pearson):
  totals={}
  simSums={}
  for other in prefs:
    # don't compare me to myself
    if other==person: continue
    sim=similarity(prefs,person,other)

    # ignore scores of zero or lower
    if sim<=0: continue
    for item in prefs[other]:
	    
      # only score movies I haven't seen yet
      if item not in prefs[person] or prefs[person][item]==0:
        # Similarity * Score
        totals.setdefault(item,0)
        totals[item]+=int(prefs[other][item])*sim
        # Sum of similarities
        simSums.setdefault(item,0)
        simSums[item]+=sim

  # Create the normalized list
  rankings=[(total/simSums[item],item) for item,total in totals.items()]

  # Return the sorted list
  rankings.sort()
  rankings.reverse()
  return rankings

  	
def getmovienames(list) :
	input = open('u.item','r')
	movie_name=[]
	movie_ids=[]
	movie_ratings=[]
	for lane in list:
		movie_ids.append(lane[1])
		movie_ratings.append(lane[0])
	for next in input:
		next=next.split("|")
		id=next[0]
		name=next[1]
		#print list
		if id in movie_ids :
			movie_name.append(name)
	return movie_name,movie_ratings
input = open('u.data','r')

pref = {}
user_count =0
for line in input:
	(user_id,item_id ,rating,ts) = line.split()
	if user_id in pref:
		pref[user_id][item_id] = rating
	else:
		user_count = user_count + 1
		pref[user_id] = {}

result =  getRecommendations(pref,'706',similarity=sim_pearson)
bot_result = result[1 : 5]
top_result = result[-5 :]
print "Most recommended Movies and their ratings"
most,rating=getmovienames(bot_result)
for i in range(0,len(most)) :
	print  most[i],rating[i]
print '\n'
Least,rating=getmovienames(top_result)
print "Least recommended Movies and their ratings"
for k in range(0,len(Least)):
	print Least[k],rating[k] 
