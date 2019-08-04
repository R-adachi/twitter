from pprint import pprint
import get_csv_module as getcsv
import get_list_module as getlist
import csv

clist=getcsv.get()
clist_name=getcsv.getname()
llist=getlist.get()

kekka=[[]]

cnt=0

for i in clist:
    check=(i in llist)
    kekka.append([clist_name[cnt],i,check])
    cnt+=1

del kekka[0]
#pprint(status_list[0].text)
#pprint(status_list)

with open('../c96_kekka.csv', 'w' ,encoding="utf_8_sig") as f:
    writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
    writer.writerows(kekka)     # list（1次元配列）の場合
