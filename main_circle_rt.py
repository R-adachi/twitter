from pprint import pprint
import get_csv_module as getcsv
import get_list_module as getlist
import csv
import circle_check_rt_module as rt
import time

kekka=[[]]

cnt=0
start=time.time()
rt.check('c97pre')
#start=datetime(2019,11,1,(16 - 9),30)
kekka=[[]]
final=[[]]
cnt=0
while(cnt<10):
    rtlist=rt.check('c97pre')
    kekka.extend(rtlist)
    #final=list(set(kekka))
    time.sleep(30)
    cnt+=1
    print(cnt)

"""
with open('../c97pre.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(kekka)
"""
