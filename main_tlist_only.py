from pprint import pprint
import get_csv_module as getcsv
import get_list_andname_module as getlist
import csv
import get_pic_module as getpic
import time
import copy

llist=copy.copy(getlist.get())

kekka=[[]]

for i in llist:
    kekka.append(i)

#del kekka[0]
#pprint(status_list[0].text)
#pprint(status_list)

cnt=0
start=time.time()
for i in kekka:
    i.append(getpic.get(i[1],i[0]))
    cnt+=1
    if(cnt>30):
        stop=time.time()
        time.sleep(900-(stop-start))
        start=time.time()
        cnt=0
#kekka[0]=['名前','アカウント','整合性チェック','お品書き']

f = open("../myname.txt", "r")
myname = f.read()
f.close()

with open('../c96_'+myname+'.csv', 'w' ,encoding="utf_8_sig") as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerows(kekka)
