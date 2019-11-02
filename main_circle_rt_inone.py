from pprint import pprint
import get_csv_module as getcsv
import get_list_module as getlist
import csv
import get_touraku_inone_module as touraku
import time
import day_place_module as dp
import get_ill_list_module as getillist

cnt=0
nlist=getcsv.getc97pre()
kekka_list=[]
clist=[]

alist=getcsv.getoverA()
unlist=getcsv.getUn()
illist=getillist.get()

alist.extend(illist)
alist.extend(unlist)
csvlist=list(set(alist))

for n in nlist:
    kekka=dp.seikei(n[1])
    if(len(kekka)>0):
        kekka_list.append([n[0],True])
        clist.append(n[0])

for c in csvlist:
    if(c not in clist):
        if(touraku.get(c)):
            kekka_list.append([c,True])
        else:
            kekka_list.append([c,False])


with open('../c97_check.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(kekka_list)
