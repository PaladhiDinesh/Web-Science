#from pysqlite2 import dbapi2 as sqlite
from sqlite3 import dbapi2 as sqlite
import re
import math

def getwords(doc):
  splitter=re.compile('\\W*')
  ## Remove all the HTML tags
  doc=re.compile(r'<[^>]+>').sub('',doc)  
  # Split the words by non-alpha characters
  words=[s.lower() for s in splitter.split(doc) 
          if len(s)>2 and len(s)<20]
  
  # Return the unique set of words only
  return dict([(w,1) for w in words])

class classifier:
  def __init__(self,getfeatures,filename=None):
    # Counts of feature/category combinations
    self.fc={}
    # Counts of documents in each category
    self.cc={}
    ## extract features for classification
    self.getfeatures=getfeatures
    
  def setdb(self,dbfile):
    self.con=sqlite.connect(dbfile)
    self.con.execute('create table if not exists rss(num, entry, feature, predicted, actual, cprob)')
    self.con.execute('create table if not exists fc(feature,category,count)')
    self.con.execute('create table if not exists cc(category,count)')
    # remove old data from previous sessions
    # self.con.execute('delete from rss')
    # self.con.execute('delete from fc')
    # self.con.execute('delete from cc')

  def manualClassdb (self,num, entry, feature, predicted, actual):
    self.con.execute("insert into rss values ('%s','%s', '%s', '%s','%s', '%s')"
                     % (num, entry, feature, predicted, actual, None))
    self.con.commit()

  def autoClassdb (self,num, entry, feature, predicted, actual, cp):
    self.con.execute("insert into rss values ('%s','%s', '%s', '%s','%s', '%s')"
                     % (num, entry, feature, predicted, actual, cp))
    self.con.commit()   
  ## Increase the count of a feature/category pair
  def incf(self,f,cat):
    count=self.fcount(f,cat)
    if count==0:
      self.con.execute("insert into fc values ('%s','%s',1)" 
                       % (f,cat.lower()))
    else:
      self.con.execute(
        "update fc set count=%d where feature='%s' and category='%s'" 
        % (count+1,f,cat.lower())) 

  ## The number of times a feature has appeared in a category
  def fcount(self,f,cat):
    res=self.con.execute(
      'select count from fc where feature="%s" and category="%s"'
      %(f,cat)).fetchone()
    if res==None: return 0
    else: return float(res[0])

  ## Increase the count of a category
  def incc(self,cat):
    count=self.catcount(cat)
    if count==0:
      self.con.execute("insert into cc values ('%s',1)" % (cat.lower()))
    else:
      self.con.execute("update cc set count=%d where category='%s'" 
                       % (count+1,cat))    

  ## The number of items in a category
  def catcount(self,cat):
    res=self.con.execute('select count from cc where category="%s"'
                         %(cat)).fetchone()
    if res==None: return 0
    else: return float(res[0])

  ## The list of all categories
  def categories(self):
    cur=self.con.execute('select category from cc');
    return [d[0] for d in cur]

  ## The total number of items
  def totalcount(self):
    res=self.con.execute('select sum(count) from cc').fetchone();
    if res==None: return 0
    return res[0]


  ## The train method takes an item(document) and a classification.
  ## It uses the getfeatures function to the break the item into its
  ## separate features. It then calls incf to increase the counts for
  ## this classification for every feature. Finally, it increases
  ## the total count for this classification.
  def train(self,item,cat):
    features=self.getfeatures(item)
    # Increment the count for every feature with this category
    for f in features:
      self.incf(f,cat)

    # Increment the count for this category
    self.incc(cat)
    self.con.commit()

  ## Probability is a number between 0 and 1, indicating
  ## the likelihood of an event. You calculate the probability of
  ## a word in a particular category by dividing the number of
  ## times the word appears in a document in that category
  ## by the total number of documents in the category.
  def fprob(self,f,cat):
    if self.catcount(cat)==0: return 0

    # The total number of times this feature appeared in this 
    # category divided by the total number of items in this category
    return self.fcount(f,cat)/self.catcount(cat)

  def weightedprob(self,f,cat,prf,weight=1.0,ap=0.5):
    # Calculate current probability
    basicprob=prf(f,cat)

    # Count the number of times this feature has appeared in
    # all categories
    totals=sum([self.fcount(f,c) for c in self.categories()])

    # Calculate the weighted average
    bp=((weight*ap)+(totals*basicprob))/(weight+totals)
    return bp




class naivebayes(classifier):
  
  def __init__(self,getfeatures):
    classifier.__init__(self,getfeatures)
    self.thresholds={}
  
  def docprob(self,item,cat):
    features=self.getfeatures(item)   

    # Multiply the probabilities of all the features together
    p=1
    for f in features: p*=self.weightedprob(f,cat,self.fprob)
    return p

  def prob(self,item,cat):
    catprob=self.catcount(cat)/self.totalcount()
    docprob=self.docprob(item,cat)
    return docprob*catprob
  
  def setthreshold(self,cat,t):
    self.thresholds[cat]=t
    
  def getthreshold(self,cat):
    if cat not in self.thresholds: return 1.0
    return self.thresholds[cat]
  
  def classify(self,item,default=None):
    probs={}
    # Find the category with the highest probability
    max=0.0
    for cat in self.categories():
      probs[cat]=self.prob(item,cat)
      if probs[cat]>max: 
        max=probs[cat]
        best=cat

    # Make sure the probability exceeds threshold*next best
    for cat in probs:
      if cat==best: continue
      if probs[cat]*self.getthreshold(best)>probs[best]: return default
    return best

## This function will return the probability that an item with the
## specified feature belongs in the specified category, assuming there
## will be an equal number of items in each category.
class fisherclassifier(classifier):
  def cprob(self,f,cat):
    # The frequency of this feature in this category    
    clf=self.fprob(f,cat)
    if clf==0: return 0

    # The frequency of this feature in all the categories
    freqsum=sum([self.fprob(f,c) for c in self.categories()])

    # The probability is the frequency in this category divided by
    # the overall frequency
    p=clf/(freqsum)
    
    return p

  
  def fisherprob(self,item,cat):
    # Multiply all the probabilities together
    p=1
    features=self.getfeatures(item)
    for f in features:
      p*=(self.weightedprob(f,cat,self.cprob))

    # Take the natural log and multiply by -2
    fscore=-2*math.log(p)
    fprobvalue=self.invchi2(fscore,len(features)*2)
    #print fprobvalue

    # Use the inverse chi2 function to get a probability
    return fprobvalue

  ## Inverse chi-squared function
  def invchi2(self,chi, df):
    m = chi / 2.0
    sum = term = math.exp(-m)
    for i in range(1, df//2):
        term *= m / i
        sum += term
    return min(sum, 1.0)

  def __init__(self,getfeatures):
    classifier.__init__(self,getfeatures)
    self.minimums={}

  def setminimum(self,cat,min):
    self.minimums[cat]=min
  
  def getminimum(self,cat):
    if cat not in self.minimums: return 0
    return self.minimums[cat]
  
  def classify(self,item,default=None):
    # Loop through looking for the best result
    best=default
    max=0.0
    for c in self.categories():
      p=self.fisherprob(item,c)
      # Make sure it exceeds its minimum
      if p>self.getminimum(c) and p>max:
        best=c
        max=p
    return best