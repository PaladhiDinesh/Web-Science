#! /usr/bin/env python  
import os
import sys
import urllib
import time
import feedparser

from bs4 import BeautifulSoup

def checkNextPage(url):
    
    f = urllib.urlopen(url) 
    soup = BeautifulSoup(f.read(), from_encoding=f.info().getparam('charset'))
    
    try:
        link = soup.find('link', rel='next',href = True)['href']
    except TypeError:
        link = None
    return link
    
    
def main():
    feedlist   = open('100atomurls').readlines()
    
    for url in feedlist:
        try:
            d = feedparser.parse(url)
           
            title = d['feed']['title'] 
            
            count    = 1
            nextLink = checkNextPage( url )
            
            while nextLink:
                nextLink = checkNextPage( nextLink )
                count += 1
                
            print u'|'.join((str(count),title)).encode('utf-8').strip()
            
            
            
        except KeyError:
            pass      

if __name__ == '__main__':
    main()