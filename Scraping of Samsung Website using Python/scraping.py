# -*- coding: utf-8 -*-
import requests
import json
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
import pandas as pd
headers = {"Accept":"*/*",
"Host":"api.bazaarvoice.com",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
"limit.q0":"30",
"offset.q0":"105"
}
limit = 100;
offset =100;
page = requests.get("https://www.verizonwireless.com/smartphones/samsung-galaxy-s7",headers=headers)
soup = BeautifulSoup(page.content,'html.parser')
name = soup.find_all(class_="fontSize_4 color_00 block")
name_last = soup.find_all(class_="fontSize_7 block")
name = name[0].get_text().strip()+" "+name_last[0].get_text().strip()
new=0
ans=100
#total=110
globallist =[]   
titlelist=['Device','Title','ReviewText','SubmissionTime','UserNickname']
globallist.append(titlelist)
#print(globallist)
#for getting total number of reviews
url = "https://api.bazaarvoice.com/data/batch.json?passkey=e8bg3vobqj42squnih3a60fui&apiversion=5.5&displaycode=6543-en_us&resource.q0=reviews&filter.q0=isratingsonly%3Aeq%3Afalse&filter.q0=productid%3Aeq%3Adev5800066&filter.q0=contentlocale%3Aeq%3Aen_US&sort.q0=rating%3Adesc&stats.q0=reviews&filteredstats.q0=reviews&include.q0=authors%2Cproducts%2Ccomments&filter_reviews.q0=contentlocale%3Aeq%3Aen_US&filter_reviewcomments.q0=contentlocale%3Aeq%3Aen_US&filter_comments.q0=contentlocale%3Aeq%3Aen_US&limit.q0="+str(100)+"&offset.q0="+str(1*offset)+"&limit_comments.q0=3&callback=bv_1111_57232"
html = urlopen(url).read().decode()
json_result = json.loads((str(html)[14:-1]))
total = json_result['BatchedResults']['q0']['TotalResults']
print("total: ",total)

#for getting review in multiples of 100
for limchange in range(0,round(total/100)):
#    print (limchange)  
    url = "https://api.bazaarvoice.com/data/batch.json?passkey=e8bg3vobqj42squnih3a60fui&apiversion=5.5&displaycode=6543-en_us&resource.q0=reviews&filter.q0=isratingsonly%3Aeq%3Afalse&filter.q0=productid%3Aeq%3Adev5800066&filter.q0=contentlocale%3Aeq%3Aen_US&sort.q0=rating%3Adesc&stats.q0=reviews&filteredstats.q0=reviews&include.q0=authors%2Cproducts%2Ccomments&filter_reviews.q0=contentlocale%3Aeq%3Aen_US&filter_reviewcomments.q0=contentlocale%3Aeq%3Aen_US&filter_comments.q0=contentlocale%3Aeq%3Aen_US&limit.q0="+str(ans)+"&offset.q0="+str(limchange*offset)+"&limit_comments.q0=3&callback=bv_1111_57232"
    html = urlopen(url).read().decode()
    json_result = json.loads((str(html)[14:-1]))
   
    for review in range(0,100):
        allreviews= json_result['BatchedResults']['q0']['Results'][review]['ReviewText'].replace("\n", " ")
        allreviews="".join( allreviews.splitlines())
        templist=[name,json_result['BatchedResults']['q0']['Results'][review]['Title'],allreviews,json_result['BatchedResults']['q0']['Results'][review]['SubmissionTime'][0:10],json_result['BatchedResults']['q0']['Results'][review]['UserNickname']]
#        print("Review: ",new+review+1,json_result['BatchedResults']['q0']['Results'][review]['ReviewText'])
#        print ("Username: ",json_result['BatchedResults']['q0']['Results'][review]['UserNickname'])
#        print ("Title: ",json_result['BatchedResults']['q0']['Results'][review]['Title'])
#        print ("Submission Time: ",json_result['BatchedResults']['q0']['Results'][review]['SubmissionTime'][0:10])
        globallist.append(templist)
    new=review+new+1
    
ans=total%100    
#for getting last reviews
url = "https://api.bazaarvoice.com/data/batch.json?passkey=e8bg3vobqj42squnih3a60fui&apiversion=5.5&displaycode=6543-en_us&resource.q0=reviews&filter.q0=isratingsonly%3Aeq%3Afalse&filter.q0=productid%3Aeq%3Adev5800066&filter.q0=contentlocale%3Aeq%3Aen_US&sort.q0=rating%3Adesc&stats.q0=reviews&filteredstats.q0=reviews&include.q0=authors%2Cproducts%2Ccomments&filter_reviews.q0=contentlocale%3Aeq%3Aen_US&filter_reviewcomments.q0=contentlocale%3Aeq%3Aen_US&filter_comments.q0=contentlocale%3Aeq%3Aen_US&limit.q0="+str(ans)+"&offset.q0="+str(ans)+"&limit_comments.q0=3&callback=bv_1111_57232"
html = urlopen(url).read().decode()
json_result = json.loads((str(html)[14:-1]))


for review in range(0,ans):
    allreviews= json_result['BatchedResults']['q0']['Results'][review]['ReviewText'].replace("\n", " ")
    allreviews="".join( allreviews.splitlines())
    templist1=[name,json_result['BatchedResults']['q0']['Results'][review]['Title'],allreviews,json_result['BatchedResults']['q0']['Results'][review]['SubmissionTime'][0:10],json_result['BatchedResults']['q0']['Results'][review]['UserNickname']]
#    print("Review: ",new+review+1,json_result['BatchedResults']['q0']['Results'][review]['ReviewText'])
#    print ("Username: ",json_result['BatchedResults']['q0']['Results'][review]['UserNickname'])
#    print ("Title: ",json_result['BatchedResults']['q0']['Results'][review]['Title'])
#    print ("Submission Time: ",json_result['BatchedResults']['q0']['Results'][review]['SubmissionTime'][0:10])
    globallist.append(templist1)
new=review+new+1

#print(globallist)
with open('reviews.csv', 'w',encoding='utf-8',newline='') as csv_file:
    writer = csv.writer(csv_file,delimiter =':',lineterminator='\n')
    writer.writerows(globallist)