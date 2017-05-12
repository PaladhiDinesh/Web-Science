
import feedparser
import re
import math
import docclass
# Takes a filename or URL of a blog feed and classifies the entries
def read(feed,classifier):

  splitRegexp = re.compile( r"<[^>]+>" )

  num=0
  Get feed entries and loop over them
  f=feedparser.parse(feed)
  print
  print '----- Begin manual classification (training) -----'
  for entry in f['entries'][0:50]:
    num=num +1
    # Print the contents of the entry
    title=entry['title'].encode('utf-8').replace("'","")
    print 'Title:     '+ title
    
    description = splitRegexp.sub( "", entry[ "description" ] )
    
    print description #entry['description'].encode('utf-8')

    # Combine all the text to create one item for the classifier
    #fulltext='%s\n%s\n%s' % (entry['title'],entry['publisher'],entry['description'])
    fulltext='%s\n%s' % (entry['title'],entry['description'])
    # Remove apostrophes
    fulltext=fulltext.replace("'","")
    # Print the best guess at the current category
    predicted=str(classifier.classify(fulltext))
    print 'Predicted category: ', predicted

    # Ask the user to specify the correct category and train on that
    actual=raw_input('Actual category: ')
    feature=None
    classifier.train(fulltext, actual)
 
    # Save the manual classifications
    # num, entry, feature, predicted, actual, cprob=None
    classifier.manualClassdb(num, title, feature, predicted, actual)
  
#def autoClassify(feed,classifier):
  num=50
  print '----- Begin automatic classification -----'
  # Get feed entries and loop over them
  f=feedparser.parse(feed)
  for entry in f['entries'][50:100]:
    num=num+1
    # Print the contents of the entry
    title=entry['title'].encode('utf-8').replace("'","")
    print 'Title:     '+ title
    description = splitRegexp.sub( "", entry[ "description" ] )
    
    print description #entry['description'].encode('utf-8')

    # Combine all the text to create one item for the classifier
    #fulltext='%s\n%s\n%s' % (entry['title'],entry['publisher'],entry['description'])
    fulltext='%s\n%s' % (entry['title'],entry['description'])
    fulltext=fulltext.replace("'","")
    # Print the best guess at the current category
    predicted=str(classifier.classify(fulltext))
    print 'Predicted: ', predicted

    # Ask the user to specify the correct category
    actual=raw_input('Enter actual category: ')
    feature=raw_input('Enter string classifier: ')

    #classifier.train(entry,cl)
    # probability the item should be in this category
    cp=round(classifier.cprob(feature,predicted),3)
    print 'cprob: ', str(cp)
    fischerprob1=round(classifier.fisherprob(feature,predicted),4)
    print 'fisherprob: ', str(fischerprob1)
    # Save the trained classifications
    # num, entry, feature, predicted, actual, cprob(feature, predicted)
    classifier.autoClassdb(num, title, feature, predicted, actual, cp) 
   # entryfeatures(entry)	
  #return classifier

def entryfeatures(entry):
  splitter=re.compile('\\W*')
  f={}
  
  # Extract the title words and annotate
  titlewords=[s.lower() for s in splitter.split(entry['title']) 
          if len(s)>2 and len(s)<20]
  for w in titlewords: f['Title:'+w]=1
  
  # Extract the description words
  descriptionwords=[s.lower() for s in splitter.split(entry['description']) 
          if len(s)>2 and len(s)<20]

  # Count uppercase words
  uc=0
  for i in range(len(descriptionwords)):
    w=descriptionwords[i]
    f[w]=1
    if w.isupper(): uc+=1
    
    # Get word pairs in description as features
    if i<len(descriptionwords)-1:
      twowords=' '.join(descriptionwords[i:i+1])
      f[twowords]=1
    
  # Removed: Keep creator and publisher whole
  #f['Publisher:'+entry['publisher']]=1

  # UPPERCASE is a virtual word flagging too much shouting  
  if float(uc)/len(descriptionwords)>0.3: f['UPPERCASE']=1
  print f
  return f

def main():
  cl=docclass.fisherclassifier(docclass.getwords)
  cl.setdb('dpaladhi.db')
  read('my_data.xml',cl)
main()