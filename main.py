from pprint import pprint
import get_csv_module as getcsv
import get_list_module as getlist
import csv
import get_pic_module as getpic

clist=getcsv.get()
clist_name=getcsv.getname()
llist=getlist.get()

kekka=[['名前','アカウント','整合性チェック','お品書き']]

cnt=0

for i in clist:
    check=(i in llist)
    kekka.append([clist_name[cnt],i,check])
    cnt+=1

#del kekka[0]
#pprint(status_list[0].text)
#pprint(status_list)

for i in kekka:
    if(i[2]):
        i.append(getpic.get(i[1],i[0]))


with open('../c96_kekka.csv', 'w' ,encoding="utf_8_sig") as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerows(kekka)
