	
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
		
result = []
for i in range(1,user_count+1):
	cofficient =  sim_pearson(pref,'706',str(i))
	result.append((cofficient, i))
result.sort()
result.reverse()
a=result[:5]
print "Most Correlated"	
for i in a:
	print i
print '\n'
result.reverse()
print "Least Correlated"
b=result[:5]	
for i in b:
	print i


