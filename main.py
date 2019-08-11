from pprint import pprint
import get_csv_module as getcsv
import get_list_module as getlist
import csv
import get_pic_module as getpic
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
        if(i[3]=='4'):
            i.append(getpic.get(i[1],i[0],i[3],i[4]))
            cnt+=1
    if(cnt>30):
        stop=time.time()
        print('please wait:'+str(900-(stop-start)))
        time.sleep(900-(stop-start))
        start=time.time()
        cnt=0
#kekka[0]=['名前','アカウント','整合性チェック','お品書き','日','場所']

with open('../c96_1_kekka.csv', 'w' ,encoding="utf_8_sig") as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerows(kekka)
