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


tmp = list(getlist.get('ic'))


makelist.make('ica',tmp)
