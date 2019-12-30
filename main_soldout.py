from pprint import pprint
import get_csv_module as getcsv
import get_list_module as getlist
import csv
import soldout_check_module as soldcheck
import time

c='c97'
DAY=4

list=getlist.get(c+'d'+str(DAY))

cnt=0
start=time.time()
while(1):
    for i in list:
        soldcheck.check(i)
        time.sleep(8)
