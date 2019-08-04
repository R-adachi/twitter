from pprint import pprint
import get_csv_module as getcsv
import get_list_module as getlist

clist=getcsv.get()
llist=getlist.get()

for i in clist:
    print(i in llist)
