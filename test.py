#import tweepy
#import key_module as getkey
from pprint import pprint
import csv
from datetime import datetime
import urllib.error
import urllib.request
import os
import copy
import get_csv_module as getcsv
import day_place_module as dp

kekka_list=[]
nlist=getcsv.getc97pre()
for n in nlist:
    kekka=dp.seikei(n[1])
    if(len(kekka)>0):
        #print(n[0])
        kekka_list.append([n[0],kekka])
        #pprint(kekka_list)
#del kekka_list[0]

pprint(kekka_list)
