from pprint import pprint
import get_csv_module as getcsv
import get_list_module as getlist
import csv
import soldout_check_module as soldcheck
import time

clist=getcsv.get()
clist_name=getcsv.getname()
llist=getlist.get()
daylist=getcsv.getday()
plist=getcsv.getp()

kekka=[[]]

cnt=0

for i in clist:
    check=(i in llist)
    kekka.append([clist_name[cnt],i,check,daylist[cnt],plist[cnt]])
    cnt+=1

del kekka[0]
#pprint(status_list[0].text)
#pprint(status_list)

cnt=0
start=time.time()
for i in kekka:
    if(i[2]):
        if(i[3]=='3'):
            soldcheck.check(i[1])
