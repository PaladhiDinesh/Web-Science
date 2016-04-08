import feedparser
import collections
import re
import operator 
import math


file_out = "tfidf.txt"

def getwordcounts(url):
    
    fd = feedparser.parse(url)
    wc        = collections.defaultdict(int)
    stopwords = []
    
    stopWordList = open('stopWordList.txt').readlines()
    pages = len(fd['entries'])
    
    for stopWord in stopWordList:
        stopWord = stopWord.strip()
        stopwords.append(stopWord)
    
    for e in fd.entries:
        if 'summary' in e:
            summary = e.summary
        else:
            summary = e.description
        words = getwords('%s %s' % (e.title, summary))
        
        for word in words:
            if word not in stopwords:
                wc[word] += 1
    
    if pages == 500:
        next_link = url + "?start-index=501"
        d         = feedparser.parse(next_link)
        pages     = len(d['entries'])
        for e in d.entries:
            if 'summary' in e:
                summary = e.summary
            else:
                summary = e.description

            words = getwords('%s %s' % (e.title, summary))
            
            for word in words:
                if word not in stopwords:
                    #print word
        
                    wc[word] += 1
                
        if pages == 500:
            next_link = url + "?start-index=1001"
            for e in d.entries:
                if 'summary' in e:
                    summary = e.summary
                else:
                    summary = e.description

                words = getwords('%s %s' % (e.title, summary))
                
                for word in words:
                    if word not in stopwords:
                        #print word
            
                        wc[word] += 1
            if pages == 500:
                next_link = url + "?start-index=1501"
                for e in d.entries:
                    if 'summary' in e:
                        summary = e.summary
                    else:
                        summary = e.description

                    words = getwords('%s %s' % (e.title, summary))
                    
                    for word in words:
                        if word not in stopwords:
                            wc[word] += 1
    
    if 'title' not in fd.feed:
        print 'Invalid url', url
        return 'bogus data', wc    

    return fd.feed.title, wc

def getwords(html):
    text  = re.compile(r'<[^>]+>').sub('', html)
    words = re.compile(r'[^A-z^a-z]+').split(text)
    return [word.lower() for word in words if word]

def main():

    # XXX: break this up into smaller functions, write tests for them

    apcount    = collections.defaultdict(int)
    wordcounts = {}
    feedlist   = open('100atomurls').readlines()
    totalWordCount = {}
    
    for url in feedlist:
        title, wc = getwordcounts(url)
        wordcounts[title] = wc
        
        for word, count in wc.iteritems():
            if count > 1:
                apcount[word] += 1
                
                try:
                    totalWordCount[word] += count
                except KeyError:
                    totalWordCount[word] = count
    
    wordlist = []
    
    
    for w, bc in apcount.iteritems():
        frac = float(bc)/len(feedlist)
        #print frac
        if frac > 0.1 and frac < 0.5:
            wordlist.append(w)
    
    countOfWords = []
    
    for word in wordlist:
        countOfWords.append((word,totalWordCount[word]))        
            
    countOfWords.sort(key=lambda rating: rating[1], reverse = True )
    
    countOfWords = countOfWords[0:500]
     
    out = file(file_out, 'w')
    out.write('Blog')
   
    idfWordCount = {}
    
    for w in countOfWords:
        word = w[0]
        noOfBlogs = 0
        for blogname, counts in wordcounts.iteritems():
            
            if word in counts:
                noOfBlogs += 1
            #print noOfBlogs
        idf = math.log( 100.0 / noOfBlogs  , 2 )
        
        
        idfWordCount[word]  = idf
    
    
    for w in countOfWords:
        #print w
        out.write('\t' + w[0])
    
    out.write('\n')
        
    for blogname, counts in wordcounts.iteritems():
        blogname = blogname.encode('UTF-8')
        out.write(blogname)     
        
        for w in countOfWords:     
            word = w[0]
            occurance = w[1]
             
            tf = float(counts[word]) / occurance
            tfidf = tf * idfWordCount[word]

            # d is integer, f is float
            out.write('\t%f' % tfidf)
        
        out.write('\n')
    
    out.close()

if __name__ == '__main__':
    main()