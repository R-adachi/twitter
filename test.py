from pprint import pprint
import get_csv_module as getcsv
import get_list_module as getlist
import csv
import get_pic_module as getpic
import time
import copy
import make_tlist_module as make_tlist

DAY=4

c='c97'

clist=getcsv.get()

kekka=copy.copy(clist)

cnt=0
t_idname_list=[]

for j in kekka:
    t_idname_list.append(j[2])

make_tlist.make(c+'d'+str(DAY),t_idname_list)
