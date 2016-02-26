import commands
import re
import math
import json
file_1=open ('10_urls.txt','w')
find_memento = re.compile(r'rel.*?=.*?"https://www.linkedin.com/contacts/view?id=".*?') 
#fname="&trk=contacts-contacts-list-contact_name-0"
oc_doc1= 'lynx -dump'+"http://www.cs.odu.edu/~dpaladhi/Contacts%20_LinkedIn.html#?filter=recent"+'|'+'grep -i ' + "https://www.linkedin.com/contacts/view?id=" 
w_doc=commands.getoutput(oc_doc1)
file_1.write(w_doc)