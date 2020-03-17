from pprint import pprint
import get_csv_module_v2 as getcsv
import get_list_module as getlist
import csv
import circle_check_rt_module as rt
import circle_check_fv_module as fv
import circle_check_fv_infvl_module as flfv
import time
import make_tlist_module as makelist
from progressbar import progressbar as pber


print('C?:',end="")
num = int(input())
c = 'c' + str(num)
bc = 'c' + str(num-1)



for i in pber(rtlist):
    rt.check(i)
for i in pber(rtlist):
    fv.check(i)
for i in pber(fvlist):
    flfv.check(i)
