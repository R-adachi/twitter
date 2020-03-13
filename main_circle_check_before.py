from pprint import pprint
import get_csv_module_v2 as getcsv
import get_list_module as getlist
import csv
import circle_check_rt_module as rt
import circle_check_fv_module as fv
import circle_check_fv_infvl_module as flfv
import time
import make_tlist_module as makelist

print('C?:',end="")
num = int(input())
c = 'c' + str(num)
bc = 'c' + str(num-1)

glist=getcsv.get_pre_grade(bc)
salist = []
rtlist = []
rtlist_tmp = []
fvlist = []
nfmlist = []
for i in glist:
    if(i[4]==('A' or 'S')):
        salist.append(i[2])
    elif(i[4]==('B' or '')):
        fvlist.append(i[2])
    elif(i[4]==('C' or 'D')):
        nfmlist.append(i[2])

rtlist_tmp = list(set(salist + getlist.get('ic')))
for i in rtlist_tmp:
    if(i not in nfmlist):
        if(i not in fvlist):
            rtlist.append(i)

# makelist.make(c+'rt',rtlist)
# makelist.make(c+'fv',fvlist)

for i in rtlist:
    rt.check(i)
for i in rtlist:
    fv.check(i)
for i in fvlist:
    flfv.check(i)
