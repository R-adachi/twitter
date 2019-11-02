#import tweepy
#import key_module as getkey
from pprint import pprint
from datetime import datetime
import urllib.error
import urllib.request
import os
import copy
import get_csv_module as getcsv
import csv

csv_file=open("../c97_pre.csv","r",encoding="ms932",errors="",newline="")
f=csv.reader(csv_file,delimiter=",",doublequote=True,lineterminator="¥r¥n",quotechar='"',skipinitialspace=True)

header=next(f)

prelist=[[]]
prenamelist=[]
kekka_already_list=[]
kekka_new_list=[]

for row in f:
    if(row[2]!="" and (row[4]=='A' or row[4]=='S' or row[4]=='')):
        prelist.append(row[:5])
        prenamelist.append(str(row[2]))
del prelist[0]

csv_file.close()

clist=getcsv.getc97c()

for c in clist:
    if(c[0] in prenamelist):
        now_pre=prelist[prenamelist.index(c[0])]
        now_pre.append(c[1])
        kekka_already_list.append(now_pre)
    else:
        kekka_new_list.append(c)

with open('../c97_already.csv', 'w',encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerows(kekka_already_list)

f.close()

with open('../c97_new.csv', 'w',encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerows(kekka_new_list)

f.close()
